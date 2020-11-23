'''
ITERATIVE
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    while head:
      temp = head.next
      head.next = prev
      prev = head
      head = temp

    return prev
'''


def reverseList(self, head: ListNode) -> ListNode:

  def swap(node):
    if not node or not node.next:
      return node
    second = node.next
    reverse = swap(second)
    second.next = node
    node.next = None
    return reverse

  return swap(head)
