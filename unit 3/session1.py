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

# def reverse_comments_queue(comments):
#     stack =[]
#     new_list=[]

#     for item in comments:
#         stack.append(item)
    
#     while stack:
#         new_list.append(stack.pop())
#     return new_list

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


"""
U-
Input- string of characters
Outputs- return a bool if characters are mathcing regarless of punctionation,space and case
Constraints-
Edge Case - if no string given, if not given a string, 
P-
High level plan - to use a 2 pointer that will start opposite sides of string and check each char by char and return false immedliatly
if any missmatch and return true outside of the loop

I

"""

# def is_symmetrical_title(title):
#     if not title:
#         return False
#     new_string=title.lower().replace(" ","")
#     left_pointer = 0
#     right_pointer = len(new_string) - 1
#     print(title)

#     while left_pointer < right_pointer:
#         if new_string[left_pointer] == new_string[right_pointer]:
#             left_pointer+=1
#             right_pointer-=1
#         else:
#             return False
#     return True


# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 


#Q4
# Tasks: 
# Read through the existing solution and add comments so that everyone in your pod understands how it works.
# Modify the solution below to use the two-pointer technique.

# def engagement_boost(engagements):
#     square(engagements[left_pointer] = [] # empty list to store the squared numbs
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i] # here we are squaring the inputs list engagements
#         square(engagements[left_pointer].append((squared_engagement, i))  # storing it into new list 
    
#     square(engagements[left_pointer].sort(reverse=True)  # sort the list to descending order 
    
    
#     result = [0] * len(engagements) # initialize a result list of zeros with same length as input
#     position = len(engagements) - 1 # start filling from the end of the result list
    
#     for square, original_index in square(engagements[left_pointer]:  #loops through the list of square(engagements[left_pointer]
#         result[position] = square  # stored the current squared value into result list
#         position -= 1  # moves one position left in result list


#     
#     left_pointer = 0
#     right_pointer = len(square(engagements[left_pointer]) - 1
#     write = result - 1 

#     while left_pointer <= right_pointer:

#         if square(engagements[left_pointer][left_pointer] >= square(engagements[left_pointer][right_pointer]:
#             result[write]= square(engagements[left_pointer][left_pointer]
#             left_pointer+=1
#         else:
#             result[write]= square(engagements[left_pointer][right_pointer]
#             right_pointer-=1
#         write-=1

    
#     return result

# 2 pointer technique

# def engagement_boost(engagements):
    
#     result = [0] * len(engagements)
#     left_pointer = 0
#     right_pointer = len(engagements) - 1
#     write = len(result) - 1 

#     while left_pointer <= right_pointer:

#         if abs(engagements[left_pointer]) >= abs(engagements[right_pointer]):
#             result[write]= engagements[left_pointer] * engagements[left_pointer]
#             left_pointer+=1
#         else:
#             result[write]= engagements[right_pointer] * engagements[right_pointer]
#             right_pointer-=1
#         write-=1

    
#     return result
    
    
# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))


#Q5