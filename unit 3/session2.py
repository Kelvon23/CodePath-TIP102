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

def manage_stage_changes(changes):
    stack =[]
    removed=None
    

    for change in changes:
        
        if change.startswith("Schedule"):
            stack.append(change[-1])
        elif change.startswith("Cancel"):
            if stack:
                removed=stack.pop()
                
        elif change.startswith("Reschedule"):
            if removed is not None:
                stack.append(removed[-1])
                removed=None

    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 



# from collections import deque 


# def process_performance_requests(requests):
#     queue = deqeue()

#     for request in requests:
