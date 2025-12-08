# Jaiden Blanchard
# CS 499 Capstone with Professor Sherri Maciosek
# started 11 / 10 / 2025, first submission 11 / 15 / 2025, polished 12 / 8 /2025

from PaintNeeded import PaintNeeded

# list to hold wall_width variables
wall_list = []
window_list = []
door_list = []

#**********************************************************
# This section is meant to receive the number of walls the
# user will paint.
#**********************************************************

while True:
    try: # ask for number of walls
        wall_count = int(input("How many walls do you wish to paint? "))
        # positive whole numbers only
        if wall_count <= 0:
            print("Invalid entry. Enter a positive value.")
            continue
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue
    break

#**********************************************************
# Recieve individiual wall inputs and one room height 
# input. 
#**********************************************************

for wall in range(wall_count):
    while True:
        try:
            wall_width = int(input(f"Enter the width of your wall #{wall+1} (feet): "))
            # positive whole numbers only
            if wall_width <= 0:
                print("Error: wall width cannot be zero or less")
                continue
            else: # valid entry? add it to the list
                wall_list.append(wall_width)
        except ValueError:
            print("Invalid entry. Enter a numerical value.")
            continue
        break
# get the height of the room
while True:
    try: # only run if there is a wall width of a positive whole number
        if wall_width > 0:
            wall_height = int(input("Enter the height of your wall (feet): "))
            # positive whole numbers only
            if wall_height <= 0:
                print("Error: wall height cannot be zero or less")
                continue
            break
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue

#**********************************************************
# Ask about the existence of windows
# if yes, the user will input an individual width for each window
# and one overall height input
# if no, skip this section
#**********************************************************

while True:
    try: # determine if the user has windows in their room
        windows_yn = input("Are their windows in your room? [Y/N] ")
        # if lowercase input is received, convert it to uppercase
        if windows_yn == windows_yn.lower():
            windows_yn = windows_yn.upper()
        # if yes, get the number
        if windows_yn == "Y":
            try:  # ask for number of windows
                window_count = int(input("How many windows are in your room? "))
                # positive whole numbers only
                if window_count <= 0:
                    print("Invalid entry. Enter a positive value.")
                    continue
                for window in range(window_count):
                    while True:
                        try:
                            window_width = int(input(f"Enter the width of your window #{window + 1} (feet): "))
                            # positive whole numbers only
                            if window_width <= 0:
                                print("Error: window width cannot be zero or less")
                                continue
                            # window widths must be smaller than or equal to wall widths
                            if window_width > wall_width:
                                print("Error: window width cannot exceed wall width")
                                continue
                            else:  # valid entry? add it to the list
                                window_list.append(window_width)
                        except ValueError:
                            print("Invalid entry. Enter a numerical value.")
                            continue
                        break
                # get the height of the windows
                while True:
                    try: # only run if there is a window width of a positive whole number
                        if window_width > 0:
                            # receive the height input
                            window_height = int(input("Enter the height of your window(s) (feet): "))
                            # positive whole numbers only
                            if window_height <= 0:
                                print("Error: window height cannot be zero or less")
                                continue
                            # window heights must be smaller than or equal to wall heights
                            if window_height > wall_height:
                                print("Error: window height cannot exceed wall height")
                                continue
                            break
                    except ValueError:
                        print("Invalid entry. Enter a numerical value.")
                        continue
            except ValueError:
                print("Invalid entry. Enter a numerical value.")
                continue
            break
        # No windows, move to next section
        if windows_yn == "N":
            window_count = 0
            break
        else:
            print("Error: Invalid input. Please type 'Y' or 'N' ")
            continue
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue

#**********************************************************
# Ask about the existence of doors
# if yes, the user will input an individual width for each door
# and one overall height input
# if no, skip this section
#**********************************************************

