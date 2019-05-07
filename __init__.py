# coding:utf-8
import grpc
import beehive_job_info_pb2
import beehive_job_info_pb2_grpc


class Client(object):

    def __init__(self, host):
        self.host = host

    def __call__(self, *args, **kwargs):
        channel = grpc.insecure_channel(self.host)
        client = beehive_job_info_pb2_grpc.JobServiceStub(channel)
        return client