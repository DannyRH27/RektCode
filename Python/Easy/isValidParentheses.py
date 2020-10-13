def is_balanced(exp):
    stack = []
    closing = "}])"

    for char in exp:
        if len(stack):
            if char == "}" and stack.pop() != "{":
                return False
            if char == ")" and stack.pop() != "(":
                return False
            if char == "]" and stack.pop() != "[":
                return False

        if char not in closing:
            stack.append(char)

    if not len(stack):
        return True

    return False