while True:
    try: # determine if the user has doors in their room
        doors_yn = input("Are their doors in your room? [Y/N] ")
        # if lowercase input is received, convert it to uppercase
        if doors_yn == doors_yn.lower():
            doors_yn = doors_yn.upper()
        # if yes, get the number
        if doors_yn == "Y":
            try: # ask for number of doors
                door_count = int(input("How many doors are in your room? "))
                # positive whole numbers only
                if door_count <= 0:
                    print("Invalid entry. Enter a positive value.")
                    continue
                for door in range(door_count):
                    while True:
                        try:
                            door_width = int(input(f"Enter the width of your door #{door + 1} (feet): "))
                            # positive whole numbers only
                            if door_width <= 0:
                                print("Error: door width cannot be zero or less")
                                continue
                            # door widths must be smaller than or equal to wall widths
                            if door_width > wall_width:
                                print("Error: door width cannot exceed wall width")
                                continue
                            else: # valid entry? add it to the list
                                door_list.append(door_width)
                        except ValueError:
                            print("Invalid entry. Enter a numerical value.")
                            continue
                        break
                # get the height of the door(s)
                while True: # only run if there is a door width of a positive whole number
                    try:
                        if door_width > 0:
                            # receive the height input
                            door_height = int(input("Enter the height of your door(s) (feet): "))
                            # positive whole numbers only
                            if door_height <= 0:
                                print("Error: door height cannot be zero or less")
                                continue
                            # door heights must be smaller than or equal to wall heights
                            if door_height > wall_height:
                                print("Error: door height cannot exceed wall height")
                                continue
                            break
                    except ValueError:
                        print("Invalid entry. Enter a numerical value.")
                        continue
            except ValueError:
                print("Invalid entry. Enter a numerical value.")
                continue
            break
        # no doors, move to next section
        if doors_yn == "N":
            door_count = 0
            break
        else:
            print("Error: Invalid input. Please type 'Y' or 'N' ")
            continue
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue

#**********************************************************
# ask if the user will be painting their ceiling.
# if yes, recieve the width and length
# if no, move to next section
#**********************************************************

while True:
    try: # determine if the user is painting their ceiling
        ceiling_yn = input("Will you be painting your ceiling? [Y/N] ")
        # if lowercase input is received, convert it to uppercase
        if ceiling_yn == ceiling_yn.lower():
            ceiling_yn = ceiling_yn.upper()
        # if yes, get the number
        if ceiling_yn == "Y":
            ceiling_length = int(input("Enter the length of your ceiling (feet): "))
            # positive whole numbers only
            if ceiling_length <= 0:
                print("Invalid entry. Enter a positive value.")
                continue
            ceiling_width = int(input("Enter the width of your ceiling (feet): "))
            # positive whole numbers only
            if ceiling_width <= 0:
                print("Invalid entry. Enter a positive value.")
                continue
            break
        # not paiting the ceiling, move to next section
        if ceiling_yn == "N":
            break
        else:
            print("Error: Invalid input. Please type 'Y' or 'N' ")
            continue
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue

#**********************************************************
# Ask the user how many coats they will apply.
# the total paintable area is multiplied by the number
# of coats input
#**********************************************************

while True:
    try:
        coat_count = int(input("How many coats will you apply? "))
        # positive whole numbers only
        if coat_count <= 0:
            print("Error: coat count cannot be zero or less")
            continue
        break
    except ValueError:
        print("Invalid entry. Enter a numerical value.")
        continue

#**********************************************************
# Calculate the total area for the walls, windows, doors,
# and ceiling, mulltiplied by coat count, and divide by 
# sq ft per gallon, and recieve the final output
#**********************************************************

# the sum of every wall weidth multiplied by the wall height
total_wall_area = sum(wall_list) * wall_height

# the area of the ceiling, only calculated if user answered "Y" to ceiling
total_ceiling_area = 0
if ceiling_yn == "Y":
    total_ceiling_area = ceiling_length * ceiling_width

# the area of the windows, only calculated if user answered "Y" to windows
total_window_area = 0
if windows_yn == "Y":
    total_window_area = sum(window_list) * window_height
    if total_window_area > total_wall_area:
        print("Window area is larger than wall area. You may want to consider recalculating.")
        

# the area of the doors, only calculated if user answered "Y" to doors
total_door_area = 0
if doors_yn == "Y":
    total_door_area = sum(door_list) * door_height
    if total_door_area > total_wall_area:
        print("Door area is larger than wall area. You may want to consider recalculating.")

total_area = total_wall_area + total_ceiling_area - total_window_area - total_door_area
total_area = max(0, total_area)  # to prevent negative area results

paint = PaintNeeded(1, total_area, coat_count)
total = paint.gallons_paint()

print(f"{total_area:.2f} square ft")

# just for looks, print "gallon(s)" if the total is different from 1
if total == 1:
    print(f"Paint needed: {total:.2f} gallon")
else:
    print(f"Paint needed: {total:.2f} gallons")
