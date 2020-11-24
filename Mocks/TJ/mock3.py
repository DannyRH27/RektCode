'''
Two sorted Linked lists, return as a new sorted linked list
new list should be made by splicing together the nodes of the first two lists.
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
base case is that one is None, return the other
three cases, one is that node1 > node2, node2 > node1, node1 == node2
[1,2,3,4,5] [80,81,82,83,84]
'''
def mergeTwoLists(l1,l2):
  if not l1:
    return l2

  if not l2:
    return l1

  if l1 < l2:
    # starting with l1
    l1.next = self.mergeTwoLists(l1.next,l2)
    return l1
  else:
    l2.next = self.mergeTwoLists(l1,l2.next)
    return l2
  



  

    





