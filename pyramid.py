# Today I try to build pyramid !!!


def build_pyramid():
    for i in range(5):
        for j in range(i + 1):
            print("* ", end="")
        print()


def build_pyramid_two():
    rows = int(input("Enter number of rows: "))

    k = 0

    for i in range(1, rows + 1):  # i=0
        for j in range(1, (rows - i) + 1):  # j = 0
            print(end="  ")

        while k != (2 * i - 1):  # k က -1 နဲ့မညီဘူး
            print("* ", end="")
            k += 1

        k = 0
        print()


if __name__ == '__main__':
    # build_pyramid()
    build_pyramid_two()
