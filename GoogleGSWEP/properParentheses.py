#Given an input string s consisting solely of the characters 
# '(', ')', ', ', '[' and ']', determine whether s is a valid string.
#  A string is considered valid if every opening bracket is closed 
# by a matching type of bracket and in the correct order, and every 
# closing bracket has a corresponding opening bracket of the same type.

def properParentheses(s):
    brackets = {
        "{":"}",
        "[":"]",
        "(":")",
    }
    stack = []
    for bracket in s:
        #If it is right we will place on stack
        if bracket in brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            rightbracket = stack.pop()
            if brackets[rightbracket]!= bracket:
                return False
    return len(stack) == 0

print(properParentheses("{(){}()}"))
