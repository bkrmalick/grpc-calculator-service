from __future__ import print_function

import random
import logging

import grpc

import calculator_pb2 as types
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:6900') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        print("Service Info: ",stub.info(types.Empty()))

        add_ans=stub.add(types.TwoFloats(first=1, second=2))
        print("1+2= ",add_ans.n)

        sub_ans=stub.sub(types.TwoFloats(first=1, second=2))
        print("1-2= ",sub_ans.n)

        rand_iterator = stub.rand(types.Empty()) # get iterator from server
        print("First Random Number: ",next(rand_iterator).n)
        print("Second Random Number: ",next(rand_iterator).n)



if __name__ == '__main__':
    logging.basicConfig()
    run()