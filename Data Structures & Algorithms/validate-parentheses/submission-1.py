class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ans="[{("
        for x in s:
            if x in "({[":
                stack.append(x)
            else:
                if not stack:
                    return False
                elif x==")" and stack[-1]=="(":
                    stack.pop()
                elif x=="}" and stack[-1]=="{":
                    stack.pop()
                elif x=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        return len(stack)==0