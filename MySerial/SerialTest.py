import serial

t = serial.Serial('COM3',115200)
st = '';
while(True):
    c = t.read(1);
    if(c!=b'\n'):
        st+=c.decode();
    else:
        print(st);
        st = '';