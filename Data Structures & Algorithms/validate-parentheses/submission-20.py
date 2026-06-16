class Solution:
    def isValid(self, s: str) -> bool:
        pushArray = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                pushArray.append(s[i])
                print(pushArray)
            if (s[i] == ")" or s[i] == "}" or s[i] == "]"):
                if not pushArray:
                    return False
                if pushArray[-1] == "(" and s[i] == ")" and pushArray:
                    pushArray.pop()
                    print(pushArray)
                elif pushArray[-1] == "{" and s[i] == "}":
                    pushArray.pop()
                    print(pushArray)
                elif pushArray[-1] == "[" and s[i] == "]":
                    pushArray.pop()
                    print(pushArray)
                else:
                    return False
        return len(pushArray) == 0
        