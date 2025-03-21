"""Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data does not 
contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105."""

#Basically we are removing and saving it with a stack as we go deeper

def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []; cnum = 0; cst = ''
    for v in s:
        if v == "[":
            stack.append((cnum, cst))
            cst = ""
            cnum = 0
        elif v == "]":
            x = stack.pop()
            cst = x[1]+(x[0]*cst) 
            cnum = 0
        elif v.isdigit():
            cnum = cnum*10 + int(v)
        else:
            cst += v
    #print(mutiplicities, stack, letters, string, tempstring)    
    return cst
#