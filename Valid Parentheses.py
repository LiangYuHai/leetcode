# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        print(s)
        stack=[]
        for bracket in s:
            if (bracket is '[') or (bracket is '{') or (bracket is '('):
                stack.append(bracket)
            if bracket is ']':
                if stack[-1] is '[':
                    stack.pop()
                else:
                    return False
            if bracket is ')':
                if stack[-1] is '(':
                    stack.pop()
                else:
                    return False
            if bracket is '}':
                if stack[-1] is '{':
                    stack.pop()
                else:
                    return False
        if len(stack)== 0:
            return True
        else:
            return False

solution=Solution()
print(solution.isValid("(]"))