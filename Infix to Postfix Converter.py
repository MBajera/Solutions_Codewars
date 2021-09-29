def to_postfix(infix):
    stack = []
    output = []
    for dig in infix:
        if dig in "0123456789":
            output.append(dig)
        elif dig in "+-":
            while (stack[-1] in "*/^+-") if stack else stack:
                output.append(stack.pop(-1))
            stack.append(dig)
        elif dig in "*/":
            while (stack[-1] in "*/^") if stack else stack:
                output.append(stack.pop(-1))
            stack.append(dig)
        elif dig in "^":
            stack.append(dig)
        elif dig in "(":
            stack.append(dig)
        elif dig in ")":
            for i in range(len(stack)):
                if stack[-1] in "(":
                    stack.pop(-1)
                    break
                output.append(stack.pop(-1))
    output.extend(stack[::-1])
    return "".join(output)
