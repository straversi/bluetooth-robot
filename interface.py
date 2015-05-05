import stocks as s
import giants as g
import serial
import time

def main():
	ser = serial.Serial('/dev/cu.HC-06-DevB', 9600)
	lastScore = 0
	gameTime = 0
	gameState = {}
	lastGameState = g.gameday(0)
	stocks = s.update()
	num = stocks["GOOG"]["ChangePercent"]
	while True:
		print "updating..."
		# giants = g.update()
		if gameTime < len(g.game):
			gameState = g.gameday(gameTime)
		print "done."
		time.sleep(2)
		gameTime += 1

		# First write is winner: 0, 1
		if gameState["winner"] == "SF":
			ser.write("1")
		else:
			ser.write("0")

		# Second write is score change: 0, 1
		if gameState["runs"] > lastGameState["runs"]:
			ser.write("%d" % (gameState["runs"] - gameState["runsOpp"]))
		else:
			ser.write("0")

		# Third write is hit change: 0, 1
		if gameState["hits"] > lastGameState["hits"]:
			ser.write("1")
		else:
			ser.write("0")

		# Fourth write is winning or not: 0, 1, 2
		if gameState["runs"] > gameState["runsOpp"]:
			ser.write("2")
		elif gameState["runs"] == gameState["runsOpp"]:
			ser.write("1")
		else:
			ser.write("0")

		# Fifth write is stock change: 0, 1, 2
		if num < -1:
			num = 0
		elif num > 1:
			num = 2
		else:
			num = 1
		ser.write("%d" % num)
		print lastGameState
		print gameState
		lastGameState = gameState

if __name__ == '__main__':
	main()