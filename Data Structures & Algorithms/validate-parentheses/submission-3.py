class Solution:
    def isValid(self, s: str) -> bool:

        # define stack
        stack = []

        dic = {
            '}' : '{',
            ']' : '[',
            ')' : '('  
        }

        for char in s:
            if char in dic.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()

        return len(stack) == 0