import socket


class Client:
    def __init__(self):
        self.target_ip = 'localhost'
        self.target_port = 9191

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client

    def client_menu(self):
        client = self.client_runner()
        print("##### You can choose what you want !!")
        try:
            my_value = input("Press: 1 for get Binary Search Tree Database !!\nPress: 2 for add node !!\n:>>  ")
            if my_value == "1":
                user_request = "Build Tree Database"
                client.send(bytes(user_request, "utf-8"))
            elif my_value == "2":
                pass
            else:
                self.client_menu()
        except Exception as err:
            print(err)

        recv_info = client.recv(4069).decode('utf-8')
        print(recv_info)


if __name__ == "__main__":
    my_client = Client()
    while True:
        my_client.client_menu()
