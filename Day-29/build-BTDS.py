my_BSTDB: object = {
    0: {"_id": 3, "name": "Mg_Kaung", "age": "19", "email": "mgkaung@gmail.com", "ph-num": "111222333",
        "power-ranking": "lower-C"},
    1: {"_id": 7, "name": "Ba_Kyaw", "age": "22", "email": "bakyaw@gmail.com", "ph-num": "222333444",
        "power-ranking": "Upper-C"},
    2: {"_id": 10, "name": "La_Yin", "age": "25", "email": "layin@gmail.com", "ph-num": "333444555",
        "power-ranking": "lower-B"},
    3: {"_id": 13, "name": "Kyaw_Gyi", "age": "28", "email": "kyawgyi@gmail.com", "ph-num": "444555666",
        "power-ranking": "Upper-B"},
    4: {"_id": 15, "name": "Hla_Htay", "age": "19", "email": "hlahtay@gmail.com", "ph-num": "555666777",
        "power-ranking": "Upper-B"},
    5: {"_id": 18, "name": "Hsu_lat", "age": "22", "email": "hsulat@gmail.com", "ph-num": "666777888",
        "power-ranking": "lower-A"},
    6: {"_id": 20, "name": "Mj_Kyar_lay", "age": "25", "email": "mjkyarlay@gmail.com", "ph-num": "777888999",
        "power-ranking": "lower-A"},
    7: {"_id": 21, "name": "Ba_Htoo", "age": "33", "email": "bahtoo@gmail.com", "ph-num": "888999000",
        "power-ranking": "Upper-A"},
    8: {"_id": 24, "name": "Than_Hlaing", "age": "23", "email": "thanhlaing@gmail.com", "ph-num": "999000111",
        "power-ranking": "Upper-A"},
    9: {"_id": 28, "name": "Hla_Shwe", "age": "24", "email": "hlashwe@gmail.com", "ph-num": "111333444",
        "power-ranking": "Upper-A"},
    10: {"_id": 30, "name": "Manaw", "age": "25", "email": "manaw@gmail.com", "ph-num": "111444555",
         "power-ranking": "Upper-A"},
}


class Node:
    def __init__(self, myData):
        self.data = myData
        self.left = None
        self.right = None


def insert_data(new_data, node):
    if node is None:
        root: Node = Node(new_data)
        return root

    if new_data < node.data:
        node.left = insert_data(new_data, node.left)

    else:
        node.right = insert_data(new_data, node.right)

    return node


if __name__ == '__main__':
    root_node = Node(15)
    root_node = insert_data(10, root_node)
    root_node = insert_data(20, root_node)
    print(root_node.data)
