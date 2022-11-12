def first_list(one_list):
    try:
        print("Enter 1st list Elements")
        while True:
            one_list.append(int(input()))
    except:
        print("1st List: ")
        print(one_list)


def second_list(two_list):
    try:
        print("Enter 2nd List Elements")
        while True:
            two_list.append(int(input()))
    except:
        print("2nd List: ")
        print(two_list)


def marge(one_list, two_list, n1, n2, finel_list):
    i = 0
    j = 0
    k = 0

    while (i < n1):
        finel_list[k] = one_list[i]
        k += 1
        i += 1

    while (j < n2):
        finel_list[k] = two_list[j]
        k += 1
        j += 1

    finel_list.sort()


def main():
    one_list = []
    two_list = []
    first_list(one_list)
    second_list(two_list)

    n1 = len(one_list)
    n2 = len(two_list)

    finel_list = [0 for i in range(n1 + n2)]
    marge(one_list, two_list, n1, n2, finel_list)

    print("After Marging List")
    print(finel_list)


main()
