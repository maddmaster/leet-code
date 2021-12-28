from typing import List


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node(data: {}, next: {})".format(self.data, self.next)


def reverse_list(list: List[Node]) -> List[Node]:
    prev = None
    curr = list
    while curr is not None:
        next = curr.next        # save next
        curr.next = prev        # repoint curr.next to prev
        prev = curr
        curr = next

    return prev


def build_list(data: str) -> List[Node]:
    dummy = Node(None)
    head = dummy

    for d in list(data):
        node = Node(d)
        head.next = node
        head = head.next

    return dummy.next


def main():
    list = build_list("ABCD")
    print(list)
    print(reverse_list(list))


if __name__ == '__main__':
    main()