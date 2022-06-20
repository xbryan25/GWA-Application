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
            self.update_button.config(state='disabled')
            self.calculate_button.config(state='active')

        elif decision == 'calculate':
            print('calculate')
            self.window.config(bg='black')
            self.update_button.config(state='active')
            self.calculate_button.config(state='disabled')


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
