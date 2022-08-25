# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import camera_pb2 as camera__pb2
import camera_service_pb2 as camera__service__pb2


class CameraServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/pbCamera.CameraServer/Init',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.SetCameraParam = channel.unary_unary(
                '/pbCamera.CameraServer/SetCameraParam',
                request_serializer=camera__pb2.SetMetadata.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.GetCameraParam = channel.unary_unary(
                '/pbCamera.CameraServer/GetCameraParam',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__pb2.Metadata.FromString,
                )
        self.StartPreview = channel.unary_unary(
                '/pbCamera.CameraServer/StartPreview',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.StopPreview = channel.unary_unary(
                '/pbCamera.CameraServer/StopPreview',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.StartVideo = channel.unary_unary(
                '/pbCamera.CameraServer/StartVideo',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.StopVideo = channel.unary_unary(
                '/pbCamera.CameraServer/StopVideo',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.TakeSnapshot = channel.unary_unary(
                '/pbCamera.CameraServer/TakeSnapshot',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.StopSnapshot = channel.unary_unary(
                '/pbCamera.CameraServer/StopSnapshot',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__service__pb2.CommandAck.FromString,
                )
        self.CameraStatus = channel.unary_stream(
                '/pbCamera.CameraServer/CameraStatus',
                request_serializer=camera__service__pb2.ParamNone.SerializeToString,
                response_deserializer=camera__pb2.Event.FromString,
                )


class CameraServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCameraParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCameraParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPreview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPreview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopVideo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TakeSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CameraStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CameraServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'SetCameraParam': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCameraParam,
                    request_deserializer=camera__pb2.SetMetadata.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'GetCameraParam': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCameraParam,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__pb2.Metadata.SerializeToString,
            ),
            'StartPreview': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPreview,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'StopPreview': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPreview,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'StartVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StartVideo,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'StopVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StopVideo,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'TakeSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.TakeSnapshot,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'StopSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSnapshot,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__service__pb2.CommandAck.SerializeToString,
            ),
            'CameraStatus': grpc.unary_stream_rpc_method_handler(
                    servicer.CameraStatus,
                    request_deserializer=camera__service__pb2.ParamNone.FromString,
                    response_serializer=camera__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pbCamera.CameraServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CameraServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/Init',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCameraParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/SetCameraParam',
            camera__pb2.SetMetadata.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCameraParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/GetCameraParam',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__pb2.Metadata.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartPreview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/StartPreview',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopPreview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/StopPreview',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/StartVideo',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/StopVideo',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TakeSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/TakeSnapshot',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbCamera.CameraServer/StopSnapshot',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__service__pb2.CommandAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CameraStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pbCamera.CameraServer/CameraStatus',
            camera__service__pb2.ParamNone.SerializeToString,
            camera__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)