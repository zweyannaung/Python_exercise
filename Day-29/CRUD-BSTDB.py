
class Crud_bstdb:
    def __init__(self):
        pass

    def project_start(self):
        user_request = input("Press: (1) for add new TDB or Press: (2) for find TDB data => ")
        print(user_request)


if __name__ == "__main__":
    crud_bstdb = Crud_bstdb()
    crud_bstdb.project_start()
