import tkinter as tk


class IntroButtons:
    def __init__(self, window):
        # Intro buttons
        self.window = window
        self.update_button = tk.Button(window, text="Update", font=("Helvetica", 25), command=lambda: self.intro_decision('update'))
        self.update_button.grid(row=0, padx=(90, 100), pady=120)
        self.calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 25), command=lambda: self.intro_decision('calculate'))
        self.calculate_button.grid(row=0, padx=(30, 100), column=1)

    def intro_decision(self, decision):
        if decision == 'update':
            print('update')
            self.window.config(bg='white')
            self.update_button.grid_remove()
            self.calculate_button.grid_remove()
            update_buttons = UpdateButtons(self.window)

        elif decision == 'calculate':
            print('calculate')
            self.window.config(bg='black')
            self.update_button.grid_remove()
            self.calculate_button.grid_remove()


class UpdateButtons:
    def __init__(self, window):
        # Grade levels
        self.window = window
        self.g7_button = tk.Button(window, text="Grade 7 ", font=("Helvetica", 20), command=lambda: self.grade_decision('7'))
        self.g7_button.grid(row=0, padx=(90, 100), pady=20)
        self.g8_button = tk.Button(window, text="Grade 8 ", font=("Helvetica", 20), command=lambda: self.grade_decision('8'))
        self.g8_button.grid(row=0, padx=(30, 100), column=1)
        self.g9_button = tk.Button(window, text="Grade 9 ", font=("Helvetica", 20), command=lambda: self.grade_decision('9'))
        self.g9_button.grid(row=1, padx=(90, 100), pady=20)
        self.g10_button = tk.Button(window, text="Grade 10", font=("Helvetica", 20), command=lambda: self.grade_decision('10'))
        self.g10_button.grid(row=1, padx=(35, 100), column=1)
        self.g11_button = tk.Button(window, text="Grade 11", font=("Helvetica", 20), command=lambda: self.grade_decision('11'))
        self.g11_button.grid(row=2, padx=(90, 100), pady=20)
        self.g12_button = tk.Button(window, text="Grade 12", font=("Helvetica", 20), command=lambda: self.grade_decision('12'))
        self.g12_button.grid(row=2, padx=(35, 100), column=1)

    def grade_decision(self, decision):
        if decision == '7':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()



def main():
    window = tk.Tk()

    # Window configurations
    window.title("GWA Application by Bryan")
    window.resizable(width='FALSE', height='FALSE')
    window.configure(background="black")
    window.geometry('600x300')

    buttons = IntroButtons(window)

    window.mainloop()


if __name__ == "__main__":
    main()
