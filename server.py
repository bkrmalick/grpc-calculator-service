from concurrent import futures
import time
import math
import logging
import random

import grpc

import calculator_pb2 as types
import calculator_pb2_grpc


start_time = None # GLOBAL VARIABLE

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def add(self, request, context):
        return types.Float(n=request.first+request.second)

    def sub(self, request, context):
        return types.Float(n=request.first-request.second)

    def rand(self, request, context):
        while True:
          yield types.Integer(n=random.randint(0, 101))

    def info(self, request, context):
        elapsed = time.time() - start_time
        return types.CalcInfo(name = "Calculator Service V1", upSinceInSeconds=elapsed )



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)
    server.add_insecure_port('[::]:6900')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    start_time = time.time()
    serve()
