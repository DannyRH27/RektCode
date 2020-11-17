# the first thing is the root node of 10
# I want to build a binary search tree on another computer
# I will traverse through DFS and this will first lead to the path that has the lowest number
# How do i form the string as I traverse through the tree on my computer
'''
       10
     /   \
    8     12
  /  \   /  \
 5    9 11   15
'''

# tuple with first value being the parent node, and an arr of length 2 being the child nodes
# As I hit a parent node, I will create a tuple of (10, [8,12]), i'll put None in the array
# Just separate by - to demarcate one node and next node.
# O(V + E)
# node has left, right, value


def sendBST(root):
  stack = []
  stack.append(root)

  res = ''
  while stack:
    
    current = stack.pop()
    edges = [current.value]
    if current.left:
      edges.append(left.value)
      stack.append(current.left)
    else:
      edges.append(None)
    if current.right:
      edges.append(right.value)
      stack.append(current.right)
    else:
      edges.append(None)

    if len(res) == 0:
      res += str(edges)
    else:
      res += ("-" + str(edges))
  return root
# I know the first node is the root node
# current is root, set pointers, then i take the child node
# convert tuple arr into dictionary
# as i traverse through, lookup edges and connect, then append to stack current.left and current.right
def recBST(string):
  nodes = string.split("-")
  my_dict = {}
  for str_tup in nodes:
    "10, 5, 12"


    node_info = str_tup[1:-1]
    node_arr = node_info.split(",")
    parent_val = int(node_arr[0])
    left_val = int(node_arr[1])
    right_val = int(node_arr[2])

    my_dict[parent_val] = [left_val, right_val]
    

  root = Node(nodes[0][0])

  stack = []
  stack.append(root)

  while stack:
    current = stack.pop()

    edges = my_dict[current.val]
    left, right = None, None
    if edges[0]:
      left = Node(edges[0])
      current.left = left
      stack.append(left)
    if edges[1]:
      right = Node(edges[1])
      current.right = right
      stack.append(right)
  
  return root
    

    

  


