'''

class Node:
  self.prev
  self.next
  self.child


flatten doubly linked list
each node will potentially have a child

return original head

1 => 2 => 8
      => 3 => 4 => 7 =>
              => 5 => 6 

1,2,3,4,5,6,7,8

traverse through the list, basically if there's no child, don't do anything

if there is a child, i need to keep track of next by appending to stack and assign child as next 
while removing child pointer
go through child next, and stuff.

stack
[8, 7]
pop 7 =>
pop 8 => 



1 => 2 => 8
      => 3 => 4 => 7 =>
              => 5 => 6 

1,2,3,4,5,6,7,8
'''

def flatten(head):
  node = head
  stack = []

  while node:
    if not node.child:
      if not node.next:
        if not len(stack):
          return head
        temp = stack.pop()
        node.next = temp
        temp.prev = node
      node = node.next
      continue
      
    if node.next:
      stack.append(node.next)
    
    temp = node.child
    temp.prev = node
    node.child = None
    node.next = temp
    node = node.next
    





    




