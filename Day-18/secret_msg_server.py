import socket
import server_EncDec


class SecretMsgServer:
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9191

    def main(self):
        secret_msg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secret_msg.bind((self.server_ip, self.server_port))
        secret_msg.listen()
        print("##### Server is Listening now !!!")

        try:
            while True:
                client, adderss = secret_msg.accept()
                print("##### Server is Accept Connection form Client !!!!!")
                self.client_control(client)

        except Exception as err:
            print(err)

    def client_control(self, client):
        with client as sock:
            form_client = sock.recv(1024)
            rec_data = form_client.decode("utf-8")
            print(rec_data)
            pre_decryption = server_EncDec.PowerOfDecrypt().decryption(rec_data)
            dec_data = str(pre_decryption)
            print(dec_data)
            my_msg: str = "We got your data "
            per_encryption = server_EncDec.PowerOfEncrypt().encryption(my_msg, "Server")
            sock.send(bytes(per_encryption, "utf-8"))


if __name__ == "__main__":
    secret_msg = SecretMsgServer()
    secret_msg.main()
