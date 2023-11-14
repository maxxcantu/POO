
from xmlrpc.server import SimpleXMLRPCRequestHandler


class Servidor(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
