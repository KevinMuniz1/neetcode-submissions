class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False 

        stack = []


        for symbol in s:

            if symbol == "[" or symbol == "(" or symbol == "{":

                stack.append(symbol)
            
            else:

                if stack:
                    value = stack.pop()

                    if value == "{" and symbol != "}":
                        return False
                    
                    if value == "(" and symbol != ")":
                        return False
                    
                    if value == "[" and symbol != "]":
                        return False
                else:
                    return False
            
        if not stack:
            return True
        else:
            return False

                



            



        