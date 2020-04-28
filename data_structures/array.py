# list


def array_test():
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(ar)

    # 리스트의 끝에 항목을 더함.
    ar.append(9)
    print(ar)

    # 주어진 위치에 항목을 삽입.
    ar.insert(0, 0)
    print(ar)

    # 같은 값을 가진 첫 번째 항목을 삭제.
    ar.remove(9)
    print(ar)

    # 주어진 위치의 항목을 삭제하고, 그 항목을 리턴.
    # 위치의 값을 주지 않을 경우, 마지막 항목을 삭제하고 돌려줌.
    print(ar.pop())
    print(ar)

    # 항목 중 같은 값인 첫 번째 것의 인덱스를 리턴.
    # 찾는 값, start, end를 인수로 넘기면 start~end 사이의 항목에서 값을 찾음.
    print(ar.index(5))
    try:
        print(ar.index(5, 0, 3))
    except:
        print("Value is not in.")

    # 리스트의 요소들을 뒤집음.
    ar.reverse()
    print(ar)

    # 리스트의 항목들을 정렬함.
    ar.sort()
    print(ar)


def main():
    array_test()


if __name__ == "__main__":
    main()
