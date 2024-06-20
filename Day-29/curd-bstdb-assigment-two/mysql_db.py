import _mysql_connector
import mysql.connector

for_bstdb = [
    (3, "My_kaung", 19, "mgkaung@gmail.com", 111222333, "Lower-C"),
    (7, "Ba_Kyaw", 22, "bakyaw@gmail.com", 222333444, "Upper-C"),
    (10, "La_Yin", 25, "layin@gmail.com", 333444555, "Lower-B"),
    (13, "Kyaw_Gyi", 28, "kyawgyi@gmail.com", 444555666, "Upper-B"),
    (15, "Hla_Htay", 19, "hlahtay@gmail.com", 555666777, "Upper-B"),
    (18, "Hsu_Lat", 22, " hsulat@gmail.com", 666777888, "Lower-A"),
    (20, "Mj_Kyar_Lay", 25, "mjkyarlay@gmail.com", 777888999, "Lower-A"),
    (21, "Ba_Htoo", 33, "bahtoo@gmail.com", 888999000, "Upper-A"),
    (24, "Than_Hlaing", 23, "thanhlaing@gmail.com", 999000111, "Lower-A"),
    (28, "Hla_Shwe", 24, "hlashwe@gmail.com", 111333444, "Upper-A"),
    (30, "Manaw", 25, "manaw@gmail.com", 111444555, "Upper-A"),
]


class Sqldb:
    def __init__(self):
        self.from_db = []

    def make_connection_to_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="mytest"
        )
        my_cursor = mydb.cursor()
        # my_formula = "INSERT INTO bstdb (_id, name, age, email, ph_num, power_ranking) VALUES (%s,%s,%s,%s,%s,%s)"
        # my_cursor.executemany(my_formula, for_bstdb)
        # mydb.commit()

    def data_fetching(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="mytest"
        )
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM bstdb")
        result = my_cursor.fetchall()
        result_now = []
        for i in result:
            result_now.append(i)
        return result_now

    def test_db(self, sqldb):
        for i in sqldb:
            print(i["id"])


if __name__ == "__main__":
    sqldb = Sqldb()
    # abbr = sqldb.my_test()
    # sqldb.make_connection_to_db()
    fetching_result = sqldb.data_fetching()
    sqldb.test_db(fetching_result)
    # sqldb.show_db(abbr)
