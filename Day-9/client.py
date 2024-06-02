import socket


class My_client():
    def __init__(self, sms):
        self.target_ip = "localhost"
        self.target_port = 9998
        self.send_and_recv_data = {}
        self.client_sms = bytes(sms, 'utf-8')
        self.send_and_recv_data.update({len(self.send_and_recv_data): sms})

    def run_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        client.send(self.client_sms)
        received_from_server = client.recv(1024)
        recv_sms = received_from_server.decode("utf-8")
        self.send_and_recv_data.update({len(self.send_and_recv_data): recv_sms})
        print("Go back Data from sever:", recv_sms)
        client.close()


if __name__ == '__main__':
    while True:
        sms: str = input("Enter some data to send:> ")
        my_client = My_client(sms)
        my_client.run_client()
