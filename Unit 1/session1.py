#Q7
# def main():
#     race_times = [1, 2, 3, 4, 5, 6]
#     threshold = 4
#     result = count_less_than(race_times, threshold)
#     print(result)



# def count_less_than(race_times, threshold):
#     x=0
#     rt_result = [x+=1 for time in race_times if time < threshold  ]
#     return rt_result

# main()

#Q8
# def main():
#     task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
#     print_todo_list(task)

# def print_todo_list(task):
#     for i in range(len(task)):
#         print(f"{i+1}. {task(i)} ")
    

# main()

#Q9
# def main():
#     item_quantities = [2, 4, 6, 8]
#     print(can_pair(item_quantities))


# def can_pair(item_quantities):
#     for item in item_quantities:
#         if item % 2 != 0:
#             return False
#     return True


#Q10
# def main():
#     quantity = 6
#     print(split_haycorns(quantity))


# def split_haycorns(quantity):
#     if quantity <= 0:
#         return None
#     else:
#         result = [i for i in range(1,quantity+1)if quantity % i == 0]
#         return result


# main()

#q11
# def tiggerfy(s):
#     banned_letters = ['t', 'i', 'g', 'e', 'r']
#     result = s                  # start with the whole string
#     for letter in banned_letters:
#         result = result.replace(letter, "")
#         result = result.replace(letter.upper(), "")  # handle uppercase too
#     return result

# def main():
#     print(tiggerfy("suspicerous"))  # suspcous
#     print(tiggerfy("Trigger"))      # 
#     print(tiggerfy("Hunny"))        # Hunny

# main()


#q12

# def main():
#     items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
#     print(locate_thistles(items))

# def locate_thistles(items):
# 	result = [i for i in range(len(items)) if items[i] == "thistle"]
#     return result 



# Advance Q's

#Q1
# def linear_search(items, target):
#     for i in range(len(items)):
#         if target == items[i]:
#             return i
#     return -1

# def main(): 
#     items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
#     target = 'hunny'
#     print(linear_search(items, target))

# main()

#Q2
# def final_value_after_operations(operations):
#     tigger = 1
#     for i in range(len(operations)):
#         op = operations[i].lower()
#         if op == 'bouncy' or op == 'flouncy':
#             tigger += 1
#         elif op == 'trouncy' or op == 'pouncy':
#             tigger -= 1

    
#     return tigger

# def main():
#     # operations = ["trouncy", "flouncy", "flouncy"]
#     # print(final_value_after_operations(operations))
    
#     operations = ["bouncy", "bouncy", "flouncy"]
#     print(final_value_after_operations(operations))


# main()

#Q3

# def tiggerfy(word):
#     word.lower()
#     bad_letter = ["t","i","gg","er"]

    
#     for i in range(len(word)):
#         wd.replace(,"")

        