import socket
import subprocess
import threading


class My_sever():

    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9998
        self.toSave = {}

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        # server.listen(1)
        # print(f'[*] Listening on {self.server_ip}:{self.server_port}')
        # while True:
        #     client, address = server.accept()
        #     print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        #     client_handler = threading.Thread(target=self.handle_client, args=(client,))
        #     client_handler.start()
        server.listen()
        print("Server is listen on ip:{} and port:{} ".format(self.server_ip, self.server_port))
        try:
            while True:
                client, address = server.accept()
                print("Accept connection form - {} : {} ".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client_socket):
        with client_socket as sock:
            from_client = sock.recv(1024)
            received_data = from_client.decode("utf-8")
            print("Running command: ", received_data)

            try:
                output = subprocess.getoutput("dir")
                print("***********\n", output)
                print("*****************")
            except Exception as err:
                print(err)
            # self.toSave.update(received_data)
            message = "server got it:>" + received_data
            # print(message)
            to_send = bytes(message, "utf-8")
            print("hello", to_send)
            sock.send(to_send)


if __name__ == '__main__':
    my_server = My_sever()
    my_server.main()
