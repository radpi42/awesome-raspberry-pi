msg = 'this is where you can add devices to your device list'

print(msg)

devices =  []
while True:
    print('enter deivce IP address: [eg: 192.168.10.X]')
    device = input()
    if device == '':
        break
    devices = devices + [device]
print('devices to check:')
for device in devices:
    print(device)

