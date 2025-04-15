import tkinter
from tkinter import ttk

class ChildWindow:
    def __init__(self, parent):
        # create child window gadget
        self.child_window = tkinter.Toplevel(parent)
        self.child_window.geometry("900x400")
        self.child_window.title("User Information")

        # Center the child window in the top vertical center of the parent window
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        child_width = 900
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

        self.label4 = tkinter.Label(self.child_window, text="Reps:")
        self.label4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.spinbox4 = tkinter.Spinbox(self.child_window, from_=0, to=200)
        self.spinbox4.grid(row=4, column=1, padx=10, pady=5)

        self.label5 = tkinter.Label(self.child_window, text="Weight of lift:")
        self.label5.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.spinbox5 = tkinter.Spinbox(self.child_window, from_=0, to=400)
        self.spinbox5.grid(row=5, column=1, padx=10, pady=5)

        # Add a close button
        self.return_value = None  # Initialize the return value
        add_button = tkinter.Button(self.child_window, text="Add to list", command=self.add_to_list)
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_to_list(self):
        # Get the values from the inputs
        # and add them to a tuple
        # then set to return_value

        self.return_value = (
            self.entry1.get(),
            self.combobox2.get(),
            self.spinbox3.get(),
            self.spinbox4.get(),
            self.spinbox5.get(),
        )
        
        self.child_window.destroy()

    def get_value(self):
        # Return the value set before closing
        return self.return_value