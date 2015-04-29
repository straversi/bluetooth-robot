import stocks as s
import giants as g
import serial
import time

def main():
	# ser = serial.Serial('/dev/cu.HC-06-DevB', 9600)
	while True:
		print "updating..."
		stocks = s.update()
		giants = g.update()
		print "done."
		time.sleep(5)
		num = stocks["GOOG"]["ChangePercent"]
		if giants["winner"]:
			win = "1"
		else
			win = "0"
		ser.write("%d\n" % win)
		ser.write("%d\n" % num)
		print num

if __name__ == '__main__':
	main()