import re
from stack import Stack

def eval_postfix(expr):
    stack = Stack()
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            stack.push(float(token))
        else:
            if stack.size() < 2:
                raise ValueError("Not enough operands in the expression or invalid expression.")
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.push(num1 + num2)
            elif token == '-':
                stack.push(num1 - num2)
            elif token == '*':
                stack.push(num1 * num2)
            elif token == '/':
                if num2 != 0:
                    stack.push(num1 / num2)
                else:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                    
    if stack.size() != 1:
        raise ValueError("Invalid expression or too many operands.")

    return stack.pop()


def in2post(expr):
    precedence = {'+': 1, '-': 1,
                '*': 2, '/': 2,
                '(': 0, ')': 0}
    stack = Stack()
    postfix = []

    tokens = re.findall(r'\d+|[+\-*/()]', expr.replace(" ", ""))
    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while not stack.is_empty() and precedence[stack.top()] >= precedence[token]:
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)


def main():
    with open('data.txt', 'r') as file:
        for line in file:
            infix_expr = line.strip()
            print(f'infix: {infix_expr}')
            try:
                postfix_expr = in2post(infix_expr)
                if postfix_expr is None:
                    raise ValueError("Invalid input expression encountered.")
                print(f'postfix: {postfix_expr}')
                postfix_result = eval_postfix(postfix_expr)
                print(f'answer: {postfix_result}\n')
            except (ValueError, AttributeError) as e:
                print(f'Error: {e}\n')
                print(f'Please check the input expression: "{infix_expr}"\n')

if __name__ == "__main__":
    main()

