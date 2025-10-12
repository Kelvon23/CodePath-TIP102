"""
U-
I - list of actions
O - returning a list w all the changes
C - 
E - empty list, if list isnt type string,


P- 
High level plan - loop through the given list then we check the given list of instructions and add/delete the element from the stack then 
return what remaining in the stack


I-

def manage_stage_changes(changes):

"""

# def manage_stage_changes(changes):
#     stack =[]
#     removed=None
    

#     for change in changes:
        
#         if change.startswith("Schedule"):
#             stack.append(change[-1])
#         elif change.startswith("Cancel"):
#             if stack:
#                 removed=stack.pop()
                
#         elif change.startswith("Reschedule"):
#             if removed is not None:
#                 stack.append(removed[-1])
#                 removed=None

#     return stack

# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 



"""
U-
Input - a list of tuples that has priorty scale and value
Output - value from input list
Constraints - 
Edge cases - if list is empty, 
P-
High_level plan - loop through the list and append the value depending if priority is greater than next item. potienally needs 2 pointer to check 
I-
"""

# from collections import deque 

# #my solution is wrong as it fails to check to see if the middle is the highest priorty. 
# #fails to check for every case and due to that aaranges them wrong
# def process_performance_requests(requests):
#     queue = deque()
#     left,right = 0,len(requests) - 1

#     while left <= right:
#         if requests[left][0]>=requests[right][0]:
#             queue.appendleft(requests[left][1])
#             left+=1
#         else:
#             queue.appendleft(requests[right][1])
#             right-=1
        
#     return queue

# #Ai solution to the problem 
# def process_performance_requests(requests):
#     # Sort by priority descending; stable sort preserves arrival order
#     sorted_requests = sorted(requests, key=lambda x: x[0], reverse=True)
    
#     # Extract only the performance names into a deque (if a queue is required)
#     queue = deque([name for _, name in sorted_requests])
    
#     return list(queue)  # Convert to list for readable output

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


#Q4 
""" 
U- 
Input - list of values from user
Output- int total from points
Constraints - none
Edge Cases - if empty

P-
High level plan - create a stack that will append each item from list and have a variable that will store the pop item value which will then
be increment with next pop

I-
"""
def collect_festival_points(points):
    stack=[]
    total = 0

    for point in points:
        stack.append(point)
    
    while stack:
        total+=stack.pop()
    
    return total


print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 



"""
Understand-
Input-
Output-
Case-
Edge Cases -
Plan-
High Level Plan -
I-
"""
