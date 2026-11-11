class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char == "(":
                stack.append("(")
            elif char == "{":
                stack.append("{")
            elif char == "[":
                stack.append("[")
            else:
                if not stack:
                    return False
                if stack and char == "]" and stack[-1] != "[":
                    break
                elif stack and char == "}" and stack[-1] != "{":
                    break
                elif stack and char == ")" and stack[-1] != "(":
                    break
                else:
                    if stack:
                        stack.pop()
                    else:
                        break
                
        
        if not stack:
            return True
        else:
            return False

        