# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from shadowsocks.protos import (
    aioshadowsocks_pb2 as shadowsocks_dot_protos_dot_aioshadowsocks__pb2,
)


class ssStub(object):
    """service
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateUser = channel.unary_unary(
            "/aioshadowsocks.ss/CreateUser",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.FromString,
        )
        self.UpdateUser = channel.unary_unary(
            "/aioshadowsocks.ss/UpdateUser",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.FromString,
        )
        self.GetUser = channel.unary_unary(
            "/aioshadowsocks.ss/GetUser",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.FromString,
        )
        self.DeleteUser = channel.unary_unary(
            "/aioshadowsocks.ss/DeleteUser",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.Empty.FromString,
        )
        self.InitUserServer = channel.unary_unary(
            "/aioshadowsocks.ss/InitUserServer",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserServer.FromString,
        )
        self.GetUserServer = channel.unary_unary(
            "/aioshadowsocks.ss/GetUserServer",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserServer.FromString,
        )
        self.StopUserServer = channel.unary_unary(
            "/aioshadowsocks.ss/StopUserServer",
            request_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.SerializeToString,
            response_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.Empty.FromString,
        )


class ssServicer(object):
    """service
  """

    def CreateUser(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateUser(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUser(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteUser(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def InitUserServer(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserServer(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def StopUserServer(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ssServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateUser": grpc.unary_unary_rpc_method_handler(
            servicer.CreateUser,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.SerializeToString,
        ),
        "UpdateUser": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateUser,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.SerializeToString,
        ),
        "GetUser": grpc.unary_unary_rpc_method_handler(
            servicer.GetUser,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.User.SerializeToString,
        ),
        "DeleteUser": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteUser,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.Empty.SerializeToString,
        ),
        "InitUserServer": grpc.unary_unary_rpc_method_handler(
            servicer.InitUserServer,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserServer.SerializeToString,
        ),
        "GetUserServer": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserServer,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserServer.SerializeToString,
        ),
        "StopUserServer": grpc.unary_unary_rpc_method_handler(
            servicer.StopUserServer,
            request_deserializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.UserIdReq.FromString,
            response_serializer=shadowsocks_dot_protos_dot_aioshadowsocks__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "aioshadowsocks.ss", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))