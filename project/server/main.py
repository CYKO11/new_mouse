import time
import server
import keyboard

socketServer = server.socketServer(5000)

while True:
    socketServer.listenForConnection()

    try:
        while True:
            data = socketServer.readFromConnection()
            if not data:
                time.sleep(0.01)
            else:
                print(data)
                keyboard.press_and_release('windows')
    except IOError:
        socketServer.closeConnection();
        break;
    else:
        socketServer.closeConnection();
        break;
