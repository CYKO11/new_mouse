import client
import ad1115
import time

socketClient = client.socketClient("192.168.8.100",5000)
board = ad1115.A2DC()
rawData = None
temp = None

while True:
    rawData = board.readSampleSet(4);
    # temp = ""
    # for value in rawData:
    #     temp += str(value) + " , "
    # temp += "\n"
    # socketClient.send('windows');

    # print(rawData[2][0])
    # print(type(rawData[2][0]))
    if rawData[3][0] > 3:
        socketClient.send('windows' + str(rawData[3][0]));
    time.sleep(0.4)
    rawData = None

socketClient.closeConn()