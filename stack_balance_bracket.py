
def valid_parent(l,r):
    if l == '[' and r == ']':
        return True
    elif l == '{' and r == '}':
        return True
    elif l == '(' and r == ')':
        return True


def is_matched(expression):
    m = []
    for i in range(len(expression)):
        if expression[i] == '(' or expression[i] == '{' or expression[i] == '[':
            m.append(expression[i])
        else:

            if m and valid_parent(m[len(m)-1],expression[i]):
                m.pop()
            else:
                return False
    if len(m) >= 1:
        return False
    else:
        return True





t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
