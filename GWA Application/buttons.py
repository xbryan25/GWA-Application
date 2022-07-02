import tkinter as tk
import csv


class IntroButtons:
    def __init__(self, window):
        # Intro buttons
        self.window = window
        self.calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 25), command=lambda: self.intro_decision('calculate'))
        self.calculate_button.grid(row=0, padx=(220, 0), pady=(120, 60))
        self.credits_button = tk.Button(window, text="About this app", font=("Helvetica", 15), command=lambda: self.intro_decision('about_this_app'))
        self.credits_button.grid(row=1, padx=(60, 100), column=1)

    def intro_decision(self, decision):
        if decision == 'calculate':
            self.window.config(bg='white')
            self.calculate_button.grid_remove()
            self.credits_button.grid_remove()
            CalculateButtons(self.window)

        elif decision == 'about_this_app':
            self.calculate_button.grid_remove()
            self.credits_button.grid_remove()
            AboutThisApp(self.window)


class CalculateButtons:
    # Grade 7 grades
    g7_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g8_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g9_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g10_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g11_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    g12_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    def __init__(self, window, state=0):
        # Back button
        self.back_button = tk.Button(window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(0))
        self.back_button.place(x=10, y=20)

        # Grade levels
        self.window = window
        self.g7_button = tk.Button(window, text="Grade 7 ", font=("Helvetica", 20), command=lambda: self.grade_decision('7'))
        self.g7_button.grid(row=1, padx=(90, 100), pady=20)
        self.g8_button = tk.Button(window, text="Grade 8 ", font=("Helvetica", 20), command=lambda: self.grade_decision('8'))
        self.g8_button.grid(row=1, padx=(30, 100), column=1)
        self.g9_button = tk.Button(window, text="Grade 9 ", font=("Helvetica", 20), command=lambda: self.grade_decision('9'))
        self.g9_button.grid(row=2, padx=(90, 100), pady=20)
        self.g10_button = tk.Button(window, text="Grade 10", font=("Helvetica", 20), command=lambda: self.grade_decision('10'))
        self.g10_button.grid(row=2, padx=(35, 100), column=1)
        self.g11_button = tk.Button(window, text="Grade 11", font=("Helvetica", 20), command=lambda: self.grade_decision('11'))
        self.g11_button.grid(row=3, padx=(90, 100), pady=20)
        self.g12_button = tk.Button(window, text="Grade 12", font=("Helvetica", 20), command=lambda: self.grade_decision('12'))
        self.g12_button.grid(row=3, padx=(35, 100), column=1)

    def back_decision(self, state, widgets=None, gwa_labels=None):
        if state == 0:
            self.back_button.destroy()
            self.g7_button.destroy()
            self.g8_button.destroy()
            self.g9_button.destroy()
            self.g10_button.destroy()
            self.g11_button.destroy()
            self.g12_button.destroy()
            self.window.config(bg='black')
            buttons = IntroButtons(self.window)
        elif state == 1:
            for widget in widgets:
                widget.destroy()

            if gwa_labels is not None:
                for gwa_label in gwa_labels:
                    gwa_label.destroy()

            CalculateButtons.g7_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g8_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g9_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g10_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g11_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g12_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

            SaveGWA(self.window, state=1)

            update_buttons = CalculateButtons(self.window, 1)
        else:
            print("Not found")

    def grade_decision(self, decision):
        self.back_button.destroy()
        self.g7_button.destroy()
        self.g8_button.destroy()
        self.g9_button.destroy()
        self.g10_button.destroy()
        self.g11_button.destroy()
        self.g12_button.destroy()

        if decision == '7':
            self.g7_update()
        elif decision == '8':
            self.g8_update()
        elif decision == '9':
            self.g9_update()
        elif decision == '10':
            self.g10_update()
        elif decision == '11':
            self.g11_update()
        elif decision == '12':
            self.g12_update()

    def g7_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g7_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G7', CalculateButtons.g7_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 7 buttons
        g7_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10))
        g7_is_label.grid(row=0, column=1)
        g7_is_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[0], g7_is_grade_label, 0, 7, gwa_label))
        g7_is_minus_button.grid(row=1, column=0, padx=(200, 0))
        g7_is_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[0]}", font=("Helvetica", 10))
        g7_is_grade_label.grid(row=1, column=1)
        g7_is_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[0], g7_is_grade_label, 0, 7, gwa_label))
        g7_is_add_button.grid(row=1, column=2)

        g7_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g7_math_label.grid(row=0, column=4)
        g7_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[1], g7_math_grade_label, 1, 7, gwa_label))
        g7_math_minus_button.grid(row=1, column=3)
        g7_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[1]}", font=("Helvetica", 10))
        g7_math_grade_label.grid(row=1, column=4)
        g7_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[1], g7_math_grade_label, 1, 7, gwa_label))
        g7_math_add_button.grid(row=1, column=5)

        g7_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g7_eng_label.grid(row=2, column=1)
        g7_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[2], g7_eng_grade_label, 2, 7, gwa_label))
        g7_eng_minus_button.grid(row=3, column=0, padx=(200, 0))
        g7_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[2]}", font=("Helvetica", 10))
        g7_eng_grade_label.grid(row=3, column=1)
        g7_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[2], g7_eng_grade_label, 2, 7, gwa_label))
        g7_eng_add_button.grid(row=3, column=2)

        g7_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g7_fil_label.grid(row=2, column=4)
        g7_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[3], g7_fil_grade_label, 3, 7, gwa_label))
        g7_fil_minus_button.grid(row=3, column=3)
        g7_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[3]}", font=("Helvetica", 10))
        g7_fil_grade_label.grid(row=3, column=4)
        g7_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[3], g7_fil_grade_label, 3, 7, gwa_label))
        g7_fil_add_button.grid(row=3, column=5)

        g7_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g7_ss_label.grid(row=4, column=1)
        g7_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[4], g7_ss_grade_label, 4, 7, gwa_label))
        g7_ss_minus_button.grid(row=5, column=0, padx=(200, 0))
        g7_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[4]}", font=("Helvetica", 10))
        g7_ss_grade_label.grid(row=5, column=1)
        g7_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[4], g7_ss_grade_label, 4, 7, gwa_label))
        g7_ss_add_button.grid(row=5, column=2)

        g7_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g7_pehm_label.grid(row=4, column=4)
        g7_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[5], g7_pehm_grade_label, 5, 7, gwa_label))
        g7_pehm_minus_button.grid(row=5, column=3)
        g7_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[5]}", font=("Helvetica", 10))
        g7_pehm_grade_label.grid(row=5, column=4)
        g7_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[5], g7_pehm_grade_label, 5, 7, gwa_label))
        g7_pehm_add_button.grid(row=5, column=5)

        g7_valed_label = tk.Label(self.window, text="Values Education", font=("Helvetica", 10))
        g7_valed_label.grid(row=6, column=1)
        g7_valed_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[6], g7_valed_grade_label, 6, 7, gwa_label))
        g7_valed_minus_button.grid(row=7, column=0, padx=(200, 0))
        g7_valed_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[6]}", font=("Helvetica", 10))
        g7_valed_grade_label.grid(row=7, column=1)
        g7_valed_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[6], g7_valed_grade_label, 6, 7, gwa_label))
        g7_valed_add_button.grid(row=7, column=2)

        g7_adtech_label = tk.Label(self.window, text="Adtech", font=("Helvetica", 10))
        g7_adtech_label.grid(row=6, column=4)
        g7_adtech_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[7], g7_adtech_grade_label, 7, 7, gwa_label))
        g7_adtech_minus_button.grid(row=7, column=3)
        g7_adtech_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[7]}", font=("Helvetica", 10))
        g7_adtech_grade_label.grid(row=7, column=4)
        g7_adtech_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[7], g7_adtech_grade_label, 7, 7, gwa_label))
        g7_adtech_add_button.grid(row=7, column=5)

        g7_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g7_cs_label.grid(row=8, column=1)
        g7_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g7_grades[8], g7_cs_grade_label, 8, 7, gwa_label))
        g7_cs_minus_button.grid(row=9, column=0, padx=(200, 0))
        g7_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[8]}", font=("Helvetica", 10))
        g7_cs_grade_label.grid(row=9, column=1)
        g7_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g7_grades[8], g7_cs_grade_label, 8, 7, gwa_label))
        g7_cs_add_button.grid(row=9, column=2)

        g7_buttons = [g7_is_label, g7_is_minus_button, g7_is_grade_label, g7_is_add_button,
                      g7_math_label, g7_math_minus_button, g7_math_grade_label, g7_math_add_button,
                      g7_eng_label, g7_eng_minus_button, g7_eng_grade_label, g7_eng_add_button,
                      g7_fil_label, g7_fil_minus_button, g7_fil_grade_label, g7_fil_add_button,
                      g7_ss_label, g7_ss_minus_button, g7_ss_grade_label, g7_ss_add_button,
                      g7_pehm_label, g7_pehm_minus_button, g7_pehm_grade_label, g7_pehm_add_button,
                      g7_valed_label, g7_valed_minus_button, g7_valed_grade_label, g7_valed_add_button,
                      g7_adtech_label, g7_adtech_minus_button, g7_adtech_grade_label, g7_adtech_add_button,
                      g7_cs_label, g7_cs_minus_button, g7_cs_grade_label, g7_cs_add_button,
                      back_button, save_gwa_button]

    def g8_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g8_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G8', CalculateButtons.g8_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 8 buttons
        g8_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10))
        g8_is_label.grid(row=0, column=1)
        g8_is_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[0], g8_is_grade_label, 0, 8, gwa_label))
        g8_is_minus_button.grid(row=1, column=0, padx=(200, 0))
        g8_is_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[0]}", font=("Helvetica", 10))
        g8_is_grade_label.grid(row=1, column=1)
        g8_is_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[0], g8_is_grade_label, 0, 8, gwa_label))
        g8_is_add_button.grid(row=1, column=2)

        g8_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g8_math_label.grid(row=0, column=4)
        g8_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[1], g8_math_grade_label, 1, 8, gwa_label))
        g8_math_minus_button.grid(row=1, column=3)
        g8_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[1]}", font=("Helvetica", 10))
        g8_math_grade_label.grid(row=1, column=4)
        g8_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[1], g8_math_grade_label, 1, 8, gwa_label))
        g8_math_add_button.grid(row=1, column=5)

        g8_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g8_eng_label.grid(row=2, column=1)
        g8_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[2], g8_eng_grade_label, 2, 8, gwa_label))
        g8_eng_minus_button.grid(row=3, column=0, padx=(200, 0))
        g8_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[2]}", font=("Helvetica", 10))
        g8_eng_grade_label.grid(row=3, column=1)
        g8_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[2], g8_eng_grade_label, 2, 8, gwa_label))
        g8_eng_add_button.grid(row=3, column=2)

        g8_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g8_fil_label.grid(row=2, column=4)
        g8_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[3], g8_fil_grade_label, 3, 8, gwa_label))
        g8_fil_minus_button.grid(row=3, column=3)
        g8_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[3]}", font=("Helvetica", 10))
        g8_fil_grade_label.grid(row=3, column=4)
        g8_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[3], g8_fil_grade_label, 3, 8, gwa_label))
        g8_fil_add_button.grid(row=3, column=5)

        g8_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g8_ss_label.grid(row=4, column=1)
        g8_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[4], g8_ss_grade_label, 4, 8, gwa_label))
        g8_ss_minus_button.grid(row=5, column=0, padx=(200, 0))
        g8_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[4]}", font=("Helvetica", 10))
        g8_ss_grade_label.grid(row=5, column=1)
        g8_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[4], g8_ss_grade_label, 4, 8, gwa_label))
        g8_ss_add_button.grid(row=5, column=2)

        g8_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g8_pehm_label.grid(row=4, column=4)
        g8_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[5], g8_pehm_grade_label, 5, 8, gwa_label))
        g8_pehm_minus_button.grid(row=5, column=3)
        g8_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[5]}", font=("Helvetica", 10))
        g8_pehm_grade_label.grid(row=5, column=4)
        g8_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[5], g8_pehm_grade_label, 5, 8, gwa_label))
        g8_pehm_add_button.grid(row=5, column=5)

        g8_valed_label = tk.Label(self.window, text="Values Education", font=("Helvetica", 10))
        g8_valed_label.grid(row=6, column=1)
        g8_valed_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[6], g8_valed_grade_label, 6, 8, gwa_label))
        g8_valed_minus_button.grid(row=7, column=0, padx=(200, 0))
        g8_valed_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[6]}", font=("Helvetica", 10))
        g8_valed_grade_label.grid(row=7, column=1)
        g8_valed_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[6], g8_valed_grade_label, 6, 8, gwa_label))
        g8_valed_add_button.grid(row=7, column=2)

        g8_adtech_label = tk.Label(self.window, text="Adtech", font=("Helvetica", 10))
        g8_adtech_label.grid(row=6, column=4)
        g8_adtech_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[7], g8_adtech_grade_label, 7, 8, gwa_label))
        g8_adtech_minus_button.grid(row=7, column=3)
        g8_adtech_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[7]}", font=("Helvetica", 10))
        g8_adtech_grade_label.grid(row=7, column=4)
        g8_adtech_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[7], g8_adtech_grade_label, 7, 8, gwa_label))
        g8_adtech_add_button.grid(row=7, column=5)

        g8_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g8_cs_label.grid(row=8, column=1)
        g8_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[8], g8_cs_grade_label, 8, 8, gwa_label))
        g8_cs_minus_button.grid(row=9, column=0, padx=(200, 0))
        g8_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[8]}", font=("Helvetica", 10))
        g8_cs_grade_label.grid(row=9, column=1)
        g8_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[8], g8_cs_grade_label, 8, 8, gwa_label))
        g8_cs_add_button.grid(row=9, column=2)

        g8_es_label = tk.Label(self.window, text="Earth Science", font=("Helvetica", 10))
        g8_es_label.grid(row=8, column=4)
        g8_es_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g8_grades[9], g8_es_grade_label, 9, 8, gwa_label))
        g8_es_minus_button.grid(row=9, column=3)
        g8_es_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[9]}", font=("Helvetica", 10))
        g8_es_grade_label.grid(row=9, column=4)
        g8_es_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g8_grades[9], g8_es_grade_label, 9, 8, gwa_label))
        g8_es_add_button.grid(row=9, column=5)

        g8_buttons = [g8_is_label, g8_is_minus_button, g8_is_grade_label, g8_is_add_button,
                      g8_math_label, g8_math_minus_button, g8_math_grade_label, g8_math_add_button,
                      g8_eng_label, g8_eng_minus_button, g8_eng_grade_label, g8_eng_add_button,
                      g8_fil_label, g8_fil_minus_button, g8_fil_grade_label, g8_fil_add_button,
                      g8_ss_label, g8_ss_minus_button, g8_ss_grade_label, g8_ss_add_button,
                      g8_pehm_label, g8_pehm_minus_button, g8_pehm_grade_label, g8_pehm_add_button,
                      g8_valed_label, g8_valed_minus_button, g8_valed_grade_label, g8_valed_add_button,
                      g8_adtech_label, g8_adtech_minus_button, g8_adtech_grade_label, g8_adtech_add_button,
                      g8_cs_label, g8_cs_minus_button, g8_cs_grade_label, g8_cs_add_button,
                      g8_es_label, g8_es_minus_button, g8_es_grade_label, g8_es_add_button,
                      back_button, save_gwa_button]

    def g9_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g9_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G9', CalculateButtons.g9_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 9 buttons
        g9_bio_label = tk.Label(self.window, text="Biology", font=("Helvetica", 10))
        g9_bio_label.grid(row=0, column=1)
        g9_bio_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[0], g9_bio_grade_label, 0, 9, gwa_label))
        g9_bio_minus_button.grid(row=1, column=0, padx=(200, 0))
        g9_bio_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[0]}", font=("Helvetica", 10))
        g9_bio_grade_label.grid(row=1, column=1)
        g9_bio_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[0], g9_bio_grade_label, 0, 9, gwa_label))
        g9_bio_add_button.grid(row=1, column=2)

        g9_chem_label = tk.Label(self.window, text="Chemistry", font=("Helvetica", 10))
        g9_chem_label.grid(row=0, column=4)
        g9_chem_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[1], g9_chem_grade_label, 1, 9, gwa_label))
        g9_chem_minus_button.grid(row=1, column=3)
        g9_chem_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[1]}", font=("Helvetica", 10))
        g9_chem_grade_label.grid(row=1, column=4)
        g9_chem_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[1], g9_chem_grade_label, 1, 9, gwa_label))
        g9_chem_add_button.grid(row=1, column=5)

        g9_p6_label = tk.Label(self.window, text="Physics", font=("Helvetica", 10))
        g9_p6_label.grid(row=2, column=1)
        g9_p6_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[2], g9_p6_grade_label, 2, 9, gwa_label))
        g9_p6_minus_button.grid(row=3, column=0, padx=(200, 0))
        g9_p6_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[2]}", font=("Helvetica", 10))
        g9_p6_grade_label.grid(row=3, column=1)
        g9_p6_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[2], g9_p6_grade_label, 2, 9, gwa_label))
        g9_p6_add_button.grid(row=3, column=2)

        g9_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g9_math_label.grid(row=2, column=4)
        g9_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[3], g9_math_grade_label, 3, 9, gwa_label))
        g9_math_minus_button.grid(row=3, column=3)
        g9_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[3]}", font=("Helvetica", 10))
        g9_math_grade_label.grid(row=3, column=4)
        g9_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[3], g9_math_grade_label, 3, 9, gwa_label))
        g9_math_add_button.grid(row=3, column=5)

        g9_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g9_eng_label.grid(row=4, column=1)
        g9_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[4], g9_eng_grade_label, 4, 9, gwa_label))
        g9_eng_minus_button.grid(row=5, column=0, padx=(200, 0))
        g9_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[4]}", font=("Helvetica", 10))
        g9_eng_grade_label.grid(row=5, column=1)
        g9_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[4], g9_eng_grade_label, 4, 9, gwa_label))
        g9_eng_add_button.grid(row=5, column=2)

        g9_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g9_fil_label.grid(row=4, column=4)
        g9_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[5], g9_fil_grade_label, 5, 9, gwa_label))
        g9_fil_minus_button.grid(row=5, column=3)
        g9_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[5]}", font=("Helvetica", 10))
        g9_fil_grade_label.grid(row=5, column=4)
        g9_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[5], g9_fil_grade_label, 5, 9, gwa_label))
        g9_fil_add_button.grid(row=5, column=5)

        g9_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g9_ss_label.grid(row=6, column=1)
        g9_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[6], g9_ss_grade_label, 6, 9, gwa_label))
        g9_ss_minus_button.grid(row=7, column=0, padx=(200, 0))
        g9_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[6]}", font=("Helvetica", 10))
        g9_ss_grade_label.grid(row=7, column=1)
        g9_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[6], g9_ss_grade_label, 6, 9, gwa_label))
        g9_ss_add_button.grid(row=7, column=2)

        g9_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g9_pehm_label.grid(row=6, column=4)
        g9_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[7], g9_pehm_grade_label, 7, 9, gwa_label))
        g9_pehm_minus_button.grid(row=7, column=3)
        g9_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[7]}", font=("Helvetica", 10))
        g9_pehm_grade_label.grid(row=7, column=4)
        g9_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[7], g9_pehm_grade_label, 7, 9, gwa_label))
        g9_pehm_add_button.grid(row=7, column=5)

        g9_stat_label = tk.Label(self.window, text="Statistics", font=("Helvetica", 10))
        g9_stat_label.grid(row=8, column=1)
        g9_stat_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[8], g9_stat_grade_label, 8, 9, gwa_label))
        g9_stat_minus_button.grid(row=9, column=0, padx=(200, 0))
        g9_stat_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[8]}", font=("Helvetica", 10))
        g9_stat_grade_label.grid(row=9, column=1)
        g9_stat_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[8], g9_stat_grade_label, 8, 9, gwa_label))
        g9_stat_add_button.grid(row=9, column=2)

        g9_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g9_cs_label.grid(row=8, column=4)
        g9_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g9_grades[9], g9_cs_grade_label, 9, 9, gwa_label))
        g9_cs_minus_button.grid(row=9, column=3)
        g9_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[9]}", font=("Helvetica", 10))
        g9_cs_grade_label.grid(row=9, column=4)
        g9_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g9_grades[9], g9_cs_grade_label, 9, 9, gwa_label))
        g9_cs_add_button.grid(row=9, column=5)

        g9_buttons = [g9_bio_label, g9_bio_minus_button, g9_bio_grade_label, g9_bio_add_button,
                      g9_chem_label, g9_chem_minus_button, g9_chem_grade_label, g9_chem_add_button,
                      g9_p6_label, g9_p6_minus_button, g9_p6_grade_label, g9_p6_add_button,
                      g9_math_label, g9_math_minus_button, g9_math_grade_label, g9_math_add_button,
                      g9_eng_label, g9_eng_minus_button, g9_eng_grade_label, g9_eng_add_button,
                      g9_fil_label, g9_fil_minus_button, g9_fil_grade_label, g9_fil_add_button,
                      g9_ss_label, g9_ss_minus_button, g9_ss_grade_label, g9_ss_add_button,
                      g9_pehm_label, g9_pehm_minus_button, g9_pehm_grade_label, g9_pehm_add_button,
                      g9_stat_label, g9_stat_minus_button, g9_stat_grade_label, g9_stat_add_button,
                      g9_cs_label, g9_cs_minus_button, g9_cs_grade_label, g9_cs_add_button,
                      back_button, save_gwa_button]

    def g10_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g10_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G10', CalculateButtons.g10_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 10 buttons
        g10_bio_label = tk.Label(self.window, text="Biology", font=("Helvetica", 10))
        g10_bio_label.grid(row=0, column=1)
        g10_bio_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[0], g10_bio_grade_label, 0, 10, gwa_label))
        g10_bio_minus_button.grid(row=1, column=0, padx=(200, 0))
        g10_bio_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[0]}", font=("Helvetica", 10))
        g10_bio_grade_label.grid(row=1, column=1)
        g10_bio_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[0], g10_bio_grade_label, 0, 10, gwa_label))
        g10_bio_add_button.grid(row=1, column=2)

        g10_chem_label = tk.Label(self.window, text="Chemistry", font=("Helvetica", 10))
        g10_chem_label.grid(row=0, column=4)
        g10_chem_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[1], g10_chem_grade_label, 1, 10, gwa_label))
        g10_chem_minus_button.grid(row=1, column=3)
        g10_chem_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[1]}", font=("Helvetica", 10))
        g10_chem_grade_label.grid(row=1, column=4)
        g10_chem_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[1], g10_chem_grade_label, 1, 10, gwa_label))
        g10_chem_add_button.grid(row=1, column=5)

        g10_p6_label = tk.Label(self.window, text="Physics", font=("Helvetica", 10))
        g10_p6_label.grid(row=2, column=1)
        g10_p6_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[2], g10_p6_grade_label, 2, 10, gwa_label))
        g10_p6_minus_button.grid(row=3, column=0, padx=(200, 0))
        g10_p6_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[2]}", font=("Helvetica", 10))
        g10_p6_grade_label.grid(row=3, column=1)
        g10_p6_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[2], g10_p6_grade_label, 2, 10, gwa_label))
        g10_p6_add_button.grid(row=3, column=2)

        g10_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g10_math_label.grid(row=2, column=4)
        g10_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[3], g10_math_grade_label, 3, 10, gwa_label))
        g10_math_minus_button.grid(row=3, column=3)
        g10_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[3]}", font=("Helvetica", 10))
        g10_math_grade_label.grid(row=3, column=4)
        g10_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[3], g10_math_grade_label, 3, 10, gwa_label))
        g10_math_add_button.grid(row=3, column=5)

        g10_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g10_eng_label.grid(row=4, column=1)
        g10_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[4], g10_eng_grade_label, 4, 10, gwa_label))
        g10_eng_minus_button.grid(row=5, column=0, padx=(200, 0))
        g10_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[4]}", font=("Helvetica", 10))
        g10_eng_grade_label.grid(row=5, column=1)
        g10_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[4], g10_eng_grade_label, 4, 10, gwa_label))
        g10_eng_add_button.grid(row=5, column=2)

        g10_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g10_fil_label.grid(row=4, column=4)
        g10_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[5], g10_fil_grade_label, 5, 10, gwa_label))
        g10_fil_minus_button.grid(row=5, column=3)
        g10_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[5]}", font=("Helvetica", 10))
        g10_fil_grade_label.grid(row=5, column=4)
        g10_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[5], g10_fil_grade_label, 5, 10, gwa_label))
        g10_fil_add_button.grid(row=5, column=5)

        g10_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g10_ss_label.grid(row=6, column=1)
        g10_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[6], g10_ss_grade_label, 6, 10, gwa_label))
        g10_ss_minus_button.grid(row=7, column=0, padx=(200, 0))
        g10_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[6]}", font=("Helvetica", 10))
        g10_ss_grade_label.grid(row=7, column=1)
        g10_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[6], g10_ss_grade_label, 6, 10, gwa_label))
        g10_ss_add_button.grid(row=7, column=2)

        g10_pehm_label = tk.Label(self.window, text="PEHM", font=("Helvetica", 10))
        g10_pehm_label.grid(row=6, column=4)
        g10_pehm_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[7], g10_pehm_grade_label, 7, 10, gwa_label))
        g10_pehm_minus_button.grid(row=7, column=3)
        g10_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[7]}", font=("Helvetica", 10))
        g10_pehm_grade_label.grid(row=7, column=4)
        g10_pehm_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[7], g10_pehm_grade_label, 7, 10, gwa_label))
        g10_pehm_add_button.grid(row=7, column=5)

        g10_res_label = tk.Label(self.window, text="Research", font=("Helvetica", 10))
        g10_res_label.grid(row=8, column=1)
        g10_res_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[8], g10_res_grade_label, 8, 10, gwa_label))
        g10_res_minus_button.grid(row=9, column=0, padx=(200, 0))
        g10_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[8]}", font=("Helvetica", 10))
        g10_res_grade_label.grid(row=9, column=1)
        g10_res_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[8], g10_res_grade_label, 8, 10, gwa_label))
        g10_res_add_button.grid(row=9, column=2)

        g10_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10))
        g10_cs_label.grid(row=8, column=4)
        g10_cs_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g10_grades[9], g10_cs_grade_label, 9, 10, gwa_label))
        g10_cs_minus_button.grid(row=9, column=3)
        g10_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[9]}", font=("Helvetica", 10))
        g10_cs_grade_label.grid(row=9, column=4)
        g10_cs_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g10_grades[9], g10_cs_grade_label, 9, 10, gwa_label))
        g10_cs_add_button.grid(row=9, column=5)

        g10_buttons = [g10_bio_label, g10_bio_minus_button, g10_bio_grade_label, g10_bio_add_button,
                       g10_chem_label, g10_chem_minus_button, g10_chem_grade_label, g10_chem_add_button,
                       g10_p6_label, g10_p6_minus_button, g10_p6_grade_label, g10_p6_add_button,
                       g10_math_label, g10_math_minus_button, g10_math_grade_label, g10_math_add_button,
                       g10_eng_label, g10_eng_minus_button, g10_eng_grade_label, g10_eng_add_button,
                       g10_ss_label, g10_ss_minus_button, g10_ss_grade_label, g10_ss_add_button,
                       g10_pehm_label, g10_pehm_minus_button, g10_pehm_grade_label, g10_pehm_add_button,
                       g10_res_label, g10_res_minus_button, g10_res_grade_label, g10_res_add_button,
                       g10_cs_label, g10_cs_minus_button, g10_cs_grade_label, g10_cs_add_button,
                       back_button, save_gwa_button]

    def g11_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g11_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G11', CalculateButtons.g11_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 11 buttons
        g11_core_label = tk.Label(self.window, text="Core", font=("Helvetica", 10))
        g11_core_label.grid(row=0, column=1)
        g11_core_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[0], g11_core_grade_label, 0, 11, gwa_label))
        g11_core_minus_button.grid(row=1, column=0, padx=(200, 0))
        g11_core_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[0]}", font=("Helvetica", 10))
        g11_core_grade_label.grid(row=1, column=1)
        g11_core_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[0], g11_core_grade_label, 0, 11, gwa_label))
        g11_core_add_button.grid(row=1, column=2)

        g11_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g11_math_label.grid(row=0, column=4)
        g11_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[1], g11_math_grade_label, 1, 11, gwa_label))
        g11_math_minus_button.grid(row=1, column=3)
        g11_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[1]}", font=("Helvetica", 10))
        g11_math_grade_label.grid(row=1, column=4)
        g11_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[1], g11_math_grade_label, 1, 11, gwa_label))
        g11_math_add_button.grid(row=1, column=5)

        g11_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g11_eng_label.grid(row=2, column=1)
        g11_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[2], g11_eng_grade_label, 2, 11, gwa_label))
        g11_eng_minus_button.grid(row=3, column=0, padx=(200, 0))
        g11_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[2]}", font=("Helvetica", 10))
        g11_eng_grade_label.grid(row=3, column=1)
        g11_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[2], g11_eng_grade_label, 2, 11, gwa_label))
        g11_eng_add_button.grid(row=3, column=2)

        g11_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g11_fil_label.grid(row=2, column=4)
        g11_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[3], g11_fil_grade_label, 3, 11, gwa_label))
        g11_fil_minus_button.grid(row=3, column=3)
        g11_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[3]}", font=("Helvetica", 10))
        g11_fil_grade_label.grid(row=3, column=4)
        g11_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[3], g11_fil_grade_label, 3, 11, gwa_label))
        g11_fil_add_button.grid(row=3, column=5)

        g11_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g11_ss_label.grid(row=4, column=1)
        g11_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[4], g11_ss_grade_label, 4, 11, gwa_label))
        g11_ss_minus_button.grid(row=5, column=0, padx=(200, 0))
        g11_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[4]}", font=("Helvetica", 10))
        g11_ss_grade_label.grid(row=5, column=1)
        g11_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[4], g11_ss_grade_label, 4, 11, gwa_label))
        g11_ss_add_button.grid(row=5, column=2)

        g11_res_label = tk.Label(self.window, text="Research", font=("Helvetica", 10))
        g11_res_label.grid(row=4, column=4)
        g11_res_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[5], g11_res_grade_label, 5, 11, gwa_label))
        g11_res_minus_button.grid(row=5, column=3)
        g11_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[5]}", font=("Helvetica", 10))
        g11_res_grade_label.grid(row=5, column=4)
        g11_res_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[5], g11_res_grade_label, 5, 11, gwa_label))
        g11_res_add_button.grid(row=5, column=5)

        g11_elec_label = tk.Label(self.window, text="Elective", font=("Helvetica", 10))
        g11_elec_label.grid(row=6, column=1)
        g11_elec_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g11_grades[6], g11_elec_grade_label, 6, 11, gwa_label))
        g11_elec_minus_button.grid(row=7, column=0, padx=(200, 0))
        g11_elec_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[6]}", font=("Helvetica", 10))
        g11_elec_grade_label.grid(row=7, column=1)
        g11_elec_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g11_grades[6], g11_elec_grade_label, 6, 11, gwa_label))
        g11_elec_add_button.grid(row=7, column=2)

        g11_buttons = [g11_core_label, g11_core_minus_button, g11_core_grade_label, g11_core_add_button,
                       g11_math_label, g11_math_minus_button, g11_math_grade_label, g11_math_add_button,
                       g11_eng_label, g11_eng_minus_button, g11_eng_grade_label, g11_eng_add_button,
                       g11_fil_label, g11_fil_minus_button, g11_fil_grade_label, g11_fil_add_button,
                       g11_ss_label, g11_ss_minus_button, g11_ss_grade_label, g11_ss_add_button,
                       g11_res_label, g11_res_minus_button, g11_res_grade_label, g11_res_add_button,
                       g11_elec_label, g11_elec_minus_button, g11_elec_grade_label, g11_elec_add_button,
                       back_button, save_gwa_button]

    def g12_update(self):
        # Back button
        back_button = tk.Button(self.window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(1, g12_buttons, gwa_labels))
        back_button.place(x=10, y=20)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G12', CalculateButtons.g12_grades)
        save_gwa_button = save_gwa.save_button()

        # Grade 12 buttons
        g12_core_label = tk.Label(self.window, text="Core", font=("Helvetica", 10))
        g12_core_label.grid(row=0, column=1)
        g12_core_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[0], g12_core_grade_label, 0, 12, gwa_label))
        g12_core_minus_button.grid(row=1, column=0, padx=(200, 0))
        g12_core_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[0]}", font=("Helvetica", 10))
        g12_core_grade_label.grid(row=1, column=1)
        g12_core_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[0], g12_core_grade_label, 0, 12, gwa_label))
        g12_core_add_button.grid(row=1, column=2)

        g12_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10))
        g12_math_label.grid(row=0, column=4)
        g12_math_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[1], g12_math_grade_label, 1, 12, gwa_label))
        g12_math_minus_button.grid(row=1, column=3)
        g12_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[1]}", font=("Helvetica", 10))
        g12_math_grade_label.grid(row=1, column=4)
        g12_math_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[1], g12_math_grade_label, 1, 12, gwa_label))
        g12_math_add_button.grid(row=1, column=5)

        g12_eng_label = tk.Label(self.window, text="English", font=("Helvetica", 10))
        g12_eng_label.grid(row=2, column=1)
        g12_eng_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[2], g12_eng_grade_label, 2, 12, gwa_label))
        g12_eng_minus_button.grid(row=3, column=0, padx=(200, 0))
        g12_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[2]}", font=("Helvetica", 10))
        g12_eng_grade_label.grid(row=3, column=1)
        g12_eng_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[2], g12_eng_grade_label, 2, 12, gwa_label))
        g12_eng_add_button.grid(row=3, column=2)

        g12_fil_label = tk.Label(self.window, text="Filipino", font=("Helvetica", 10))
        g12_fil_label.grid(row=2, column=4)
        g12_fil_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[3], g12_fil_grade_label, 3, 12, gwa_label))
        g12_fil_minus_button.grid(row=3, column=3)
        g12_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[3]}", font=("Helvetica", 10))
        g12_fil_grade_label.grid(row=3, column=4)
        g12_fil_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[3], g12_fil_grade_label, 3, 12, gwa_label))
        g12_fil_add_button.grid(row=3, column=5)

        g12_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10))
        g12_ss_label.grid(row=4, column=1)
        g12_ss_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[4], g12_ss_grade_label, 4, 12, gwa_label))
        g12_ss_minus_button.grid(row=5, column=0, padx=(200, 0))
        g12_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[4]}", font=("Helvetica", 10))
        g12_ss_grade_label.grid(row=5, column=1)
        g12_ss_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[4], g12_ss_grade_label, 4, 12, gwa_label))
        g12_ss_add_button.grid(row=5, column=2)

        g12_res_label = tk.Label(self.window, text="Research", font=("Helvetica", 10))
        g12_res_label.grid(row=4, column=4)
        g12_res_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[5], g12_res_grade_label, 5, 12, gwa_label))
        g12_res_minus_button.grid(row=5, column=3)
        g12_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[5]}", font=("Helvetica", 10))
        g12_res_grade_label.grid(row=5, column=4)
        g12_res_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[5], g12_res_grade_label, 5, 12, gwa_label))
        g12_res_add_button.grid(row=5, column=5)

        g12_elec_label = tk.Label(self.window, text="Elective", font=("Helvetica", 10))
        g12_elec_label.grid(row=6, column=1)
        g12_elec_minus_button = tk.Button(self.window, text="-", font=("Helvetica", 10), command=lambda: self.grade_change('-', CalculateButtons.g12_grades[6], g12_elec_grade_label, 6, 12, gwa_label))
        g12_elec_minus_button.grid(row=7, column=0, padx=(200, 0))
        g12_elec_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[6]}", font=("Helvetica", 10))
        g12_elec_grade_label.grid(row=7, column=1)
        g12_elec_add_button = tk.Button(self.window, text="+", font=("Helvetica", 10), command=lambda: self.grade_change('+', CalculateButtons.g12_grades[6], g12_elec_grade_label, 6, 12, gwa_label))
        g12_elec_add_button.grid(row=7, column=2)

        g12_buttons = [g12_core_label, g12_core_minus_button, g12_core_grade_label, g12_core_add_button,
                       g12_math_label, g12_math_minus_button, g12_math_grade_label, g12_math_add_button,
                       g12_eng_label, g12_eng_minus_button, g12_eng_grade_label, g12_eng_add_button,
                       g12_fil_label, g12_fil_minus_button, g12_fil_grade_label, g12_fil_add_button,
                       g12_ss_label, g12_ss_minus_button, g12_ss_grade_label, g12_ss_add_button,
                       g12_res_label, g12_res_minus_button, g12_res_grade_label, g12_res_add_button,
                       g12_elec_label, g12_elec_minus_button, g12_elec_grade_label, g12_elec_add_button,
                       back_button, save_gwa_button]

    def grade_change(self, operation, grade, label, index, grade_level, gwa_label):
        if operation == '+':
            if grade < 5.0:
                grade += 0.25

                if grade_level == 7:
                    CalculateButtons.g7_grades[index] = grade
                    self.gwa_calculation(7, gwa_label)
                elif grade_level == 8:
                    CalculateButtons.g8_grades[index] = grade
                    self.gwa_calculation(8, gwa_label)
                elif grade_level == 9:
                    CalculateButtons.g9_grades[index] = grade
                    self.gwa_calculation(9, gwa_label)
                elif grade_level == 10:
                    CalculateButtons.g10_grades[index] = grade
                    self.gwa_calculation(10, gwa_label)
                elif grade_level == 11:
                    CalculateButtons.g11_grades[index] = grade
                    self.gwa_calculation(11, gwa_label)
                elif grade_level == 12:
                    CalculateButtons.g12_grades[index] = grade
                    self.gwa_calculation(12, gwa_label)

                label.config(text=f"{grade}", font=("Helvetica", 10))
        elif operation == '-':
            if grade > 1.0:
                grade -= 0.25

                if grade_level == 7:
                    CalculateButtons.g7_grades[index] = grade
                    self.gwa_calculation(7, gwa_label)
                elif grade_level == 8:
                    CalculateButtons.g8_grades[index] = grade
                    self.gwa_calculation(8, gwa_label)
                elif grade_level == 9:
                    CalculateButtons.g9_grades[index] = grade
                    self.gwa_calculation(9, gwa_label)
                elif grade_level == 10:
                    CalculateButtons.g10_grades[index] = grade
                    self.gwa_calculation(10, gwa_label)
                elif grade_level == 11:
                    CalculateButtons.g11_grades[index] = grade
                    self.gwa_calculation(11, gwa_label)
                elif grade_level == 12:
                    CalculateButtons.g12_grades[index] = grade
                    self.gwa_calculation(12, gwa_label)

                label.config(text=f"{grade}", font=("Helvetica", 10))

    def gwa_calculation(self, grade_level, gwa_label=None):

        if grade_level == 'creation':
            gwa_title_label = tk.Label(self.window, text="GWA", font=("Helvetica", 10))
            gwa_title_label.place(x=10, y=100)

            gwa_label = tk.Label(self.window, text=f'{1.00}', font=("Helvetica", 10))
            gwa_label.place(x=10, y=130)

            return gwa_title_label, gwa_label

        elif grade_level == 7:
            gwa_grade_7 = (CalculateButtons.g7_grades[0]) * 1.7 + (CalculateButtons.g7_grades[1] * 1.7) + \
                          (CalculateButtons.g7_grades[2] * 1.3) + (CalculateButtons.g7_grades[3] * 1.0) + \
                          (CalculateButtons.g7_grades[4] * 1.0) + (CalculateButtons.g7_grades[5] * 1.0) + \
                          (CalculateButtons.g7_grades[6] * 0.7) + (CalculateButtons.g7_grades[7] * 1.0) + \
                          (CalculateButtons.g7_grades[8] * 1.0)

            gwa_grade_7 = str(round((gwa_grade_7 / 10.4), 3))

            if len(gwa_grade_7) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_7))
                gwa_grade_7 = gwa_grade_7 + trailing_zero

            gwa_label.config(text=gwa_grade_7)

        elif grade_level == 8:
            gwa_grade_8 = (CalculateButtons.g8_grades[0] * 2.0) + (CalculateButtons.g8_grades[1] * 1.7) + \
                          (CalculateButtons.g8_grades[2] * 1.3) + (CalculateButtons.g8_grades[3] * 1.0) + \
                          (CalculateButtons.g8_grades[4] * 1.0) + (CalculateButtons.g8_grades[5] * 1.0) + \
                          (CalculateButtons.g8_grades[6] * 0.7) + (CalculateButtons.g8_grades[7] * 1.0) + \
                          (CalculateButtons.g8_grades[8] * 1.0) + (CalculateButtons.g8_grades[9] * 0.7)

            gwa_grade_8 = str(round((gwa_grade_8 / 11.4), 3))

            if len(gwa_grade_8) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_8))
                gwa_grade_8 = gwa_grade_8 + trailing_zero

            gwa_label.config(text=gwa_grade_8)

        elif grade_level == 9:
            gwa_grade_9 = (CalculateButtons.g9_grades[0] * 1.0) + (CalculateButtons.g9_grades[1] * 1.0) + \
                          (CalculateButtons.g9_grades[2] * 1.0) + (CalculateButtons.g9_grades[3] * 1.0) + \
                          (CalculateButtons.g9_grades[4] * 1.0) + (CalculateButtons.g9_grades[5] * 1.0) + \
                          (CalculateButtons.g9_grades[6] * 1.0) + (CalculateButtons.g9_grades[7] * 1.0) + \
                          (CalculateButtons.g9_grades[8] * 1.0) + (CalculateButtons.g9_grades[9] * 1.0)

            gwa_grade_9 = str(round((gwa_grade_9 / 10.0), 3))

            if len(gwa_grade_9) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_9))
                gwa_grade_9 = gwa_grade_9 + trailing_zero

            gwa_label.config(text=gwa_grade_9)

        elif grade_level == 10:
            gwa_grade_10 = (CalculateButtons.g10_grades[0] * 1.0) + (CalculateButtons.g10_grades[1] * 1.0) + \
                          (CalculateButtons.g10_grades[2] * 1.0) + (CalculateButtons.g10_grades[3] * 1.3) + \
                          (CalculateButtons.g10_grades[4] * 1.0) + (CalculateButtons.g10_grades[5] * 1.0) + \
                          (CalculateButtons.g10_grades[6] * 1.0) + (CalculateButtons.g10_grades[7] * 1.0) + \
                          (CalculateButtons.g10_grades[8] * 1.0) + (CalculateButtons.g10_grades[9] * 1.0)

            gwa_grade_10 = str(round((gwa_grade_10 / 10.3), 3))

            if len(gwa_grade_10) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_10))
                gwa_grade_10 = gwa_grade_10 + trailing_zero

            gwa_label.config(text=gwa_grade_10)

        elif grade_level == 11:
            gwa_grade_11 = (CalculateButtons.g11_grades[0] * 1.7) + (CalculateButtons.g11_grades[1] * 1.0) + \
                          (CalculateButtons.g11_grades[2] * 1.0) + (CalculateButtons.g11_grades[3] * 1.0) + \
                          (CalculateButtons.g11_grades[4] * 1.0) + (CalculateButtons.g11_grades[5] * 2.0) + \
                          (CalculateButtons.g11_grades[6] * 1.7)

            gwa_grade_11 = str(round((gwa_grade_11 / 9.4), 3))

            if len(gwa_grade_11) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_11))
                gwa_grade_11 = gwa_grade_11 + trailing_zero

            gwa_label.config(text=gwa_grade_11)

        elif grade_level == 12:
            gwa_grade_12 = (CalculateButtons.g12_grades[0] * 1.7) + (CalculateButtons.g12_grades[1] * 1.0) + \
                           (CalculateButtons.g12_grades[2] * 1.0) + (CalculateButtons.g12_grades[3] * 1.0) + \
                           (CalculateButtons.g12_grades[4] * 1.0) + (CalculateButtons.g12_grades[5] * 2.0) + \
                           (CalculateButtons.g12_grades[6] * 1.7)

            gwa_grade_12 = str(round((gwa_grade_12 / 9.4), 3))

            if len(gwa_grade_12) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_12))
                gwa_grade_12 = gwa_grade_12 + trailing_zero

            gwa_label.config(text=gwa_grade_12)


