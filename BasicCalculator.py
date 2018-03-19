# How to evaluate infix notation with parenthesis? (basic calculator)

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23


# Keep a global running total and a stack of signs (+1 or -1), one for each open scope.
# The “global” outermost sign is +1.
#
# Each number consumes a sign.
# Each + and - causes a new sign.
# Each ( duplicates the current sign so it can be used for the first term inside the new scope.
# That’s also why I start with [1, 1] - the global sign 1 and a duplicate to be used for the first term,
# since expressions start like 3... or (..., not like +3... or +(....
# Each ) closes the current scope and thus drops the current sign.


def calculate(self, s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'],
        elif c == ')':
            signs.pop()
        i += 1
    return total

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
    # The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5


#use stack
def calculate_2(self, s):
    if not s:
        return "0"
    stack, num, sign = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i])-ord("0")
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0
    return sum(stack)