# bluetooth-robot

### Initialization
```shell
pip install pyserial
```
Then use the OS to pair with the HC-06 Bluetooth shield.
After you have succesfully paired with the device, run
```shell
python -m serial.tools.list_ports
```
This will list current Bluetooth ports available. Look for something like
```shell
/dev/cu.HC-06-DevB
```
Remember that.
Now, open Python (2.7) and import the library.
```python
import serial
ser = serial.Serial('/dev/cu.HC-06-DevB', 9600)
```
The light on the shield should go solid, indicating that it is connected.
You may now use commands such as
```python
ser.write('1')
ser.readline()
```


## stocks.py

Add a company symbol to `symbols` to include it in the search results.

Here is an example of changePercent after running main()
```python
>>> changePercent
{'AAPL': 1.76542830825914, 'NFLX': 1.79174240457024, 'GOOG': -1.49391625701634}
```
