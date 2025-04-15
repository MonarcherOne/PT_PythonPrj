import tkinter
from child_window import ChildWindow  # Import the ChildWindow class
from gym import gym_calculate  # Import the gym_calculate function from gym.py

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
            text="Details:\n- Points breakdown will appear here\n- Additional information",
            justify="left"
        )
        self.label4_details.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.label5 = tkinter.Label(self.main_window, text="The winner is:")
        self.label5.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.label5_result = tkinter.Label(self.main_window, text="")
        self.label5_result.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.user_list = []  # list of tuples
        self.user_results = []  # list of results

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
        print(f"Returned value: {returned_value}")  # Example: Print the returned value

    def show_user_list(self):
        # Display the user list in label2_details
        user_list_text = ""
        
        for user in self.user_list:
            user_list_text += user[0] + ", " + user[1] + ", " + user[2] + " km, " + user[3] + " reps, " + user[4] + " kg\n"

        if len(user_list_text) > 0:
            user_list_text = user_list_text[:-1]

        self.label2_details.config(text=user_list_text)

    def calculate(self):
        for user in self.user_list:
            # Calculate the points for each user and add to the user_results list
            result = gym_calculate(user[1], float(user[2]), int(user[3]), float(user[4]))
            self.user_results.append((user[0], result))

        # Display the results in label4_details
        max_user = self.user_results[0]
        result_text = ""
        for user, result in self.user_results:
            result_text += f"{user}: {result} points\n"
            if result > max_user[1]:
                max_user = (user, result)

        if len(result_text) > 0:
            result_text = result_text[:-1]

        self.label4_details.config(text=result_text)
        self.label5_result.config(text=f"Winner is: {max_user[0]} with {max_user[1]} points")


# create an instance of the MainWindow class
mainWindow = MainWindow()


