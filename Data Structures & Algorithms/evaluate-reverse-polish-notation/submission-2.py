class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
            stack = []

            for n in tokens:
            # if n in "+,-,*,/": WRONG, don't need commas
                if n in "+-*/":
                        op_one = stack.pop()
                        op_two = stack.pop()
                        if n == '+':
                            res = op_two + op_one
                            stack.append(res)
                        elif n == '-':
                            res = op_two - op_one
                            stack.append(res)
                        elif n == '*':
                            res = op_two * op_one
                            stack.append(res)
                        elif n == '/':
                            res = int(op_two / op_one)
                            stack.append(res)

                    # res = op_one + n + op_two WRONG, this is string concat
                # stack.push(n) WRONG, no push(), use append()
                else:
                    stack.append(int(n))
            return stack[0]
        