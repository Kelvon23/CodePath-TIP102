#Q1
#Understand 
#I - inputs are list of artisits and set times 
#O - return a dictonary that hold key value pair between previous inputs 
#C
#E - if list is empty and if list does not have same len 
#P 
#Big idea - I will have 2 lists as inputs and then use dict to store a key using value from artists and have the value match set times 
#Steps:
# def lineup(list1,list2)
# dic ={}
# for art from artist:
#   if art not in dic:
#       dic[art]
#   else:
        dic[art]

# solves it but some areas to improve 
def lineup(artists, set_times):
    dic={}
    for art in range(len(artists)):   
        if art not in dic:  #redundant no point as it will always be true and not need
            dic[artists[art]]=set_times[art] # only is this needed
    if not dic: # not needed as no matter what dic will return an empty dict 
        return dic
    return dic


#Q2
# string artist name that will be searched for and dictonary that has all the revelant info.
# return the value if artisit appear but return a error message if dont appear 
# return dict no matter 


def get_artist_info(artist, festival_schedule):
    result = festival_schedule.get(artist,'message': 'Artist not found')
    dic={}
    if artist in festival_schedule:
         return result
    else:
        dic["message"] = "Artist not found" # dic and this wasnt need apparently & couldve simply explicty return a dict 
        return dic # return {"message": "Artist not found"}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
    

#Q3
def total_sales(ticket_sales):
    total=0
    for sale in ticket_sales.values():
        total+=sale
    
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales),end="")

#Q4
