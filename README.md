# bluetooth-robot

### Initialization
```shell
pip install pyserial
```
Then use the OS to pair with the HC-06 Bluetooth sheild.
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
