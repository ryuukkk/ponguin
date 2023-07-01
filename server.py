import socketserver
import game_objects
import game


class PonguinServer(socketserver.ThreadingMixIn, socketserver.UDPServer): pass

class RequestHandler(socketserver.DatagramRequestHandler):

    def handle(self) -> None:
