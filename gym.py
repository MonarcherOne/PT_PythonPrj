import tkinter
from tkinter import ttk

# Gym tracker
# user input their names,and gender, ay least 3 days;
# specific, how many kilometres did you run, how many reps in total, how heavy for each rep,
# output: the current rank, leaderboard

# Daily calculation formula for the ranking: 
# Everybody starts at (0 points), first 10 km runner will get 500 points per 1 km, 
# after 10 km, will get 1000 points per km
# for weightlifting in total weight: 1st 100 kg get 5 points per 1 kg, after will get 8 points per 1 kg.
# after calculation if female, will be multiplied by 1.5x.

# Data correction: distance will be between 0 and 50, reps will be between 0 and 100, weight will be between 0 and 150.
# If all values are 0, skip the calculation for that day.

# After calcutated, will get the daily average points for each user(all divide by # of day inputted by user), then multiply by 30(monthly), and the winner will be the one with the most monthly points.

# Ranking system:
# Bronze rank is from 0-200,000 points,
# Silver is from 200,001 to 1,000,000
# Diamond is > 1,000,000


# calculate point for 1 day
def gym_calculate_daily (distance, reps, weight):
    point = 0
    if distance <= 10:
        point = point + (distance * 500)
    else:
        point = point + (10 * 500) + ((distance - 10) * 1000)

    totalWeight = reps * weight
    
    if totalWeight <=100: 
        point = point + (totalWeight * 5)
    else:
        point = point + (100 * 5) + ((totalWeight - 100)* 8)
    
    return point


# calculate point for 1 user
def gym_calculate (user):
    # user structure: ('Name', 'Gender', [ [day1_kmsRunning, day1_repsNumber, day1_liftWeightEachRep], [day2..], [day3..], ... ])

    gender = user[1]

    point = 0
    dayCount = 0

    for day in user[2]:
        distance = float(day[0])
        reps = int(round(float(day[1])))
        weight = float(day[2])

        # do some data correction/refining here:
        if distance < 0:
            distance = 0
        elif distance > 50:
            distance = 50

        if reps < 0:
            reps = 0
        elif reps > 100:
            reps = 100

        if weight < 0:
            weight = 0
        elif weight > 150:
            weight = 150

        # skip if all values are 0
        if distance == 0 and reps == 0 and weight == 0:
            #continue command meaning skip this day and go back to the for and calculate for the next day
            continue
        
        #if all values are valid(user has at least inputted something)then daycount will be added 1. If not, continue above and not add the day count.
        dayCount += 1
        

        point += gym_calculate_daily(distance, reps, weight)
    
    if gender == "Female":
        point = point * 1.5

    return point / dayCount * 30


# get the ranking of the user based on the points
def get_ranking (point):
    if point < 200000:
        return "Bronze"
    elif point < 1000000:
        return "Silver"
    else:
        return "Diamond"
    
# show the result of all users
def show_result (user_list):
    max_user = ""
    max_point = 0
    result_text = ""
    
    for user in user_list:
        # Calculate the points for each user
        point = gym_calculate(user)

        if point > max_point:
            max_point = point
            max_user = user[0]

        rank = get_ranking(point)

        result_text += f"{user[0]}: {point:,.2f} points, Rank: {rank}\n"

    result_text += f"\nThe winner is: {max_user} with {max_point:,.2f} points"

    return result_text


# testing:
list_users = [('Mary','Female',[[10.5678, 20, 47.1234], [5, 10, 20]]),('Tom','Male',[[15, 40, 30], [19, 40, 50], [21, 50, 100], [0, 0, 0]])]
print(show_result(list_users))


# comment below line for UI running:
#exit()


# UI Part
class ChildWindow:
    def __init__(self, parent):
        # create child window gadget
        self.child_window = tkinter.Toplevel(parent)
        self.child_window.geometry("800x400")
        self.child_window.title("User Information")

        # Center the child window in the top vertical center of the parent window
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        child_width = 800
        child_height = 400
        x = parent_x + (parent_width // 2) - (child_width // 2)
        y = parent_y + 50  # Adjust the vertical offset to position near the top
        self.child_window.geometry(f"{child_width}x{child_height}+{x}+{y}")

        # Add labels and inputs to the child window
        self.label1 = tkinter.Label(self.child_window, text="Name:")
        self.label1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry1 = tkinter.Entry(self.child_window)
        self.entry1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = tkinter.Label(self.child_window, text="Gender:")
        self.label2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.combobox2 = tkinter.ttk.Combobox(self.child_window, values=["Male", "Female", "Other"])
        self.combobox2.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = tkinter.Label(self.child_window, text="Distance:")
        self.label3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.spinbox3 = tkinter.Spinbox(self.child_window, from_=0, to=100)
        self.spinbox3.grid(row=3, column=1, padx=10, pady=5)
        self.label3_unit= tkinter.Label(self.child_window, text="KM")
        self.label3_unit.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.spinbox3_2 = tkinter.Spinbox(self.child_window, from_=0, to=100)
        self.spinbox3_2.grid(row=3, column=3, padx=10, pady=5)
        self.label3_2unit= tkinter.Label(self.child_window, text="KM")
        self.label3_2unit.grid(row=3, column=4, padx=10, pady=5, sticky="w")
        
        self.spinbox3_3 = tkinter.Spinbox(self.child_window, from_=0, to=100)
        self.spinbox3_3.grid(row=3, column=5, padx=10, pady=5)
        self.label3_3unit= tkinter.Label(self.child_window, text="KM")
        self.label3_3unit.grid(row=3, column=6, padx=10, pady=5, sticky="w")


        self.label4 = tkinter.Label(self.child_window, text="Reps:")
        self.label4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.spinbox4 = tkinter.Spinbox(self.child_window, from_=0, to=200)
        self.spinbox4.grid(row=4, column=1, padx=10, pady=5)
        self.label4_unit= tkinter.Label(self.child_window, text="times")
        self.label4_unit.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.spinbox4_2 = tkinter.Spinbox(self.child_window, from_=0, to=200)
        self.spinbox4_2.grid(row=4, column=3, padx=10, pady=5)
        self.label4_2unit= tkinter.Label(self.child_window, text="times")
        self.label4_2unit.grid(row=4, column=4, padx=10, pady=5, sticky="w")
        

        self.spinbox4_3 = tkinter.Spinbox(self.child_window, from_=0, to=200)
        self.spinbox4_3.grid(row=4, column=5, padx=10, pady=5)
        self.label4_3unit= tkinter.Label(self.child_window, text="times")
        self.label4_3unit.grid(row=4, column=6, padx=10, pady=5, sticky="w")

        self.label5 = tkinter.Label(self.child_window, text="Weight of lift:")
        self.label5.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.spinbox5 = tkinter.Spinbox(self.child_window, from_=0, to=400)
        self.spinbox5.grid(row=5, column=1, padx=10, pady=5)
        self.label5_unit= tkinter.Label(self.child_window, text="KG")
        self.label5_unit.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        self.spinbox5_2 = tkinter.Spinbox(self.child_window, from_=0, to=400)
        self.spinbox5_2.grid(row=5, column=3, padx=10, pady=5)
        self.label5_2unit= tkinter.Label(self.child_window, text="KG")
        self.label5_2unit.grid(row=5, column=4, padx=10, pady=5, sticky="w")

        self.spinbox5_3= tkinter.Spinbox(self.child_window, from_=0, to=400)
        self.spinbox5_3.grid(row=5, column=5, padx=10, pady=5)
        self.label5_3unit= tkinter.Label(self.child_window, text="KG")
        self.label5_3unit.grid(row=5, column=6, padx=10, pady=5, sticky="w")


        # Add a close button
        self.return_value = None  # Initialize the return value
        add_button = tkinter.Button(self.child_window, text="Add to list", command=self.add_to_list)
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_to_list(self):
        # Get the values from the inputs
        # and add them to a tuple
        # then set to return_value

        # self.return_value = (
        #     self.entry1.get(),
        #     self.combobox2.get(),
        #     self.spinbox3.get(),
        #     self.spinbox3_2.get(),
        #     self.spinbox3_3.get(),
        #     self.spinbox4.get(),
        #     self.spinbox4_2.get(),
        #     self.spinbox4_3.get(),
        #     self.spinbox5.get(),
        #     self.spinbox5_2.get(),
        #     self.spinbox5_3.get(),
        # )

        self.return_value = (
            self.entry1.get(),
            self.combobox2.get(),
            [
                [self.spinbox3.get(), self.spinbox4.get(), self.spinbox5.get()],
                [self.spinbox3_2.get(), self.spinbox4_2.get(), self.spinbox5_2.get()],
                [self.spinbox3_3.get(), self.spinbox4_3.get(), self.spinbox5_3.get()],
            ]
        )
        
        self.child_window.destroy()

    def get_value(self):
        # Return the value set before closing
        return self.return_value


class MainWindow:
    def __init__(self):
        # create main window gadget
        self.main_window = tkinter.Tk()
        self.main_window.title("Main Window")
        self.main_window.geometry("900x600")

        self.main_window.grid_columnconfigure(3, weight=1)  # Ensure column 3 expands to the right

        # Add 5 labels to the main window, with the text
        # "Click next button to input a user", "Inputed users:",
        # "Click next button to calculate the points", "Calculated Result:", "The winner is:"
        self.label1 = tkinter.Label(self.main_window, text="Click next button to input a user")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.button1 = tkinter.Button(self.main_window, text="Input a user", command=self.show_child_window)
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        self.label_formula = tkinter.Label(
            self.main_window, 
            text="The formula is:\n"
             "First 10 km runner will get 500 points per 1 km,\n"
             "After 10 km, will get 1000 points per km\n"
             "1st 100 kg get 5 points per 1 kg, after will get 8 points per 1 kg.\n"
             "after calculation if female, will be multiplied by 1.5x",
            justify="left"
        )
        self.label_formula.grid(row=0, column=3, padx=10, pady=10, sticky="e")  # Stick to the right
        self.label2 = tkinter.Label(self.main_window, text="Inputed users:")
        self.label2.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Add a multiline label beside label4
        self.label2_details = tkinter.Label(
            self.main_window, 
            text="Details:\n- Points breakdown will appear here\n- Additional information",
            justify="left"
        )
        self.label2_details.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.label3 = tkinter.Label(self.main_window, text="Click next button to calculate the points")
        self.label3.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.button2 = tkinter.Button(self.main_window, text="Calculate", command=self.calculate)
        self.button2.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        self.label4 = tkinter.Label(self.main_window, text="Calculated Result:")
        self.label4.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        
        # Add a multiline label beside label4
        self.label4_details = tkinter.Label(
            self.main_window, 
            text="- Points & winner will appear here",
            justify="left"
        )
        self.label4_details.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.user_list = []  # list of tuples

        # enter the tk main loop
        tkinter.mainloop()

    def show_child_window(self):
        # Call the ChildWindow class and wait for it to return a value
        child_window = ChildWindow(self.main_window)
        self.main_window.wait_window(child_window.child_window)  # Wait for the child window to close
        returned_value = child_window.get_value()  # Retrieve the value from the child window
        if returned_value:  # Check if a value was returned
            self.user_list.append(returned_value)  # Add the returned value to the list
            self.show_user_list()
        # print(f"Returned value: {returned_value}")  # Example: Print the returned value

    def show_user_list(self):
        # Display the user list in label2_details
        user_list_text = ""
        
        for user in self.user_list:
            user_list_text += user[0] + ", " + user[1] + ",\n" + "day 1: " + user[2][0][0] + " km, " + user[2][0][1] + " reps, " + user[2][0][2] + " kg\n" + "day 2: " + user[2][1][0] + " km, " + user[2][1][1] + " reps, " + user[2][1][2] + " kg\n" + "day 3: " + user[2][2][0] + " km, " + user[2][2][1] + " reps, " + user[2][2][2] + " kg\n"

        if len(user_list_text) > 0:
            user_list_text = user_list_text[:-1]

        self.label2_details.config(text=user_list_text)

    def calculate(self):
        self.label4_details.config(text=show_result(self.user_list))


# Create an instance of the MainWindow class & Run the application
mainWindow = MainWindow()
