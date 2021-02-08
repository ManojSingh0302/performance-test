#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
This contains to load test of Hello World example of gRPC call with locust.
This implementation of locust with gRPC having stopwatch method moved in libs.
"""

# Built-in/Generic Imports
import sys
import grpc


# Libs
from locust.contrib.fasthttp import FastHttpUser
from locust import task, events, constant
from gRPC_services.libs.service_defination import stopwatch
from server.python.helloworld import helloworld_pb2
from server.python.helloworld import helloworld_pb2_grpc

__author__ = 'Manoj Singh'


class GRPCServerClient:

	@stopwatch
	# this is the method we want to measure
	def hello_world(self, message):
		try:
			with grpc.insecure_channel('127.0.0.1:50051') as channel:
				stub = helloworld_pb2_grpc.GreeterStub(channel)
				response = stub.SayHello(helloworld_pb2.HelloRequest(name=message))
				print(response)
		except (KeyboardInterrupt, SystemExit):
			sys.exit(0)


class GRPCMyLocust(FastHttpUser):
	host = 'http://127.0.0.1:50051'
	wait_time = constant(0)
	grpc_server_client = GRPCServerClient()

	def on_start(self):
		""" on_start is called when a Locust start before any task is scheduled """
		pass

	def on_stop(self):
		""" on_stop is called when the TaskSet is stopping """
		pass

	@task
	def grpc_client_task(self):
		"""To be updated"""
		message = "Hello World!"
		self.grpc_server_client.hello_world(message)
