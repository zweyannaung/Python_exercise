import socket
import mysql.connector
import node_tdb


class Server:
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 9191

    def main(self):
        bstdb_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bstdb_server.bind((self.server_ip, self.server_port))
        bstdb_server.listen()
        print("##### Server is listening now !!!")
        try:
            while True:
                client, address = bstdb_server.accept()
                self.client_control(client)

        except Exception as err:
            print(err)

    def client_control(self, client):
        with client as sock:
            from_client = sock.recv(1024).decode('utf-8')
            if from_client == "Build Tree Database":
                self.build_tree_database()
            sock.send(bytes("hello from server", "utf-8"))

    def build_tree_database(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password=" ", database="mytest")
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM bstdb")
        result = my_cursor.fetchall()
        main_node = node_tdb.Rawdata(result).build_tree()
        node_tdb.Rawdata(result).adding_node(main_node)


if __name__ == "__main__":
    bstdb = Server()
    bstdb.main()

# tommorrow work sqldb ကို node tree ဆောက်ရမယ်
# adding_node from node_tdb.py ကိုဆက်ရေးရမယ်
