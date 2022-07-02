from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwo(self, l1, l2, carry):
        result = carry
        if l1 is not None:
            result += l1.val
            l1 = l1.next
        if l2 is not None:
            result += l2.val
            l2 = l2.next
        if result >= 10:
            result = result - 10
            carry = 1
        else:
            carry = 0
        if (l1 is None and l2 is None and carry == 0):
            return ListNode(result)
        else:
            return ListNode(result, self.addTwo(l1, l2, carry))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwo(l1,l2,0)

def getLinkedList(l: List, i: int):
    if i == len(l) - 1:
        return ListNode(l[i])
    else:
        return ListNode(l[i], getLinkedList(l, i+1))

if __name__ == '__main__':
    l1 = getLinkedList([2,4,3], 0)
    l2 = getLinkedList([5,6,4], 0)
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    curr = res
    while curr is not None:
        print(curr.val)
        curr = curr.next