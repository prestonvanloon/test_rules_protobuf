# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Reference implementation for health checking in gRPC Python."""

import threading
import grpc

from protos.health import health_pb2
from protos.health import health_pb2_grpc

#def run():
#    channel = grpc.insecure_channel('localhost:50051')
#    stub = health_pb2_grpc.HealthStub(channel)
#    response = stub.Check(health_pb2.HealthCheckRequest())
#    print("Health client received: " + response.message)

def print_bottle(note_string):
    my_bottle = health_pb2.Bottle(note='Ahoy!')
    return my_bottle.SerializeToString()
