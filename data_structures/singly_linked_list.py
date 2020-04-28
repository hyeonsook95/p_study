class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.before = None
        self.current = None

        self.num_of_data = 0

    # 삽입연산
    # 첫번째 노드에 삽입하는 경우
    # 중간 노드에 삽입하는 경우
    def append(self, pre, data):
        new_node = Node(data)

        if pre == self.head.next:
            new_node.next = pre
            self.head.next = new_node
        else:
            new_node.next = pre.next
            pre.next = new_node

        self.num_of_data += 1

    # 마지막 노드로 삽입하는 경우
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        if self.head.next == None:
            self.head.next = new_node

        self.num_of_data += 1

    # 삭제연산
    def delete(self, pre):
        if self.num_of_data == 0:
            return None

        old = pre.next
        pop_data = old.data

        if old == None:
            return
        pre.next = old.next

        self.num_of_data -= 1

        return pop_data

    def delete(self):
        if self.num_of_data == 0:
            return None

        pop_data = self.current.data

        if self.current == self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data

    # 탐색연산
    def search(self, data):
        tmp = self.head.next
        while tmp != tail:
            if tmp.data == data:
                return tmp
            tmp = tmp.next
        return None

    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.num_of_data == 0:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data


def main():
    linkedList = LinkedList()
    linkedList.append(5)
    linkedList.append(2)
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(7)
    linkedList.append(2)
    linkedList.append(11)

    print("first: ", linkedList.first())  # first: 5
    print("next: ", linkedList.next())  # next: 2
    print("size: ", linkedList.size())  # size: 7
    print("delete: ", linkedList.delete())  # delete: 2
    print("size :", linkedList.size())  # size : 6
    print("current:", linkedList.current.data)  # current: 5
    print("tail:", linkedList.tail.data)  # tail: 11
    print("first :", linkedList.first())  # first : 5
    print("next :", linkedList.next())  # next : 1
    print("next :", linkedList.next())  # next : 2
    print("next :", linkedList.next())


if __name__ == "__main__":
    main()
