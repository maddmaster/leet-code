from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "Node(val: {}, next: {})".format(self.val, self.next)

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        dummy = ListNode(None)
        headm = dummy

        while head1 is not None or head2 is not None:
            while head1 is not None and head2 is not None and head1.val <= head2.val:
                headm.next = ListNode(head1.val)
                headm = headm.next
                head1 = head1.next

            while head1 is not None and head2 is not None and head2.val <= head1.val:
                headm.next = ListNode(head2.val)
                headm = headm.next
                head2 = head2.next

            while head1 is not None and head2 is None:
                headm.next = ListNode(head1.val)
                headm = headm.next
                head1 = head1.next

            while head2 is not None and head1 is None:
                headm.next = ListNode(head2.val)
                headm = headm.next
                head2 = head2.next

        return dummy.next


def build_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    else:
        dummy = ListNode(None)
        head = dummy
        for val in values:
            node = ListNode(val)
            head.next = node
            head = head.next

        return dummy.next

if __name__ == '__main__':
    list1 = build_list([1])
    list2 = build_list([2])

    solution = Solution()
    print(solution.merge_two_lists(list1, list2))