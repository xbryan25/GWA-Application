import tkinter as tk


def intro_buttons(window):
    update_button = tk.Button(window, text="Update", font=("Helvetica", 25), command=lambda: intro_decision('update')).grid(row=0, padx=(90, 100), pady=120)
    calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 25), command=lambda: intro_decision('calculate')).grid(row=0, padx=(30, 100), column=1)


def intro_decision(decision):
    if decision == 'update':
        print('update')
    elif decision == 'calculate':
        print('calculate')


def main():
    window = tk.Tk()

    # Window configurations
    window.title("GWA Application by Bryan")
    window.resizable(width='FALSE', height='FALSE')
    window.configure(background="black")
    window.geometry('600x300')

    intro_buttons(window)

    window.mainloop()


if __name__ == "__main__":
    main()
