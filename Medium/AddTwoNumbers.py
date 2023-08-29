
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l3:ListNode = ListNode(l1.val + l2.val)
    carry = 0
    import math
    while l1.next or l2.next:

        x = l1.next if l1.next != None else 0
        y = l2.next if l2.next != None else 0

        if l3 == None:
            l3 = ListNode((x + y + carry) % 10)
        else:
            temp = ListNode((x + y + carry) % 10)
            l3.next = temp
            l3 = temp

        carry = math.floor((x + y + carry) / 10)

    l3.next = (carry)
    return l3


l1 = [9,9,9,9,9,9,9]

l2 = [9,9,9,9]

print(addTwoNumbers(l1,l2))        
        