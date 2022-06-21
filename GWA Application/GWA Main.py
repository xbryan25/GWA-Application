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
    # Grade 7 grades
    g7_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g8_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

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
            self.g7_update()
        elif decision == '8':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()
            self.g8_update()
        elif decision == '9':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()
        elif decision == '10':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()
        elif decision == '11':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()
        elif decision == '12':
            self.g7_button.grid_remove()
            self.g8_button.grid_remove()
            self.g9_button.grid_remove()
            self.g10_button.grid_remove()
            self.g11_button.grid_remove()
            self.g12_button.grid_remove()

    def g7_update(self):
        # Grade 7 buttons
        g7_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10))
        g7_is_label.grid(row=0, column=1)
        g7_is_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[0], g7_is_grade_label, 0, 7))
        g7_is_minus_button.grid(row=1, column=0)
        g7_is_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[0]}", font=("Helvetica", 10))
        g7_is_grade_label.grid(row=1, column=1)
        g7_is_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[0], g7_is_grade_label, 0, 7))
        g7_is_add_button.grid(row=1, column=2)

        g7_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g7_math_label.grid(row=0, column=4)
        g7_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[1], g7_math_grade_label, 1, 7))
        g7_math_minus_button.grid(row=1, column=3)
        g7_math_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[1]}", font=("Helvetica", 10))
        g7_math_grade_label.grid(row=1, column=4)
        g7_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[1], g7_math_grade_label, 1, 7))
        g7_math_add_button.grid(row=1, column=5)

        g7_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g7_eng_label.grid(row=2, column=1)
        g7_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[2], g7_eng_grade_label, 2, 7))
        g7_eng_minus_button.grid(row=3, column=0)
        g7_eng_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[2]}", font=("Helvetica", 10))
        g7_eng_grade_label.grid(row=3, column=1)
        g7_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[2], g7_eng_grade_label, 2, 7))
        g7_eng_add_button.grid(row=3, column=2)

        g7_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g7_fil_label.grid(row=2, column=4)
        g7_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[3], g7_fil_grade_label, 3, 7))
        g7_fil_minus_button.grid(row=3, column=3)
        g7_fil_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[3]}", font=("Helvetica", 10))
        g7_fil_grade_label.grid(row=3, column=4)
        g7_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[3], g7_fil_grade_label, 3, 7))
        g7_fil_add_button.grid(row=3, column=5)

        g7_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g7_ss_label.grid(row=4, column=1)
        g7_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[4], g7_ss_grade_label, 4, 7))
        g7_ss_minus_button.grid(row=5, column=0)
        g7_ss_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[4]}", font=("Helvetica", 10))
        g7_ss_grade_label.grid(row=5, column=1)
        g7_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[4], g7_ss_grade_label, 4, 7))
        g7_ss_add_button.grid(row=5, column=2)

        g7_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g7_pehm_label.grid(row=4, column=4)
        g7_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[5], g7_pehm_grade_label, 5, 7))
        g7_pehm_minus_button.grid(row=5, column=3)
        g7_pehm_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[5]}", font=("Helvetica", 10))
        g7_pehm_grade_label.grid(row=5, column=4)
        g7_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[5], g7_pehm_grade_label, 5, 7))
        g7_pehm_add_button.grid(row=5, column=5)

        g7_valed_label = tk.Label(self.window, text="Values Education", font=("Helvetica", 10))
        g7_valed_label.grid(row=6, column=1)
        g7_valed_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[6], g7_valed_grade_label, 6, 7))
        g7_valed_minus_button.grid(row=7, column=0)
        g7_valed_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[6]}", font=("Helvetica", 10))
        g7_valed_grade_label.grid(row=7, column=1)
        g7_valed_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[6], g7_valed_grade_label, 6, 7))
        g7_valed_add_button.grid(row=7, column=2)

        g7_adtech_label = tk.Label(self.window, text="Adtech", font=("Helvetica", 10))
        g7_adtech_label.grid(row=6, column=4)
        g7_adtech_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[7], g7_adtech_grade_label, 7, 7))
        g7_adtech_minus_button.grid(row=7, column=3)
        g7_adtech_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[7]}", font=("Helvetica", 10))
        g7_adtech_grade_label.grid(row=7, column=4)
        g7_adtech_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[7], g7_adtech_grade_label, 7, 7))
        g7_adtech_add_button.grid(row=7, column=5)

        g7_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g7_cs_label.grid(row=8, column=1)
        g7_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g7_grades[8], g7_cs_grade_label, 8, 7))
        g7_cs_minus_button.grid(row=9, column=0)
        g7_cs_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g7_grades[8]}", font=("Helvetica", 10))
        g7_cs_grade_label.grid(row=9, column=1)
        g7_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g7_grades[8], g7_cs_grade_label, 8, 7))
        g7_cs_add_button.grid(row=9, column=2)

    def g8_update(self):
        # Grade 8 buttons
        g8_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10))
        g8_is_label.grid(row=0, column=1)
        g8_is_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[0], g8_is_grade_label, 0, 8))
        g8_is_minus_button.grid(row=1, column=0)
        g8_is_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[0]}", font=("Helvetica", 10))
        g8_is_grade_label.grid(row=1, column=1)
        g8_is_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[0], g8_is_grade_label, 0, 8))
        g8_is_add_button.grid(row=1, column=2)

        g8_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g8_math_label.grid(row=0, column=4)
        g8_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[1], g8_math_grade_label, 1, 8))
        g8_math_minus_button.grid(row=1, column=3)
        g8_math_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[1]}", font=("Helvetica", 10))
        g8_math_grade_label.grid(row=1, column=4)
        g8_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[1], g8_math_grade_label, 1, 8))
        g8_math_add_button.grid(row=1, column=5)

        g8_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g8_eng_label.grid(row=2, column=1)
        g8_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[2], g8_eng_grade_label, 2, 8))
        g8_eng_minus_button.grid(row=3, column=0)
        g8_eng_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[2]}", font=("Helvetica", 10))
        g8_eng_grade_label.grid(row=3, column=1)
        g8_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[2], g8_eng_grade_label, 2, 8))
        g8_eng_add_button.grid(row=3, column=2)

        g8_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g8_fil_label.grid(row=2, column=4)
        g8_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[3], g8_fil_grade_label, 3, 8))
        g8_fil_minus_button.grid(row=3, column=3)
        g8_fil_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[3]}", font=("Helvetica", 10))
        g8_fil_grade_label.grid(row=3, column=4)
        g8_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[3], g8_fil_grade_label, 3, 8))
        g8_fil_add_button.grid(row=3, column=5)

        g8_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g8_ss_label.grid(row=4, column=1)
        g8_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[4], g8_ss_grade_label, 4, 8))
        g8_ss_minus_button.grid(row=5, column=0)
        g8_ss_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[4]}", font=("Helvetica", 10))
        g8_ss_grade_label.grid(row=5, column=1)
        g8_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[4], g8_ss_grade_label, 4, 8))
        g8_ss_add_button.grid(row=5, column=2)

        g8_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g8_pehm_label.grid(row=4, column=4)
        g8_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[5], g8_pehm_grade_label, 5, 8))
        g8_pehm_minus_button.grid(row=5, column=3)
        g8_pehm_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[5]}", font=("Helvetica", 10))
        g8_pehm_grade_label.grid(row=5, column=4)
        g8_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[5], g8_pehm_grade_label, 5, 8))
        g8_pehm_add_button.grid(row=5, column=5)

        g8_valed_label = tk.Label(self.window, text="Values Education", font=("Helvetica", 10))
        g8_valed_label.grid(row=6, column=1)
        g8_valed_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[6], g8_valed_grade_label, 6, 8))
        g8_valed_minus_button.grid(row=7, column=0)
        g8_valed_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[6]}", font=("Helvetica", 10))
        g8_valed_grade_label.grid(row=7, column=1)
        g8_valed_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[6], g8_valed_grade_label, 6, 8))
        g8_valed_add_button.grid(row=7, column=2)

        g8_adtech_label = tk.Label(self.window, text="Adtech", font=("Helvetica", 10))
        g8_adtech_label.grid(row=6, column=4)
        g8_adtech_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[7], g8_adtech_grade_label, 7, 8))
        g8_adtech_minus_button.grid(row=7, column=3)
        g8_adtech_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[7]}", font=("Helvetica", 10))
        g8_adtech_grade_label.grid(row=7, column=4)
        g8_adtech_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[7], g8_adtech_grade_label, 7, 8))
        g8_adtech_add_button.grid(row=7, column=5)

        g8_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g8_cs_label.grid(row=8, column=1)
        g8_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[8], g8_cs_grade_label, 8, 8))
        g8_cs_minus_button.grid(row=9, column=0)
        g8_cs_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[8]}", font=("Helvetica", 10))
        g8_cs_grade_label.grid(row=9, column=1)
        g8_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[8], g8_cs_grade_label, 8, 8))
        g8_cs_add_button.grid(row=9, column=2)

        g8_es_label = tk.Label(self.window, text="Earth Science", font=("Helvetica", 10))
        g8_es_label.grid(row=8, column=4)
        g8_es_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', UpdateButtons.g8_grades[9], g8_es_grade_label, 9, 8))
        g8_es_minus_button.grid(row=9, column=3)
        g8_es_grade_label = tk.Label(self.window, text=f"{UpdateButtons.g8_grades[9]}", font=("Helvetica", 10))
        g8_es_grade_label.grid(row=9, column=4)
        g8_es_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', UpdateButtons.g8_grades[9], g8_es_grade_label, 9, 8))
        g8_es_add_button.grid(row=9, column=5)

    @staticmethod
    def grade_change(operation, grade, label, index, grade_level):
        if operation == '+':
            if grade < 5.0:
                grade += 0.25

                if grade_level == 7:
                    UpdateButtons.g7_grades[index] = grade
                elif grade_level == 8:
                    UpdateButtons.g8_grades[index] = grade
                # elif grade_level == '9':
                #     UpdateButtons.g9_grades[index] = grade
                # elif grade_level == '10':
                #     UpdateButtons.g10_grades[index] = grade
                # elif grade_level == '11':
                #     UpdateButtons.g11_grades[index] = grade
                # elif grade_level == '12':
                #     UpdateButtons.g12_grades[index] = grade

                label.config(text=f"{grade}", font=("Helvetica", 10))
        elif operation == '-':
            if grade > 1.0:
                grade -= 0.25

                if grade_level == 7:
                    UpdateButtons.g7_grades[index] = grade
                elif grade_level == 8:
                    UpdateButtons.g8_grades[index] = grade
                # elif grade_level == '9':
                #     UpdateButtons.g9_grades[index] = grade
                # elif grade_level == '10':
                #     UpdateButtons.g10_grades[index] = grade
                # elif grade_level == '11':
                #     UpdateButtons.g11_grades[index] = grade
                # elif grade_level == '12':
                #     UpdateButtons.g12_grades[index] = grade

                UpdateButtons.g7_grades[index] = grade
                label.config(text=f"{grade}", font=("Helvetica", 10))

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
