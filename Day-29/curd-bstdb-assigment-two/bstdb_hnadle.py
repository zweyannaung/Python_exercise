import mysql_db
import mysql.connector


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
    # result = mysql_db.Sqldb.data_fetching(self=None)
    # print(result)
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
    print(release)


def add_all_node(dbData, node):
    for i in dbData:
        insert_data(i, node)


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
    # # find_node(main_node, 28)
    # crud_bstdb = Crud_bstdb()
    # # print(crud_bstdb)
    # crud_bstdb.project_start(main_node)
