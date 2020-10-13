#exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4
# ((9 - (2 * 1)) - 8) + 4 => ((9 - 2) - 8) + 4 => 3

def evaluate_post_fix(exp):
    def helper2(operator, num1, num2):
      if operator == "+":
        return num1 + num2
      elif operator == "-":
        return num2 - num1
      elif operator == "*":
        return num1 * num2
      elif operator == "/":
        return num2 / num1
        
    def helper(exp, stack):
        if not exp:
          if len(stack) == 1:
            return stack
          else:
            while len(stack) > 1:
              val = stack.pop()
              

        val = exp[-1] if len(exp) else stack.pop()
        exp = exp[:-1]

        if val is " ":
            return helper(exp, stack)
        elif val in ["+", "-", "*", "/"]:
            stack.append(val)
        else:
            if not stack[-1].isdigit():
                stack.append(val)
            else:
                digit1 = int(stack.pop())
                operator = stack.pop()

                result = helper2(operator, digit1, int(val))
                stack.append(str(result))

        return helper(exp, stack)
    return helper(exp, [])
