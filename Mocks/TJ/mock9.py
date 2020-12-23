'''
moderating a race
get certain info back in the middle of the race
top k runners at any given time

whenever a runner passes a mile marker, we have their unique ID and the mile marker
start at mile marker 0
1 (ID, 1)
1,2,3,4,5

5,5,4,3,2,1
easy access to update ID's progress
have an easy way to sort and keep track of who is top k
it would be easy to just take the top k from this structure

14 ppl who have passed mile marker 3



(4,1,unique ID)


heap =  

sort by mile marker

outer hash will constantly point at the ids

{
  1: {
    name: Bob
    mile: 2
    relative: 2
    heap_idx: 
  },
  2: {
    name: Jay
    mile: 2
    relative: 3,
    heap_idx: 2
  }
}

[]

switch it with the bottom, pop, edit, and then sift it back down
Understand better how the actual swapping works beyond runtime

final runtime is 2 * k * log(n) = popping, shuffling, putting it back in

heap = [1,2]

hash = {
  1 => Node(Jay prev = None next = TJ )
  2 => Node(Danny prev = None next = None)
  3 => Node(TJ)
}

{
  0: Node(Jay) => Node(TJ)
  1: Node(Danny)
}

O(n) to create nodes
O(1) to update nodes
O(k) to check top k


'''