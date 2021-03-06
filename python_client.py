import grpc
import customer_pb2
import customer_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = customer_pb2_grpc.CustomerStub(channel)


def without_address():
    request_message1 = customer_pb2.CustomerRequest(id=1,
                                                    name='Vasya')
    response1 = stub.CreateCustomer(request_message1)

    print("Customer received: " + str(response1.id))
    print("Customer received: " + str(response1.success))


def with_address():
    address_message = customer_pb2.CustomerRequest.Address(street='Пресненская набережная',
                                                           city='Москва',
                                                           isShippingAddress=True)
    request_message2 = customer_pb2.CustomerRequest(id=2,
                                                    name='Petya',
                                                    addresses=[address_message])
    response2 = stub.CreateCustomer(request_message2)

    print("Customer received: " + str(response2.id))
    print("Customer received: " + str(response2.success))


without_address()
with_address()
