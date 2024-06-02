import socket
import enc_dec


class SecretMsgClient:

    def __init__(self):
        self.target_ip = "localhost"
        self.target_port = 9191
        self.user_key = self.get_key()

    def get_key(self):
        user_key: str = input("Enter your secret key for the whole precess !! :>> ")
        return user_key

    def client_runner(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))
        return client

    def client_menu(self):
        print("##### This is client menu")
        user_choice = input("get: get all infomation\n login: for login\n reg: to register \n press: 1 to send data\n "
                            "press: 2 to exit :>>")

        if user_choice == "1":
            user_data: str = input("Enter some data to test :>> ")
            self.encrypt_data_from_client(user_data)

    def encrypt_data_from_client(self, user_data):
        client = self.client_runner()
        print(self.user_key)
        pre_encryption = enc_dec.PowerOfEncrypt().encryption(user_data, self.user_key)
        client.send(bytes(pre_encryption, "utf-8"))
        data_rec = client.recv(4096).decode("utf-8")
        pre_decryption = enc_dec.PowerOfDecrypt().decryption(data_rec)
        dec_data = str(pre_decryption)
        client.close()
        print(dec_data)


if __name__ == "__main__":
    secret_msg = SecretMsgClient()
    while True:
        secret_msg.client_menu()
