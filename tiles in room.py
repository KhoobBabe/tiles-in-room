import math

#the function which finds the number of tiles in a room 
def tiles_in_room(list_of_lists, tile_size):
    
    #initial values are taken as 0
    tot_ar = 0
    tot_til = 0

    
    for i in range(len(list_of_lists)):
        #finding the area of the room
        ar_o_roo = list_of_lists[i][1] * list_of_lists[i][2]

        #finding the number of tiles in that room
        no_o_tiles = math.ceil(ar_o_roo / tile_size)
        
        print("number of tiles in", list_of_lists[i][0], "is", no_o_tiles)

        #adding the number of tiles of a room in its sublist
        list_of_lists[i].append(no_o_tiles)

        #finding the total number of tiles
        tot_til += no_o_tiles

        #finding the total area of all rooms
        tot_ar += ar_o_roo
        
    print()
    print("The total number of required tiles are: ", tot_til)

    #finding the total number of boxes required
    box_req = tot_til/25
    y = math.ceil(box_req)
    print("number of boxes required are: ", y)
    print()

    #finding the remaining tiles
    extr_til = (y*25) - tot_til
    print("Remaining tiles are: ", extr_til)





#CODE STARTS HERE
#we take the total number of rooms  
no_of_rooms = int(input("Enter the number of rooms: "))
print()

#the main is empty like brain
list_of_lists = []


for i in range(no_of_rooms):
    
    #the sublist which contains separate info about every room starts
    room_info = []

    #the name of room is inputted
    room_name = input("Write the name of room: ")
    room_info.append(room_name)
    
    #room's width is added
    room_width = float(input("Enter room's width: "))
    room_info.append(room_width)

    #room's length is entered
    room_length = float(input("Enter room's length: "))
    room_info.append(room_length)
    print()

    #the sublist containg the info about a singke room is added in the main list
    list_of_lists.append(room_info)


#the size of the tile is taken here
tile_size = float(input("Enter the area of a single tile: "))
print()


tiles_in_room(list_of_lists, tile_size)
