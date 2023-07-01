import socketserver
import game_objects
import game

ADDRESS = ('localhost', 8080)


class PonguinServer(socketserver.ThreadingMixIn, socketserver.UDPServer): pass


class RequestHandler(socketserver.DatagramRequestHandler):

    def handle(self) -> None:
        pass


def main():
    server = None
    try:
        server = PonguinServer(ADDRESS, RequestHandler)
        server.serve_forever()
    except Exception as err:
        print(err)
