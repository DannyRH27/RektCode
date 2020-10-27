def findAncestors(root, k):
    # Write your code here
    if not root:
        return None
    current = root
    ancestors = []

    while current:
        ancestors.append(current.val)
        if current.val > k:
            current = current.leftChild
        if current.val < k:
            current = current.rightChild
        else:
            return ancestors[::-1]

    return None
