"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Note that the operation cannot be performed on a digit that does not have any non-digit character to its left."""
def clearDigits(s):

    news = ""
    for c in s:
        if c.isdigit():
            news= news[:-1]
        else:
            news = news+c
    return news
        
#Arguably you should use a stack, popping each time, although this is about the same