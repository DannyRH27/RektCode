def findKthMax(root, k):
    # Write your code here
    if not root:
        return None
    stack = [root]
    count = 0
    while len(stack):
        count += 1
        current = stack.pop()
        if current.leftChild:
            stack.append(current.leftChild)
        if current.rightChild:
            stack.append(current.rightChild)

    second_count = 0
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.leftChild
        elif stack:
            current = stack.pop()
            if second_count == count - k:
                return current.val
            second_count += 1
            current = current.rightChild
        else:
            break
    return second_count