class SaveGWA:
    def __init__(self, window, grade_level=None, grades=None, state=None):
        self.window = window

        self.grade_level = grade_level
        self.grades = grades

    def save_button(self):
        # Save button
        save_button = tk.Button(self.window, text="Save", font=("Helvetica", 15), command=lambda: self.save_to_csv())
        save_button.place(x=10, y=200)
        return save_button

    def save_to_csv(self):
        with open('data.csv', 'a', newline='\n', encoding='utf-8') as csv_file:
            csv_write = csv.writer(csv_file, delimiter=',')

            self.grades.insert(0, self.grade_level)

            csv_write.writerow(self.grades)

            self.grades.pop(0)

        print('saved')


class AboutThisApp:
    def __init__(self, window):
        # Back button
        self.back_button = tk.Button(window, text="←", font=("Helvetica", 15), command=lambda: self.back_decision(widget_list))
        self.back_button.place(x=10, y=20)

        # Text
        self.window = window
        about_me = tk.Label(window, text="About this app", font=("Helvetica", 20), bg='black', fg='white')
        about_me.place(x=75, y=25)

        app_description = tk.Label(window, text="This is an application for the PSHS grading system", font=("Helvetica", 14), bg='black', fg='white')
        app_description.place(x=100, y=100)

        app_description2 = tk.Label(window, text="that includes storage of GWA (General Weighted", font=("Helvetica", 14), bg='black', fg='white')
        app_description2.place(x=100, y=125)

        app_description3 = tk.Label(window, text="Average), and GWA calculation for all grade levels.", font=("Helvetica", 14), bg='black', fg='white')
        app_description3.place(x=100, y=150)

        created_by = tk.Label(window, text="xbryan25", font=("Helvetica", 15), bg='black', fg='white')
        created_by.place(x=425, y=225)

        version = tk.Label(window, text="v(u) (06-26-22)", font=("Helvetica", 15), bg='black', fg='white')
        version.place(x=425, y=250)

        # GitHub picture
        github_pic = tk.PhotoImage(file='github.png')
        github_label = tk.Label(window, image=github_pic, width=24, height=24, fg='white')
        github_label.image = github_pic
        github_label.place(x=395, y=225)

        # Widget list
        widget_list = [about_me, app_description, app_description2, app_description3, created_by,
                       version, github_label]

    def back_decision(self, widget_list):
        for widget in widget_list:
            widget.destroy()
        self.back_button.destroy()

        IntroButtons(self.window)
