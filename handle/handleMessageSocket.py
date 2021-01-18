from model.model import Model
import socket
class handleMessageSocket:
    def getIpClient(self):
        return socket.gethostbyname(socket.gethostname())