class Node:
    def __init__(self):
        self.data = myData
        self.left = None
        self.right = None


class Rawdata:
    def __init__(self, result):
        self.rawData = result

    def build_tree(self):
        get_db = self.rawData
        chosen_one = int(len(get_db) / 2)
        root_node = Node(get_db[chosen_one])
        return root_node

    def adding_node(self):
        node_now = node[0]
        get_db = node[1]
        print(node_now, get_db)
        chosen_one = int(len(my_BSTDB) / 2)
        res = [_ for _ in my_BSTDB if _['power-ranking'] == "Lower-B"]  # #############################################
        insert_data(res[0], node)
        res_two = [_ for _ in my_BSTDB if _['power-ranking'] == "Upper-A"]
        insert_data(res_two[1], node)
        release = [i for i in my_BSTDB if
                   i["_id"] != res[0]["_id"] and i["_id"] != res_two[1]["_id"] and i["_id"] != my_BSTDB[chosen_one]["_id"]]
        add_all_node(release, node)
        print(release)


#
if __name__ == "__main__":
    raw = Rawdata()
    my_tree = raw.build_tree()
