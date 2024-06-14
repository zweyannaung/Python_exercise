my_BSTDB: list = [
    {"_id": 3, "name": "Mg_Kaung", "age": "19", "email": "mgkaung@gmail.com", "ph-num": "111222333",
     "power-ranking": "Lower-C"},
    {"_id": 7, "name": "Ba_Kyaw", "age": "22", "email": "bakyaw@gmail.com", "ph-num": "222333444",
     "power-ranking": "Upper-C"},
    {"_id": 10, "name": "La_Yin", "age": "25", "email": "layin@gmail.com", "ph-num": "333444555",
     "power-ranking": "Lower-B"},
    {"_id": 13, "name": "Kyaw_Gyi", "age": "28", "email": "kyawgyi@gmail.com", "ph-num": "444555666",
     "power-ranking": "Upper-B"},
    {"_id": 15, "name": "Hla_Htay", "age": "19", "email": "hlahtay@gmail.com", "ph-num": "555666777",
     "power-ranking": "Upper-B"},
    {"_id": 18, "name": "Hsu_lat", "age": "22", "email": "hsulat@gmail.com", "ph-num": "666777888",
     "power-ranking": "Lower-A"},
    {"_id": 20, "name": "Mj_Kyar_lay", "age": "25", "email": "mjkyarlay@gmail.com", "ph-num": "777888999",
     "power-ranking": "Lower-A"},
    {"_id": 21, "name": "Ba_Htoo", "age": "33", "email": "bahtoo@gmail.com", "ph-num": "888999000",
     "power-ranking": "Upper-A"},
    {"_id": 24, "name": "Than_Hlaing", "age": "23", "email": "thanhlaing@gmail.com", "ph-num": "999000111",
     "power-ranking": "Upper-A"},
    {"_id": 28, "name": "Hla_Shwe", "age": "24", "email": "hlashwe@gmail.com", "ph-num": "111333444",
     "power-ranking": "Upper-A"},
    {"_id": 30, "name": "Manaw", "age": "25", "email": "manaw@gmail.com", "ph-num": "111444555",
     "power-ranking": "lower-S"},
]


class Node:
    def __init__(self, myData):
        self.data = myData
        self.left = None
        self.right = None


def insert_data(new_data, node):
    if node is None:
        root: Node = Node(new_data)
        return root

    if new_data["_id"] < node.data["_id"]:
        node.left = insert_data(new_data, node.left)

    else:
        node.right = insert_data(new_data, node.right)

    return node


def build_tree():
    chosen_one = int(len(my_BSTDB) / 2)
    root_node = Node(my_BSTDB[chosen_one])
    return root_node
    # print(my_BSTDB[chosen_one])


def adding_node(node):
    chosen_one = int(len(my_BSTDB) / 2)
    res = [_ for _ in my_BSTDB if _['power-ranking'] == "Lower-B"]  # #############################################
    insert_data(res[0], node)
    res_two = [_ for _ in my_BSTDB if _['power-ranking'] == "Upper-A"]
    insert_data(res_two[1], node)
    release = [i for i in my_BSTDB if
               i["_id"] != res[0]["_id"] and i["_id"] != res_two[1]["_id"] and i["_id"] != my_BSTDB[chosen_one]["_id"]]
    add_all_node(release, node)
    # print(release)


def add_all_node(dbData, node):
    for i in dbData:
        insert_data(i, node)


# ################ user ကရိုက်ထည့်လိုက်တဲ့တန်ဖိုးကိုbstdb ထဲမှာ ရှာခြင်း

def find_node(node: Node, sdata):
    if node:
        find_node(node.left, sdata)
        if node.data["name"] == sdata or node.data["email"] == sdata or node.data["ph-num"] == sdata:
            print(node.data)
        find_node(node.right, sdata)
    """
    if node is not None:
        find_node(node.left, fkey)
        if node.data["_id"] == fkey:
            print(node.data)
        find_node(node.right, fkey)
    """





# def code_start():
#     main_node = build_tree()
#     adding_node(main_node)
#     find_node(main_node, 28)


class Crud_bstdb:
    def __init__(self):
        pass

    def project_start(self, node):
        while True:
            user_request = input("Press: (1) for add new TDB or Press: (2) for find TDB data => ")
            if user_request == '1':
                pass
            elif user_request == '2':
                user_search: str = input("Enter your search: name / email / ph-num => ")
                find_node(node, user_search)
            else:
                self.project_start(node)


if __name__ == '__main__':
    main_node = build_tree()
    adding_node(main_node)
    # find_node(main_node, 28)
    crud_bstdb = Crud_bstdb()
    # print(crud_bstdb)
    crud_bstdb.project_start(main_node)

