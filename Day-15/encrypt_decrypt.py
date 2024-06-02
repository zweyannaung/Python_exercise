import random


class PowerOfEncrypt:
    def __init__(self):
        self.text: str = "Mingalarbar"
        self.key: str = "Hello"
        self.random_key = random.randint(1, 1024)
        self.encryption_code = ""

    def encryption(self):
        total_key = 0
        bin_total_key = ''
        for i in self.key:
            total_key += ord(i)

        for j in self.text:
            change_ord = ord(j)
            change_ciph = change_ord ^ total_key
            double_ciph = change_ciph ^ self.random_key
            self.encryption_code += str(hex(double_ciph)) + 'X'
        self.encryption_code += hex(total_key) + "X" + hex(self.random_key)
        print(self.encryption_code)
        return self.encryption_code


class PowerOfDecrypt:
    def __init__(self):
        self.powerList = []
        self.user_text = ""
        self.user_key = ""

    def decryption(self, encrypt_data):
        self.powerList = encrypt_data.split("X")
        key_list = self.powerList[-2:]
        user_key = int(key_list[0], 16)
        ram_key = int(key_list[1], 16)
        self.user_key = user_key
        print(self.user_key)
        a = self.powerList[:-2]
        for i in range(len(a)):
            change_dec = int(a[i], 16)  ##############################################################################
            change_ram = change_dec ^ ram_key
            change_sk = change_ram ^ user_key
            # print(chr(change_sk))
            self.user_text += chr(change_sk)
        print(self.user_text)


if __name__ == '__main__':
    myPowerEnc = PowerOfEncrypt()
    myPowerDec = PowerOfDecrypt()
    encrypt: str = myPowerEnc.encryption()
    myPowerDec.decryption(encrypt)
