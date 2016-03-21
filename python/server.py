#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append('gen-py')
from calculator import Calculator
import calculator.ttypes as calculator
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.server import TServer

class CalculatorHandler():
    def ping(self):
        print("ping request")
        return 1


host = "127.0.0.1"
port = 9090
handler = CalculatorHandler()
processor = Calculator.Processor(handler)
transport = TSocket.TServerSocket(host=host, port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
print("serving {0}:{1}...".format(host, port))
server.serve()