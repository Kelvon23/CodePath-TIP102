"""
Understand
I - string 
O - Boolean 
C - 
E - {[]} 

P- High level - looping through each char in the string and if each char is approiate or not
push the opening tag and if there is a clsoing tag then pop the opening tag then if empty return true and if not then false



I


"""

# def is_valid_post_format(posts):
#     stack=[]
#     # types=["{","}","[","]","(",")"]
#     types = {"[":"]","{":"}","(":")"}

#     for char in posts:
#         if char in types.keys():
#             stack.append(char)
#         elif char in types.values():
#             if not stack or char != types[stack[-1]]:
#                 return False
#             stack.pop()
#     # if not stack:
#     #     return True 
#     return not stack



# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

#Q2
"""
U-
I - a list of words
O - a list with reversed order of words
C
E- empty list,
P- Highlevel - loop through the list and append it into stack then pop it and save it into a new list 

I-



"""

def reverse_comments_queue(comments):
    stack =[]
    new_list=[]

    for item in comments:
        stack.append(item)
    
    while stack:
        new_list.append(stack.pop())
    return new_list

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))