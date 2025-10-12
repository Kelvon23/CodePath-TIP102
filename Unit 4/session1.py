# def extract_nft_names(nft_collection):
#     nft_name=[]

#     for nft in nft_collection:
#         if nft.get("name") is not None:
#             nft_name.append(nft["name"])
#     return nft_name



# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))



# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names.append(nft["name"])
#     return nft_names

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]
# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# nft_collection_3 =[]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))


"""
U-
I- a list of nfts 
O- return a list of only most popular creators
C-
E- if creator key doesnt exist in dict, empty list

P-
High-level plan - create a new dict which will store key creators name and value being counter
Then iterate through the list and store the creator name in our new dict if it our first time then assign += 1
every other time we see him in the list. After we will loop through new dict and find which has highest counter out of everyone
then return that list.
I-
"""

# def identify_popular_creators(nft_collection):
#     creator_counter={}

#     for nft in nft_collection:
#         if nft["creator"] not in creator_counter:
#             creator_counter[nft["creator"]]=1
#         else:
#             creator_counter[nft["creator"]]+=1

#     highest=1
#     name = None

#     for creator,count in creator_counter.items():
#         if count > highest:
#             highest= count
#             name = creator

#     if not name:
#         return []
#     else:
#         return [name]

# nft_collection=[
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2=[
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]

# nft_collection_3=[
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

        
        
        
"""
Understand-
Input- a list of dict with info about nfts
Output- return a int of average value of all nfts from the list
Case-
Edge Cases - if list empty, if key dont exist
Plan-
High Level Plan - iterate through the list and have total var that will store values from list then divide based on len of list
return the avg var 
I-
"""

# def average_nft_value(nft_collection):
#     if not nft_collection:
#         return 0
    
#     total = 0
#     for nft in nft_collection:
#         total+=nft.get("value",0)

#     avg=total/len(nft_collection)

#     return avg

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]

# nft_collection_3 = []

# # checks if value in key value pair is int/float data type & proper implementation of avg 
# def average_nft_value(nft_collection):
#     total = 0.0
#     count = 0

#     for nft in nft_collection:
#         if "value" in nft and isinstance(nft["value"], (int, float)):
#             total += nft["value"]
#             count += 1

#     if count == 0:
#         return 0.0
#     return total / count


# print(average_nft_value(nft_collection))
# print(average_nft_value(nft_collection_2))
# print(average_nft_value(nft_collection_3))


