import tkinter as tk
from button_hover import ButtonHover
from save_and_import import SaveGWA
from save_and_import import ImportGWA


class IntroButtons:
    def __init__(self, window):
        # Intro buttons
        self.window = window
        self.calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 25),
                                          command=lambda: self.intro_decision('calculate'),
                                          activebackground='#9F9E9D')
        self.calculate_button.grid(row=0, padx=(220, 0), pady=(120, 60))

        calculate_button_hover = ButtonHover(self.calculate_button, 'calculate')
        self.calculate_button.bind('<Enter>', calculate_button_hover.on_enter)
        self.calculate_button.bind('<Leave>', calculate_button_hover.on_leave)

        self.credits_button = tk.Button(window, text="About this app", font=("Helvetica", 15),
                                        command=lambda: self.intro_decision('about_this_app'),
                                        activebackground='#9F9E9D')
        self.credits_button.grid(row=1, padx=(60, 100), column=1)

        credits_button_hover = ButtonHover(self.credits_button, 'credits')
        self.credits_button.bind('<Enter>', credits_button_hover.on_enter)
        self.credits_button.bind('<Leave>', credits_button_hover.on_leave)

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

    def __init__(self, window):
        self.window = window

        # Window configuration
        self.window.config(bg='#A6A6A6')

        # Back button
        self.back_button = tk.Button(window, text="←", font=("Helvetica", 15),
                                     command=lambda: self.back_decision(0),
                                     activebackground='#DB5F44')
        self.back_button.place(x=10, y=20)

        back_button_hover = ButtonHover(self.back_button, 'back_button')
        self.back_button.bind('<Enter>', back_button_hover.on_enter)
        self.back_button.bind('<Leave>', back_button_hover.on_leave)

        # Grade levels
        self.g7_button = tk.Button(window, text="Grade 7  ", font=("Helvetica", 20),
                                   command=lambda: self.grade_decision('7'),
                                   activebackground='#9F9E9D')
        self.g7_button.grid(row=1, padx=(90, 100), pady=20)

        g7_button_hover = ButtonHover(self.g7_button, 'grade_level_button')
        self.g7_button.bind('<Enter>', g7_button_hover.on_enter)
        self.g7_button.bind('<Leave>', g7_button_hover.on_leave)

        self.g8_button = tk.Button(window, text="Grade 8  ", font=("Helvetica", 20),
                                   command=lambda: self.grade_decision('8'),
                                   activebackground='#9F9E9D')
        self.g8_button.grid(row=1, padx=(30, 100), column=1)

        g8_button_hover = ButtonHover(self.g8_button, 'grade_level_button')
        self.g8_button.bind('<Enter>', g8_button_hover.on_enter)
        self.g8_button.bind('<Leave>', g8_button_hover.on_leave)

        self.g9_button = tk.Button(window, text="Grade 9  ", font=("Helvetica", 20),
                                   command=lambda: self.grade_decision('9'),
                                   activebackground='#9F9E9D')
        self.g9_button.grid(row=2, padx=(90, 100), pady=20)

        g9_button_hover = ButtonHover(self.g9_button, 'grade_level_button')
        self.g9_button.bind('<Enter>', g9_button_hover.on_enter)
        self.g9_button.bind('<Leave>', g9_button_hover.on_leave)

        self.g10_button = tk.Button(window, text="Grade 10", font=("Helvetica", 20),
                                    command=lambda: self.grade_decision('10'),
                                    activebackground='#9F9E9D')
        self.g10_button.grid(row=2, padx=(35, 100), column=1)

        g10_button_hover = ButtonHover(self.g10_button, 'grade_level_button')
        self.g10_button.bind('<Enter>', g10_button_hover.on_enter)
        self.g10_button.bind('<Leave>', g10_button_hover.on_leave)

        self.g11_button = tk.Button(window, text="Grade 11", font=("Helvetica", 20),
                                    command=lambda: self.grade_decision('11'),
                                    activebackground='#9F9E9D')
        self.g11_button.grid(row=3, padx=(90, 100), pady=20)

        g11_button_hover = ButtonHover(self.g11_button, 'grade_level_button')
        self.g11_button.bind('<Enter>', g11_button_hover.on_enter)
        self.g11_button.bind('<Leave>', g11_button_hover.on_leave)

        self.g12_button = tk.Button(window, text="Grade 12", font=("Helvetica", 20),
                                    command=lambda: self.grade_decision('12'),
                                    activebackground='#9F9E9D')
        self.g12_button.grid(row=3, padx=(35, 100), column=1)

        g12_button_hover = ButtonHover(self.g12_button, 'grade_level_button')
        self.g12_button.bind('<Enter>', g12_button_hover.on_enter)
        self.g12_button.bind('<Leave>', g12_button_hover.on_leave)

        # GWA placeholder for display
        self.display_gwa = 1.0

    def back_decision(self, state, widgets=None, gwa_labels=None, save_gwa_widgets=None):
        if state == 0:
            self.back_button.destroy()
            self.g7_button.destroy()
            self.g8_button.destroy()
            self.g9_button.destroy()
            self.g10_button.destroy()
            self.g11_button.destroy()
            self.g12_button.destroy()
            self.window.config(bg='black')
            IntroButtons(self.window)
        elif state == 1:
            self.window.config(bg='white')
            for widget in widgets:
                widget.destroy()

            if gwa_labels is not None:
                for gwa_label in gwa_labels:
                    gwa_label.destroy()

            if save_gwa_widgets is not None:
                for save_gwa_widget in save_gwa_widgets:
                    save_gwa_widget.destroy()

            CalculateButtons.g7_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g8_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g9_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g10_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g11_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            CalculateButtons.g12_grades = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

            CalculateButtons(self.window)
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
        self.window.config(bg='#FFF0C6')

        # Back button
        back_button_g7 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                   command=lambda: self.back_decision(1, g7_buttons, gwa_labels),
                                   activebackground='#DB5F44')
        back_button_g7.place(x=10, y=20)

        back_button_g7_hover = ButtonHover(back_button_g7, 'back_button')
        back_button_g7.bind('<Enter>', back_button_g7_hover.on_enter)
        back_button_g7.bind('<Leave>', back_button_g7_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 7 buttons

        # Integrated Science
        g7_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g7_is_label.grid(row=0, column=1, pady=(15, 0))

        g7_is_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g7_grades[0],
                                                                         g7_is_grade_label, 0, 7, gwa_label),
                                       activebackground='#DB5F44')
        g7_is_minus_button.grid(row=1, column=0, padx=(200, 0))

        is_minus_button_hover = ButtonHover(g7_is_minus_button, 'subject_button', 'minus')
        g7_is_minus_button.bind('<Enter>', is_minus_button_hover.on_enter)
        g7_is_minus_button.bind('<Leave>', is_minus_button_hover.on_leave)

        g7_is_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[0]}", font=("Helvetica", 10))
        g7_is_grade_label.grid(row=1, column=1, pady=5)

        g7_is_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g7_grades[0],
                                                                       g7_is_grade_label, 0, 7, gwa_label),
                                     activebackground='#67C735')
        g7_is_add_button.grid(row=1, column=2, padx=(0, 25))

        is_add_button_hover = ButtonHover(g7_is_add_button, 'subject_button', 'add')
        g7_is_add_button.bind('<Enter>', is_add_button_hover.on_enter)
        g7_is_add_button.bind('<Leave>', is_add_button_hover.on_leave)

        # Mathematics
        g7_math_label = tk.Label(self.window, text=" Mathematics ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g7_math_label.grid(row=0, column=4, pady=(15, 0))
        g7_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g7_grades[1],
                                                                           g7_math_grade_label, 1, 7, gwa_label),
                                         activebackground='#DB5F44')
        g7_math_minus_button.grid(row=1, column=3)

        math_minus_button_hover = ButtonHover(g7_math_minus_button, 'subject_button', 'minus')
        g7_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g7_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g7_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[1]}", font=("Helvetica", 10))
        g7_math_grade_label.grid(row=1, column=4, pady=5)
        g7_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g7_grades[1],
                                                                         g7_math_grade_label, 1, 7, gwa_label),
                                       activebackground='#67C735')
        g7_math_add_button.grid(row=1, column=5)

        math_add_button_hover = ButtonHover(g7_math_add_button, 'subject_button', 'add')
        g7_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g7_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g7_eng_label = tk.Label(self.window, text="         English        ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g7_eng_label.grid(row=2, column=1)
        g7_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g7_grades[2],
                                                                          g7_eng_grade_label, 2, 7, gwa_label),
                                        activebackground='#DB5F44')
        g7_eng_minus_button.grid(row=3, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g7_eng_minus_button, 'subject_button', 'minus')
        g7_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g7_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g7_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[2]}", font=("Helvetica", 10))
        g7_eng_grade_label.grid(row=3, column=1, pady=5)
        g7_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g7_grades[2],
                                                                        g7_eng_grade_label, 2, 7, gwa_label),
                                      activebackground='#67C735')
        g7_eng_add_button.grid(row=3, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g7_eng_add_button, 'subject_button', 'add')
        g7_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g7_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g7_fil_label = tk.Label(self.window, text="     Filipino     ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g7_fil_label.grid(row=2, column=4)

        g7_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g7_grades[3],
                                                                          g7_fil_grade_label, 3, 7, gwa_label),
                                        activebackground='#DB5F44')
        g7_fil_minus_button.grid(row=3, column=3)

        fil_minus_button_hover = ButtonHover(g7_fil_minus_button, 'subject_button', 'minus')
        g7_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g7_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g7_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[3]}", font=("Helvetica", 10))
        g7_fil_grade_label.grid(row=3, column=4, pady=5)
        g7_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g7_grades[3],
                                                                        g7_fil_grade_label, 3, 7, gwa_label),
                                      activebackground='#67C735')
        g7_fil_add_button.grid(row=3, column=5)

        fil_add_button_hover = ButtonHover(g7_fil_add_button, 'subject_button', 'add')
        g7_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g7_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g7_ss_label = tk.Label(self.window, text="   Social Science   ", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g7_ss_label.grid(row=4, column=1)

        g7_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g7_grades[4],
                                                                         g7_ss_grade_label, 4, 7, gwa_label),
                                       activebackground='#DB5F44')
        g7_ss_minus_button.grid(row=5, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g7_ss_minus_button, 'subject_button', 'minus')
        g7_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g7_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g7_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[4]}", font=("Helvetica", 10))
        g7_ss_grade_label.grid(row=5, column=1, pady=5)
        g7_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g7_grades[4],
                                                                       g7_ss_grade_label, 4, 7, gwa_label),
                                     activebackground='#67C735')
        g7_ss_add_button.grid(row=5, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g7_ss_add_button, 'subject_button', 'add')
        g7_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g7_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # PEHM
        g7_pehm_label = tk.Label(self.window, text="     PEHM     ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g7_pehm_label.grid(row=4, column=4)

        g7_pehm_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g7_grades[5],
                                                                           g7_pehm_grade_label, 5, 7, gwa_label),
                                         activebackground='#DB5F44')
        g7_pehm_minus_button.grid(row=5, column=3)

        pehm_minus_button_hover = ButtonHover(g7_pehm_minus_button, 'subject_button', 'minus')
        g7_pehm_minus_button.bind('<Enter>', pehm_minus_button_hover.on_enter)
        g7_pehm_minus_button.bind('<Leave>', pehm_minus_button_hover.on_leave)

        g7_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[5]}", font=("Helvetica", 10))
        g7_pehm_grade_label.grid(row=5, column=4, pady=5)
        g7_pehm_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g7_grades[5],
                                                                         g7_pehm_grade_label, 5, 7, gwa_label),
                                       activebackground='#67C735')
        g7_pehm_add_button.grid(row=5, column=5)

        pehm_add_button_hover = ButtonHover(g7_pehm_add_button, 'subject_button', 'add')
        g7_pehm_add_button.bind('<Enter>', pehm_add_button_hover.on_enter)
        g7_pehm_add_button.bind('<Leave>', pehm_add_button_hover.on_leave)

        # Values Education
        g7_valed_label = tk.Label(self.window, text=" Values Education ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g7_valed_label.grid(row=6, column=1)

        g7_valed_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g7_grades[6],
                                                                            g7_valed_grade_label, 6, 7, gwa_label),
                                          activebackground='#DB5F44')
        g7_valed_minus_button.grid(row=7, column=0, padx=(200, 0))

        valed_minus_button_hover = ButtonHover(g7_valed_minus_button, 'subject_button', 'minus')
        g7_valed_minus_button.bind('<Enter>', valed_minus_button_hover.on_enter)
        g7_valed_minus_button.bind('<Leave>', valed_minus_button_hover.on_leave)

        g7_valed_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[6]}", font=("Helvetica", 10))
        g7_valed_grade_label.grid(row=7, column=1, pady=5)
        g7_valed_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g7_grades[6],
                                                                          g7_valed_grade_label, 6, 7, gwa_label),
                                        activebackground='#67C735')
        g7_valed_add_button.grid(row=7, column=2, padx=(0, 25))

        valed_add_button_hover = ButtonHover(g7_valed_add_button, 'subject_button', 'add')
        g7_valed_add_button.bind('<Enter>', valed_add_button_hover.on_enter)
        g7_valed_add_button.bind('<Leave>', valed_add_button_hover.on_leave)

        # Adtech
        g7_adtech_label = tk.Label(self.window, text="   ADTECH   ", font=("Helvetica", 10), borderwidth=2,
                                   relief='groove')
        g7_adtech_label.grid(row=6, column=4)

        g7_adtech_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                           command=lambda: self.grade_change('-', CalculateButtons.g7_grades[7],
                                                                             g7_adtech_grade_label, 7, 7, gwa_label),
                                           activebackground='#DB5F44')
        g7_adtech_minus_button.grid(row=7, column=3)

        adtech_minus_button_hover = ButtonHover(g7_adtech_minus_button, 'subject_button', 'minus')
        g7_adtech_minus_button.bind('<Enter>', adtech_minus_button_hover.on_enter)
        g7_adtech_minus_button.bind('<Leave>', adtech_minus_button_hover.on_leave)

        g7_adtech_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[7]}", font=("Helvetica", 10))
        g7_adtech_grade_label.grid(row=7, column=4, pady=5)
        g7_adtech_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('+', CalculateButtons.g7_grades[7],
                                                                           g7_adtech_grade_label, 7, 7, gwa_label),
                                         activebackground='#67C735')
        g7_adtech_add_button.grid(row=7, column=5)

        adtech_add_button_hover = ButtonHover(g7_adtech_add_button, 'subject_button', 'add')
        g7_adtech_add_button.bind('<Enter>', adtech_add_button_hover.on_enter)
        g7_adtech_add_button.bind('<Leave>', adtech_add_button_hover.on_leave)

        # Computer Science
        g7_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g7_cs_label.grid(row=8, column=1)

        g7_cs_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g7_grades[8],
                                                                         g7_cs_grade_label, 8, 7, gwa_label),
                                       activebackground='#DB5F44')
        g7_cs_minus_button.grid(row=9, column=0, padx=(200, 0))

        cs_minus_button_hover = ButtonHover(g7_cs_minus_button, 'subject_button', 'minus')
        g7_cs_minus_button.bind('<Enter>', cs_minus_button_hover.on_enter)
        g7_cs_minus_button.bind('<Leave>', cs_minus_button_hover.on_leave)

        g7_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g7_grades[8]}", font=("Helvetica", 10))
        g7_cs_grade_label.grid(row=9, column=1, pady=5)
        g7_cs_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g7_grades[8],
                                                                       g7_cs_grade_label, 8, 7, gwa_label),
                                     activebackground='#67C735')
        g7_cs_add_button.grid(row=9, column=2, padx=(0, 25))

        cs_add_button_hover = ButtonHover(g7_cs_add_button, 'subject_button', 'add')
        g7_cs_add_button.bind('<Enter>', cs_add_button_hover.on_enter)
        g7_cs_add_button.bind('<Leave>', cs_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G7', CalculateButtons.g7_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g7_is_grade_label, g7_math_grade_label, g7_eng_grade_label, g7_fil_grade_label,
                             g7_ss_grade_label, g7_pehm_grade_label, g7_valed_grade_label, g7_adtech_grade_label,
                             g7_cs_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G7', CalculateButtons.g7_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

        g7_buttons = [g7_is_label, g7_is_minus_button, g7_is_grade_label, g7_is_add_button,
                      g7_math_label, g7_math_minus_button, g7_math_grade_label, g7_math_add_button,
                      g7_eng_label, g7_eng_minus_button, g7_eng_grade_label, g7_eng_add_button,
                      g7_fil_label, g7_fil_minus_button, g7_fil_grade_label, g7_fil_add_button,
                      g7_ss_label, g7_ss_minus_button, g7_ss_grade_label, g7_ss_add_button,
                      g7_pehm_label, g7_pehm_minus_button, g7_pehm_grade_label, g7_pehm_add_button,
                      g7_valed_label, g7_valed_minus_button, g7_valed_grade_label, g7_valed_add_button,
                      g7_adtech_label, g7_adtech_minus_button, g7_adtech_grade_label, g7_adtech_add_button,
                      g7_cs_label, g7_cs_minus_button, g7_cs_grade_label, g7_cs_add_button,
                      back_button_g7, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def g8_update(self):
        self.window.config(bg='#D2EF9C')

        # Back button
        back_button_g8 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                   command=lambda: self.back_decision(1, g8_buttons, gwa_labels),
                                   activebackground='#DB5F44')
        back_button_g8.place(x=10, y=20)

        back_button_g8_hover = ButtonHover(back_button_g8, 'back_button')
        back_button_g8.bind('<Enter>', back_button_g8_hover.on_enter)
        back_button_g8.bind('<Leave>', back_button_g8_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 8 buttons

        # Integrated Science
        g8_is_label = tk.Label(self.window, text="Integrated Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g8_is_label.grid(row=0, column=1, pady=(15, 0))

        g8_is_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g8_grades[0],
                                                                         g8_is_grade_label, 0, 8, gwa_label),
                                       activebackground='#DB5F44')
        g8_is_minus_button.grid(row=1, column=0, padx=(200, 0))

        is_minus_button_hover = ButtonHover(g8_is_minus_button, 'subject_button', 'minus')
        g8_is_minus_button.bind('<Enter>', is_minus_button_hover.on_enter)
        g8_is_minus_button.bind('<Leave>', is_minus_button_hover.on_leave)

        g8_is_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[0]}", font=("Helvetica", 10))
        g8_is_grade_label.grid(row=1, column=1, pady=5)

        g8_is_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g8_grades[0],
                                                                       g8_is_grade_label, 0, 8, gwa_label),
                                     activebackground='#67C735')
        g8_is_add_button.grid(row=1, column=2, padx=(0, 25))

        is_add_button_hover = ButtonHover(g8_is_add_button, 'subject_button', 'add')
        g8_is_add_button.bind('<Enter>', is_add_button_hover.on_enter)
        g8_is_add_button.bind('<Leave>', is_add_button_hover.on_leave)

        # Mathematics
        g8_math_label = tk.Label(self.window, text=" Mathematics ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g8_math_label.grid(row=0, column=4, pady=(15, 0))
        g8_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g8_grades[1],
                                                                           g8_math_grade_label, 1, 8, gwa_label),
                                         activebackground='#DB5F44')
        g8_math_minus_button.grid(row=1, column=3)

        math_minus_button_hover = ButtonHover(g8_math_minus_button, 'subject_button', 'minus')
        g8_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g8_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g8_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[1]}", font=("Helvetica", 10))
        g8_math_grade_label.grid(row=1, column=4, pady=5)

        g8_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g8_grades[1],
                                                                         g8_math_grade_label, 1, 8, gwa_label),
                                       activebackground='#67C735')
        g8_math_add_button.grid(row=1, column=5)

        math_add_button_hover = ButtonHover(g8_math_add_button, 'subject_button', 'add')
        g8_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g8_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g8_eng_label = tk.Label(self.window, text="         English        ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g8_eng_label.grid(row=2, column=1)

        g8_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g8_grades[2],
                                                                          g8_eng_grade_label, 2, 8, gwa_label),
                                        activebackground='#DB5F44')
        g8_eng_minus_button.grid(row=3, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g8_eng_minus_button, 'subject_button', 'minus')
        g8_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g8_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g8_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[2]}", font=("Helvetica", 10))
        g8_eng_grade_label.grid(row=3, column=1, pady=5)

        g8_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g8_grades[2],
                                                                        g8_eng_grade_label, 2, 8, gwa_label),
                                      activebackground='#67C735')
        g8_eng_add_button.grid(row=3, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g8_eng_add_button, 'subject_button', 'add')
        g8_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g8_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g8_fil_label = tk.Label(self.window, text="     Filipino     ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g8_fil_label.grid(row=2, column=4)

        g8_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g8_grades[3],
                                                                          g8_fil_grade_label, 3, 8, gwa_label),
                                        activebackground='#DB5F44')
        g8_fil_minus_button.grid(row=3, column=3)

        fil_minus_button_hover = ButtonHover(g8_fil_minus_button, 'subject_button', 'minus')
        g8_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g8_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g8_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[3]}", font=("Helvetica", 10))
        g8_fil_grade_label.grid(row=3, column=4, pady=5)

        g8_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g8_grades[3],
                                                                        g8_fil_grade_label, 3, 8, gwa_label),
                                      activebackground='#67C735')
        g8_fil_add_button.grid(row=3, column=5)

        fil_add_button_hover = ButtonHover(g8_fil_add_button, 'subject_button', 'add')
        g8_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g8_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g8_ss_label = tk.Label(self.window, text="   Social Science   ", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g8_ss_label.grid(row=4, column=1)

        g8_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g8_grades[4],
                                                                         g8_ss_grade_label, 4, 8, gwa_label),
                                       activebackground='#DB5F44')
        g8_ss_minus_button.grid(row=5, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g8_ss_minus_button, 'subject_button', 'minus')
        g8_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g8_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g8_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[4]}", font=("Helvetica", 10))
        g8_ss_grade_label.grid(row=5, column=1, pady=5)

        g8_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g8_grades[4],
                                                                       g8_ss_grade_label, 4, 8, gwa_label),
                                     activebackground='#67C735')
        g8_ss_add_button.grid(row=5, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g8_ss_add_button, 'subject_button', 'add')
        g8_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g8_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # PEHM
        g8_pehm_label = tk.Label(self.window, text="     PEHM     ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g8_pehm_label.grid(row=4, column=4)

        g8_pehm_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g8_grades[5],
                                                                           g8_pehm_grade_label, 5, 8, gwa_label),
                                         activebackground='#DB5F44')
        g8_pehm_minus_button.grid(row=5, column=3)

        pehm_minus_button_hover = ButtonHover(g8_pehm_minus_button, 'subject_button', 'minus')
        g8_pehm_minus_button.bind('<Enter>', pehm_minus_button_hover.on_enter)
        g8_pehm_minus_button.bind('<Leave>', pehm_minus_button_hover.on_leave)

        g8_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[5]}", font=("Helvetica", 10))
        g8_pehm_grade_label.grid(row=5, column=4, pady=5)

        g8_pehm_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g8_grades[5],
                                                                         g8_pehm_grade_label, 5, 8, gwa_label),
                                       activebackground='#67C735')
        g8_pehm_add_button.grid(row=5, column=5)

        pehm_add_button_hover = ButtonHover(g8_pehm_add_button, 'subject_button', 'add')
        g8_pehm_add_button.bind('<Enter>', pehm_add_button_hover.on_enter)
        g8_pehm_add_button.bind('<Leave>', pehm_add_button_hover.on_leave)

        # Values Education
        g8_valed_label = tk.Label(self.window, text=" Values Education ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g8_valed_label.grid(row=6, column=1)

        g8_valed_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g8_grades[6],
                                                                            g8_valed_grade_label, 6, 8, gwa_label),
                                          activebackground='#DB5F44')
        g8_valed_minus_button.grid(row=7, column=0, padx=(200, 0))

        valed_minus_button_hover = ButtonHover(g8_valed_minus_button, 'subject_button', 'minus')
        g8_valed_minus_button.bind('<Enter>', valed_minus_button_hover.on_enter)
        g8_valed_minus_button.bind('<Leave>', valed_minus_button_hover.on_leave)

        g8_valed_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[6]}", font=("Helvetica", 10))
        g8_valed_grade_label.grid(row=7, column=1, pady=5)

        g8_valed_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g8_grades[6],
                                                                          g8_valed_grade_label, 6, 8, gwa_label),
                                        activebackground='#67C735')
        g8_valed_add_button.grid(row=7, column=2, padx=(0, 25))

        valed_add_button_hover = ButtonHover(g8_valed_add_button, 'subject_button', 'add')
        g8_valed_add_button.bind('<Enter>', valed_add_button_hover.on_enter)
        g8_valed_add_button.bind('<Leave>', valed_add_button_hover.on_leave)

        # Adtech
        g8_adtech_label = tk.Label(self.window, text="   ADTECH  ", font=("Helvetica", 10), borderwidth=2,
                                   relief='groove')
        g8_adtech_label.grid(row=6, column=4)

        g8_adtech_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                           command=lambda: self.grade_change('-', CalculateButtons.g8_grades[7],
                                                                             g8_adtech_grade_label, 7, 8, gwa_label),
                                           activebackground='#DB5F44')
        g8_adtech_minus_button.grid(row=7, column=3)

        adtech_minus_button_hover = ButtonHover(g8_adtech_minus_button, 'subject_button', 'minus')
        g8_adtech_minus_button.bind('<Enter>', adtech_minus_button_hover.on_enter)
        g8_adtech_minus_button.bind('<Leave>', adtech_minus_button_hover.on_leave)

        g8_adtech_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[7]}", font=("Helvetica", 10))
        g8_adtech_grade_label.grid(row=7, column=4, pady=5)

        g8_adtech_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('+', CalculateButtons.g8_grades[7],
                                                                           g8_adtech_grade_label, 7, 8, gwa_label),
                                         activebackground='#67C735')
        g8_adtech_add_button.grid(row=7, column=5)

        adtech_add_button_hover = ButtonHover(g8_adtech_add_button, 'subject_button', 'add')
        g8_adtech_add_button.bind('<Enter>', adtech_add_button_hover.on_enter)
        g8_adtech_add_button.bind('<Leave>', adtech_add_button_hover.on_leave)

        # Computer Science
        g8_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g8_cs_label.grid(row=8, column=1)

        g8_cs_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g8_grades[8],
                                                                         g8_cs_grade_label, 8, 8, gwa_label),
                                       activebackground='#DB5F44')
        g8_cs_minus_button.grid(row=9, column=0, padx=(200, 0))

        cs_minus_button_hover = ButtonHover(g8_cs_minus_button, 'subject_button', 'minus')
        g8_cs_minus_button.bind('<Enter>', cs_minus_button_hover.on_enter)
        g8_cs_minus_button.bind('<Leave>', cs_minus_button_hover.on_leave)

        g8_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[8]}", font=("Helvetica", 10))
        g8_cs_grade_label.grid(row=9, column=1, pady=5)

        g8_cs_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g8_grades[8],
                                                                       g8_cs_grade_label, 8, 8, gwa_label),
                                     activebackground='#67C735')
        g8_cs_add_button.grid(row=9, column=2, padx=(0, 25))

        cs_add_button_hover = ButtonHover(g8_cs_add_button, 'subject_button', 'add')
        g8_cs_add_button.bind('<Enter>', cs_add_button_hover.on_enter)
        g8_cs_add_button.bind('<Leave>', cs_add_button_hover.on_leave)

        # Earth Science
        g8_es_label = tk.Label(self.window, text="Earth Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g8_es_label.grid(row=8, column=4)

        g8_es_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g8_grades[9],
                                                                         g8_es_grade_label, 9, 8, gwa_label),
                                       activebackground='#DB5F44')
        g8_es_minus_button.grid(row=9, column=3)

        es_minus_button_hover = ButtonHover(g8_es_minus_button, 'subject_button', 'minus')
        g8_es_minus_button.bind('<Enter>', es_minus_button_hover.on_enter)
        g8_es_minus_button.bind('<Leave>', es_minus_button_hover.on_leave)

        g8_es_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g8_grades[9]}", font=("Helvetica", 10))
        g8_es_grade_label.grid(row=9, column=4, pady=5)

        g8_es_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g8_grades[9],
                                                                       g8_es_grade_label, 9, 8, gwa_label),
                                     activebackground='#67C735')
        g8_es_add_button.grid(row=9, column=5)

        es_add_button_hover = ButtonHover(g8_es_add_button, 'subject_button', 'add')
        g8_es_add_button.bind('<Enter>', es_add_button_hover.on_enter)
        g8_es_add_button.bind('<Leave>', es_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G8', CalculateButtons.g8_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g8_is_grade_label, g8_math_grade_label, g8_eng_grade_label, g8_fil_grade_label,
                             g8_ss_grade_label, g8_pehm_grade_label, g8_valed_grade_label, g8_adtech_grade_label,
                             g8_cs_grade_label, g8_es_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G8', CalculateButtons.g8_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

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
                      back_button_g8, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def g9_update(self):
        self.window.config(bg='#8EF4B5')

        # Back button
        back_button_g9 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                   command=lambda: self.back_decision(1, g9_buttons, gwa_labels),
                                   activebackground='#DB5F44')
        back_button_g9.place(x=10, y=20)

        back_button_g9_hover = ButtonHover(back_button_g9, 'back_button')
        back_button_g9.bind('<Enter>', back_button_g9_hover.on_enter)
        back_button_g9.bind('<Leave>', back_button_g9_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 9 buttons

        # Biology
        g9_bio_label = tk.Label(self.window, text="       Biology       ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g9_bio_label.grid(row=0, column=1, pady=(15, 0))

        g9_bio_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g9_grades[0],
                                                                          g9_bio_grade_label, 0, 9, gwa_label),
                                        activebackground='#DB5F44')
        g9_bio_minus_button.grid(row=1, column=0, padx=(200, 0))

        bio_minus_button_hover = ButtonHover(g9_bio_minus_button, 'subject_button', 'minus')
        g9_bio_minus_button.bind('<Enter>', bio_minus_button_hover.on_enter)
        g9_bio_minus_button.bind('<Leave>', bio_minus_button_hover.on_leave)

        g9_bio_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[0]}", font=("Helvetica", 10))
        g9_bio_grade_label.grid(row=1, column=1, pady=5)

        g9_bio_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g9_grades[0],
                                                                        g9_bio_grade_label, 0, 9, gwa_label),
                                      activebackground='#67C735')
        g9_bio_add_button.grid(row=1, column=2, padx=(0, 25))

        bio_add_button_hover = ButtonHover(g9_bio_add_button, 'subject_button', 'add')
        g9_bio_add_button.bind('<Enter>', bio_add_button_hover.on_enter)
        g9_bio_add_button.bind('<Leave>', bio_add_button_hover.on_leave)

        # Chemistry
        g9_chem_label = tk.Label(self.window, text="      Chemistry      ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g9_chem_label.grid(row=0, column=4, pady=(15, 0))

        g9_chem_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g9_grades[1],
                                                                           g9_chem_grade_label, 1, 9, gwa_label),
                                         activebackground='#DB5F44')
        g9_chem_minus_button.grid(row=1, column=3)

        chem_minus_button_hover = ButtonHover(g9_chem_minus_button, 'subject_button', 'minus')
        g9_chem_minus_button.bind('<Enter>', chem_minus_button_hover.on_enter)
        g9_chem_minus_button.bind('<Leave>', chem_minus_button_hover.on_leave)

        g9_chem_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[1]}", font=("Helvetica", 10))
        g9_chem_grade_label.grid(row=1, column=4, pady=5)

        g9_chem_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g9_grades[1],
                                                                         g9_chem_grade_label, 1, 9, gwa_label),
                                       activebackground='#67C735')
        g9_chem_add_button.grid(row=1, column=5)

        chem_add_button_hover = ButtonHover(g9_chem_add_button, 'subject_button', 'add')
        g9_chem_add_button.bind('<Enter>', chem_add_button_hover.on_enter)
        g9_chem_add_button.bind('<Leave>', chem_add_button_hover.on_leave)

        # Physics
        g9_p6_label = tk.Label(self.window, text="      Physics      ", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g9_p6_label.grid(row=2, column=1)

        g9_p6_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g9_grades[2],
                                                                         g9_p6_grade_label, 2, 9, gwa_label),
                                       activebackground='#DB5F44')
        g9_p6_minus_button.grid(row=3, column=0, padx=(200, 0))

        p6_minus_button_hover = ButtonHover(g9_p6_minus_button, 'subject_button', 'minus')
        g9_p6_minus_button.bind('<Enter>', p6_minus_button_hover.on_enter)
        g9_p6_minus_button.bind('<Leave>', p6_minus_button_hover.on_leave)

        g9_p6_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[2]}", font=("Helvetica", 10))
        g9_p6_grade_label.grid(row=3, column=1, pady=5)

        g9_p6_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g9_grades[2],
                                                                       g9_p6_grade_label, 2, 9, gwa_label),
                                     activebackground='#67C735')
        g9_p6_add_button.grid(row=3, column=2, padx=(0, 25))

        p6_add_button_hover = ButtonHover(g9_p6_add_button, 'subject_button', 'add')
        g9_p6_add_button.bind('<Enter>', p6_add_button_hover.on_enter)
        g9_p6_add_button.bind('<Leave>', p6_add_button_hover.on_leave)

        # Mathematics
        g9_math_label = tk.Label(self.window, text="    Mathematics    ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g9_math_label.grid(row=2, column=4, pady=5)

        g9_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g9_grades[3],
                                                                           g9_math_grade_label, 3, 9, gwa_label),
                                         activebackground='#DB5F44')
        g9_math_minus_button.grid(row=3, column=3)

        math_minus_button_hover = ButtonHover(g9_math_minus_button, 'subject_button', 'minus')
        g9_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g9_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g9_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[3]}", font=("Helvetica", 10))
        g9_math_grade_label.grid(row=3, column=4)

        g9_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g9_grades[3],
                                                                         g9_math_grade_label, 3, 9, gwa_label),
                                       activebackground='#67C735')
        g9_math_add_button.grid(row=3, column=5)

        math_add_button_hover = ButtonHover(g9_math_add_button, 'subject_button', 'add')
        g9_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g9_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g9_eng_label = tk.Label(self.window, text="       English      ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g9_eng_label.grid(row=4, column=1)

        g9_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g9_grades[4],
                                                                          g9_eng_grade_label, 4, 9, gwa_label),
                                        activebackground='#DB5F44')
        g9_eng_minus_button.grid(row=5, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g9_eng_minus_button, 'subject_button', 'minus')
        g9_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g9_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g9_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[4]}", font=("Helvetica", 10))
        g9_eng_grade_label.grid(row=5, column=1, pady=5)

        g9_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g9_grades[4],
                                                                        g9_eng_grade_label, 4, 9, gwa_label),
                                      activebackground='#67C735')
        g9_eng_add_button.grid(row=5, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g9_eng_add_button, 'subject_button', 'add')
        g9_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g9_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g9_fil_label = tk.Label(self.window, text="        Filipino        ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g9_fil_label.grid(row=4, column=4)

        g9_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g9_grades[5],
                                                                          g9_fil_grade_label, 5, 9, gwa_label),
                                        activebackground='#DB5F44')
        g9_fil_minus_button.grid(row=5, column=3)

        fil_minus_button_hover = ButtonHover(g9_fil_minus_button, 'subject_button', 'minus')
        g9_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g9_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g9_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[5]}", font=("Helvetica", 10))
        g9_fil_grade_label.grid(row=5, column=4, pady=5)

        g9_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g9_grades[5],
                                                                        g9_fil_grade_label, 5, 9, gwa_label),
                                      activebackground='#67C735')
        g9_fil_add_button.grid(row=5, column=5)

        fil_add_button_hover = ButtonHover(g9_fil_add_button, 'subject_button', 'add')
        g9_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g9_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g9_ss_label = tk.Label(self.window, text="  Social Science  ", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g9_ss_label.grid(row=6, column=1)

        g9_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g9_grades[6],
                                                                         g9_ss_grade_label, 6, 9, gwa_label),
                                       activebackground='#DB5F44')
        g9_ss_minus_button.grid(row=7, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g9_ss_minus_button, 'subject_button', 'minus')
        g9_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g9_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g9_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[6]}", font=("Helvetica", 10))
        g9_ss_grade_label.grid(row=7, column=1, pady=5)

        g9_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g9_grades[6],
                                                                       g9_ss_grade_label, 6, 9, gwa_label),
                                     activebackground='#67C735')
        g9_ss_add_button.grid(row=7, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g9_ss_add_button, 'subject_button', 'add')
        g9_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g9_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # PEHM
        g9_pehm_label = tk.Label(self.window, text="         PEHM         ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g9_pehm_label.grid(row=6, column=4)

        g9_pehm_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g9_grades[7],
                                                                           g9_pehm_grade_label, 7, 9, gwa_label),
                                         activebackground='#DB5F44')
        g9_pehm_minus_button.grid(row=7, column=3)

        pehm_minus_button_hover = ButtonHover(g9_pehm_minus_button, 'subject_button', 'minus')
        g9_pehm_minus_button.bind('<Enter>', pehm_minus_button_hover.on_enter)
        g9_pehm_minus_button.bind('<Leave>', pehm_minus_button_hover.on_leave)

        g9_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[7]}", font=("Helvetica", 10))
        g9_pehm_grade_label.grid(row=7, column=4, pady=5)

        g9_pehm_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g9_grades[7],
                                                                         g9_pehm_grade_label, 7, 9, gwa_label),
                                       activebackground='#67C735')
        g9_pehm_add_button.grid(row=7, column=5)

        pehm_add_button_hover = ButtonHover(g9_pehm_add_button, 'subject_button', 'add')
        g9_pehm_add_button.bind('<Enter>', pehm_add_button_hover.on_enter)
        g9_pehm_add_button.bind('<Leave>', pehm_add_button_hover.on_leave)

        # Statistics
        g9_stat_label = tk.Label(self.window, text="     Statistics     ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g9_stat_label.grid(row=8, column=1)

        g9_stat_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g9_grades[8],
                                                                           g9_stat_grade_label, 8, 9, gwa_label),
                                         activebackground='#DB5F44')
        g9_stat_minus_button.grid(row=9, column=0, padx=(200, 0))

        stat_minus_button_hover = ButtonHover(g9_stat_minus_button, 'subject_button', 'minus')
        g9_stat_minus_button.bind('<Enter>', stat_minus_button_hover.on_enter)
        g9_stat_minus_button.bind('<Leave>', stat_minus_button_hover.on_leave)

        g9_stat_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[8]}", font=("Helvetica", 10))
        g9_stat_grade_label.grid(row=9, column=1, pady=5)

        g9_stat_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g9_grades[8],
                                                                         g9_stat_grade_label, 8, 9, gwa_label),
                                       activebackground='#67C735')
        g9_stat_add_button.grid(row=9, column=2, padx=(0, 25))

        stat_add_button_hover = ButtonHover(g9_stat_add_button, 'subject_button', 'add')
        g9_stat_add_button.bind('<Enter>', stat_add_button_hover.on_enter)
        g9_stat_add_button.bind('<Leave>', stat_add_button_hover.on_leave)

        # Computer Science
        g9_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10), borderwidth=2,
                               relief='groove')
        g9_cs_label.grid(row=8, column=4)

        g9_cs_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('-', CalculateButtons.g9_grades[9],
                                                                         g9_cs_grade_label, 9, 9, gwa_label),
                                       activebackground='#DB5F44')
        g9_cs_minus_button.grid(row=9, column=3)

        cs_minus_button_hover = ButtonHover(g9_cs_minus_button, 'subject_button', 'minus')
        g9_cs_minus_button.bind('<Enter>', cs_minus_button_hover.on_enter)
        g9_cs_minus_button.bind('<Leave>', cs_minus_button_hover.on_leave)

        g9_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g9_grades[9]}", font=("Helvetica", 10))
        g9_cs_grade_label.grid(row=9, column=4, pady=5)

        g9_cs_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                     command=lambda: self.grade_change('+', CalculateButtons.g9_grades[9],
                                                                       g9_cs_grade_label, 9, 9, gwa_label),
                                     activebackground='#67C735')
        g9_cs_add_button.grid(row=9, column=5)

        cs_add_button_hover = ButtonHover(g9_cs_add_button, 'subject_button', 'add')
        g9_cs_add_button.bind('<Enter>', cs_add_button_hover.on_enter)
        g9_cs_add_button.bind('<Leave>', cs_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G9', CalculateButtons.g9_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g9_bio_grade_label, g9_chem_grade_label, g9_p6_grade_label, g9_math_grade_label,
                             g9_eng_grade_label, g9_fil_grade_label, g9_ss_grade_label, g9_pehm_grade_label,
                             g9_stat_grade_label, g9_cs_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G9', CalculateButtons.g9_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

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
                      back_button_g9, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def g10_update(self):
        self.window.config(bg='#89D6FF')

        # Back button
        back_button_g10 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                    command=lambda: self.back_decision(1, g10_buttons, gwa_labels),
                                    activebackground='#DB5F44')
        back_button_g10.place(x=10, y=20)

        back_button_g10_hover = ButtonHover(back_button_g10, 'back_button')
        back_button_g10.bind('<Enter>', back_button_g10_hover.on_enter)
        back_button_g10.bind('<Leave>', back_button_g10_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 10 buttons

        # Biology
        g10_bio_label = tk.Label(self.window, text="       Biology       ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g10_bio_label.grid(row=0, column=1, pady=(15, 0))

        g10_bio_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g10_grades[0],
                                                                           g10_bio_grade_label, 0, 10, gwa_label),
                                         activebackground='#DB5F44')
        g10_bio_minus_button.grid(row=1, column=0, padx=(200, 0))

        bio_minus_button_hover = ButtonHover(g10_bio_minus_button, 'subject_button', 'minus')
        g10_bio_minus_button.bind('<Enter>', bio_minus_button_hover.on_enter)
        g10_bio_minus_button.bind('<Leave>', bio_minus_button_hover.on_leave)

        g10_bio_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[0]}", font=("Helvetica", 10))
        g10_bio_grade_label.grid(row=1, column=1, pady=5)

        g10_bio_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g10_grades[0],
                                                                         g10_bio_grade_label, 0, 10, gwa_label),
                                       activebackground='#67C735')
        g10_bio_add_button.grid(row=1, column=2, padx=(0, 25))

        bio_add_button_hover = ButtonHover(g10_bio_add_button, 'subject_button', 'add')
        g10_bio_add_button.bind('<Enter>', bio_add_button_hover.on_enter)
        g10_bio_add_button.bind('<Leave>', bio_add_button_hover.on_leave)

        # Chemistry
        g10_chem_label = tk.Label(self.window, text="      Chemistry      ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g10_chem_label.grid(row=0, column=4, pady=(15, 0))

        g10_chem_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g10_grades[1],
                                                                            g10_chem_grade_label, 1, 10, gwa_label),
                                          activebackground='#DB5F44')
        g10_chem_minus_button.grid(row=1, column=3)

        chem_minus_button_hover = ButtonHover(g10_chem_minus_button, 'subject_button', 'minus')
        g10_chem_minus_button.bind('<Enter>', chem_minus_button_hover.on_enter)
        g10_chem_minus_button.bind('<Leave>', chem_minus_button_hover.on_leave)

        g10_chem_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[1]}", font=("Helvetica", 10))
        g10_chem_grade_label.grid(row=1, column=4, pady=5)

        g10_chem_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g10_grades[1],
                                                                          g10_chem_grade_label, 1, 10, gwa_label),
                                        activebackground='#67C735')
        g10_chem_add_button.grid(row=1, column=5)

        chem_add_button_hover = ButtonHover(g10_chem_add_button, 'subject_button', 'add')
        g10_chem_add_button.bind('<Enter>', chem_add_button_hover.on_enter)
        g10_chem_add_button.bind('<Leave>', chem_add_button_hover.on_leave)

        # Physics
        g10_p6_label = tk.Label(self.window, text="      Physics      ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g10_p6_label.grid(row=2, column=1)

        g10_p6_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g10_grades[2],
                                                                          g10_p6_grade_label, 2, 10, gwa_label),
                                        activebackground='#DB5F44')
        g10_p6_minus_button.grid(row=3, column=0, padx=(200, 0))

        p6_minus_button_hover = ButtonHover(g10_p6_minus_button, 'subject_button', 'minus')
        g10_p6_minus_button.bind('<Enter>', p6_minus_button_hover.on_enter)
        g10_p6_minus_button.bind('<Leave>', p6_minus_button_hover.on_leave)

        g10_p6_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[2]}", font=("Helvetica", 10))
        g10_p6_grade_label.grid(row=3, column=1, pady=5)

        g10_p6_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g10_grades[2],
                                                                        g10_p6_grade_label, 2, 10, gwa_label),
                                      activebackground='#67C735')
        g10_p6_add_button.grid(row=3, column=2, padx=(0, 25))

        p6_add_button_hover = ButtonHover(g10_p6_add_button, 'subject_button', 'add')
        g10_p6_add_button.bind('<Enter>', p6_add_button_hover.on_enter)
        g10_p6_add_button.bind('<Leave>', p6_add_button_hover.on_leave)

        # Mathematics
        g10_math_label = tk.Label(self.window, text="    Mathematics    ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g10_math_label.grid(row=2, column=4)

        g10_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g10_grades[3],
                                                                            g10_math_grade_label, 3, 10, gwa_label),
                                          activebackground='#DB5F44')
        g10_math_minus_button.grid(row=3, column=3)

        math_minus_button_hover = ButtonHover(g10_math_minus_button, 'subject_button', 'minus')
        g10_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g10_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g10_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[3]}", font=("Helvetica", 10))
        g10_math_grade_label.grid(row=3, column=4, pady=5)

        g10_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g10_grades[3],
                                                                          g10_math_grade_label, 3, 10, gwa_label),
                                        activebackground='#67C735')
        g10_math_add_button.grid(row=3, column=5)

        math_add_button_hover = ButtonHover(g10_math_add_button, 'subject_button', 'add')
        g10_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g10_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g10_eng_label = tk.Label(self.window, text="       English      ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g10_eng_label.grid(row=4, column=1)

        g10_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g10_grades[4],
                                                                           g10_eng_grade_label, 4, 10, gwa_label),
                                         activebackground='#DB5F44')
        g10_eng_minus_button.grid(row=5, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g10_eng_minus_button, 'subject_button', 'minus')
        g10_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g10_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g10_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[4]}", font=("Helvetica", 10))
        g10_eng_grade_label.grid(row=5, column=1, pady=5)

        g10_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g10_grades[4],
                                                                         g10_eng_grade_label, 4, 10, gwa_label),
                                       activebackground='#67C735')
        g10_eng_add_button.grid(row=5, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g10_eng_add_button, 'subject_button', 'add')
        g10_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g10_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g10_fil_label = tk.Label(self.window, text="        Filipino        ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g10_fil_label.grid(row=4, column=4)

        g10_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g10_grades[5],
                                                                           g10_fil_grade_label, 5, 10, gwa_label),
                                         activebackground='#DB5F44')
        g10_fil_minus_button.grid(row=5, column=3)

        fil_minus_button_hover = ButtonHover(g10_fil_minus_button, 'subject_button', 'minus')
        g10_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g10_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g10_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[5]}", font=("Helvetica", 10))
        g10_fil_grade_label.grid(row=5, column=4, pady=5)

        g10_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g10_grades[5],
                                                                         g10_fil_grade_label, 5, 10, gwa_label),
                                       activebackground='#67C735')
        g10_fil_add_button.grid(row=5, column=5)

        fil_add_button_hover = ButtonHover(g10_fil_add_button, 'subject_button', 'add')
        g10_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g10_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g10_ss_label = tk.Label(self.window, text="  Social Science  ", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g10_ss_label.grid(row=6, column=1)

        g10_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g10_grades[6],
                                                                          g10_ss_grade_label, 6, 10, gwa_label),
                                        activebackground='#DB5F44')
        g10_ss_minus_button.grid(row=7, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g10_ss_minus_button, 'subject_button', 'minus')
        g10_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g10_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g10_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[6]}", font=("Helvetica", 10))
        g10_ss_grade_label.grid(row=7, column=1, pady=5)

        g10_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g10_grades[6],
                                                                        g10_ss_grade_label, 6, 10, gwa_label),
                                      activebackground='#67C735')
        g10_ss_add_button.grid(row=7, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g10_ss_add_button, 'subject_button', 'add')
        g10_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g10_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # PEHM
        g10_pehm_label = tk.Label(self.window, text="         PEHM         ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g10_pehm_label.grid(row=6, column=4, pady=5)

        g10_pehm_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g10_grades[7],
                                                                            g10_pehm_grade_label, 7, 10, gwa_label),
                                          activebackground='#DB5F44')
        g10_pehm_minus_button.grid(row=7, column=3)

        pehm_minus_button_hover = ButtonHover(g10_pehm_minus_button, 'subject_button', 'minus')
        g10_pehm_minus_button.bind('<Enter>', pehm_minus_button_hover.on_enter)
        g10_pehm_minus_button.bind('<Leave>', pehm_minus_button_hover.on_leave)

        g10_pehm_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[7]}", font=("Helvetica", 10))
        g10_pehm_grade_label.grid(row=7, column=4)

        g10_pehm_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g10_grades[7],
                                                                          g10_pehm_grade_label, 7, 10, gwa_label),
                                        activebackground='#67C735')
        g10_pehm_add_button.grid(row=7, column=5)

        pehm_add_button_hover = ButtonHover(g10_pehm_add_button, 'subject_button', 'add')
        g10_pehm_add_button.bind('<Enter>', pehm_add_button_hover.on_enter)
        g10_pehm_add_button.bind('<Leave>', pehm_add_button_hover.on_leave)

        # Research
        g10_res_label = tk.Label(self.window, text="     Research      ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g10_res_label.grid(row=8, column=1)

        g10_res_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g10_grades[8],
                                                                           g10_res_grade_label, 8, 10, gwa_label),
                                         activebackground='#DB5F44')
        g10_res_minus_button.grid(row=9, column=0, padx=(200, 0))

        res_minus_button_hover = ButtonHover(g10_res_minus_button, 'subject_button', 'minus')
        g10_res_minus_button.bind('<Enter>', res_minus_button_hover.on_enter)
        g10_res_minus_button.bind('<Leave>', res_minus_button_hover.on_leave)

        g10_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[8]}", font=("Helvetica", 10))
        g10_res_grade_label.grid(row=9, column=1, pady=5)

        g10_res_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g10_grades[8],
                                                                         g10_res_grade_label, 8, 10, gwa_label),
                                       activebackground='#67C735')
        g10_res_add_button.grid(row=9, column=2, padx=(0, 25))

        res_add_button_hover = ButtonHover(g10_res_add_button, 'subject_button', 'add')
        g10_res_add_button.bind('<Enter>', res_add_button_hover.on_enter)
        g10_res_add_button.bind('<Leave>', res_add_button_hover.on_leave)

        # Computer Science
        g10_cs_label = tk.Label(self.window, text="Computer Science", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g10_cs_label.grid(row=8, column=4)

        g10_cs_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g10_grades[9],
                                                                          g10_cs_grade_label, 9, 10, gwa_label),
                                        activebackground='#DB5F44')
        g10_cs_minus_button.grid(row=9, column=3)

        cs_minus_button_hover = ButtonHover(g10_cs_minus_button, 'subject_button', 'minus')
        g10_cs_minus_button.bind('<Enter>', cs_minus_button_hover.on_enter)
        g10_cs_minus_button.bind('<Leave>', cs_minus_button_hover.on_leave)

        g10_cs_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g10_grades[9]}", font=("Helvetica", 10))
        g10_cs_grade_label.grid(row=9, column=4, pady=5)

        g10_cs_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g10_grades[9],
                                                                        g10_cs_grade_label, 9, 10, gwa_label),
                                      activebackground='#67C735')
        g10_cs_add_button.grid(row=9, column=5)

        cs_add_button_hover = ButtonHover(g10_cs_add_button, 'subject_button', 'add')
        g10_cs_add_button.bind('<Enter>', cs_add_button_hover.on_enter)
        g10_cs_add_button.bind('<Leave>', cs_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G10', CalculateButtons.g10_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g10_bio_grade_label, g10_chem_grade_label, g10_p6_grade_label, g10_math_grade_label,
                             g10_eng_grade_label, g10_fil_grade_label, g10_ss_grade_label, g10_pehm_grade_label,
                             g10_res_grade_label, g10_cs_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G10', CalculateButtons.g10_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

        g10_buttons = [g10_bio_label, g10_bio_minus_button, g10_bio_grade_label, g10_bio_add_button,
                       g10_chem_label, g10_chem_minus_button, g10_chem_grade_label, g10_chem_add_button,
                       g10_p6_label, g10_p6_minus_button, g10_p6_grade_label, g10_p6_add_button,
                       g10_math_label, g10_math_minus_button, g10_math_grade_label, g10_math_add_button,
                       g10_eng_label, g10_eng_minus_button, g10_eng_grade_label, g10_eng_add_button,
                       g10_fil_label, g10_fil_minus_button, g10_fil_grade_label, g10_fil_add_button,
                       g10_ss_label, g10_ss_minus_button, g10_ss_grade_label, g10_ss_add_button,
                       g10_pehm_label, g10_pehm_minus_button, g10_pehm_grade_label, g10_pehm_add_button,
                       g10_res_label, g10_res_minus_button, g10_res_grade_label, g10_res_add_button,
                       g10_cs_label, g10_cs_minus_button, g10_cs_grade_label, g10_cs_add_button,
                       back_button_g10, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def g11_update(self):
        self.window.config(bg='#AF9DFF')

        # Back button
        back_button_g11 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                    command=lambda: self.back_decision(1, g11_buttons, gwa_labels),
                                    activebackground='#DB5F44')
        back_button_g11.place(x=10, y=20)

        back_button_g11_hover = ButtonHover(back_button_g11, 'back_button')
        back_button_g11.bind('<Enter>', back_button_g11_hover.on_enter)
        back_button_g11.bind('<Leave>', back_button_g11_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 11 buttons

        # Core
        g11_core_label = tk.Label(self.window, text="        Core        ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g11_core_label.grid(row=0, column=1, pady=(15, 0))

        g11_core_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g11_grades[0],
                                                                            g11_core_grade_label, 0, 11, gwa_label),
                                          activebackground='#DB5F44')
        g11_core_minus_button.grid(row=1, column=0, padx=(200, 0))

        core_minus_button_hover = ButtonHover(g11_core_minus_button, 'subject_button', 'minus')
        g11_core_minus_button.bind('<Enter>', core_minus_button_hover.on_enter)
        g11_core_minus_button.bind('<Leave>', core_minus_button_hover.on_leave)

        g11_core_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[0]}", font=("Helvetica", 10))
        g11_core_grade_label.grid(row=1, column=1, pady=5)

        g11_core_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g11_grades[0],
                                                                          g11_core_grade_label, 0, 11, gwa_label),
                                        activebackground='#67C735')
        g11_core_add_button.grid(row=1, column=2, padx=(0, 25))

        core_add_button_hover = ButtonHover(g11_core_add_button, 'subject_button', 'add')
        g11_core_add_button.bind('<Enter>', core_add_button_hover.on_enter)
        g11_core_add_button.bind('<Leave>', core_add_button_hover.on_leave)

        # Mathematics
        g11_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g11_math_label.grid(row=0, column=4, pady=(15, 0))

        g11_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g11_grades[1],
                                                                            g11_math_grade_label, 1, 11, gwa_label),
                                          activebackground='#DB5F44')
        g11_math_minus_button.grid(row=1, column=3)

        math_minus_button_hover = ButtonHover(g11_math_minus_button, 'subject_button', 'minus')
        g11_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g11_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g11_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[1]}", font=("Helvetica", 10))
        g11_math_grade_label.grid(row=1, column=4, pady=5)

        g11_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g11_grades[1],
                                                                          g11_math_grade_label, 1, 11, gwa_label),
                                        activebackground='#67C735')
        g11_math_add_button.grid(row=1, column=5)

        math_add_button_hover = ButtonHover(g11_math_add_button, 'subject_button', 'add')
        g11_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g11_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g11_eng_label = tk.Label(self.window, text="      English      ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g11_eng_label.grid(row=2, column=1)

        g11_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g11_grades[2],
                                                                           g11_eng_grade_label, 2, 11, gwa_label),
                                         activebackground='#DB5F44')
        g11_eng_minus_button.grid(row=3, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g11_eng_minus_button, 'subject_button', 'minus')
        g11_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g11_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g11_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[2]}", font=("Helvetica", 10))
        g11_eng_grade_label.grid(row=3, column=1, pady=5)

        g11_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g11_grades[2],
                                                                         g11_eng_grade_label, 2, 11, gwa_label),
                                       activebackground='#67C735')
        g11_eng_add_button.grid(row=3, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g11_eng_add_button, 'subject_button', 'add')
        g11_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g11_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g11_fil_label = tk.Label(self.window, text="    Filipino    ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g11_fil_label.grid(row=2, column=4)

        g11_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g11_grades[3],
                                                                           g11_fil_grade_label, 3, 11, gwa_label),
                                         activebackground='#DB5F44')
        g11_fil_minus_button.grid(row=3, column=3)

        fil_minus_button_hover = ButtonHover(g11_fil_minus_button, 'subject_button', 'minus')
        g11_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g11_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g11_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[3]}", font=("Helvetica", 10))
        g11_fil_grade_label.grid(row=3, column=4, pady=5)

        g11_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g11_grades[3],
                                                                         g11_fil_grade_label, 3, 11, gwa_label),
                                       activebackground='#67C735')
        g11_fil_add_button.grid(row=3, column=5)

        fil_add_button_hover = ButtonHover(g11_fil_add_button, 'subject_button', 'add')
        g11_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g11_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g11_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g11_ss_label.grid(row=4, column=1)

        g11_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g11_grades[4],
                                                                          g11_ss_grade_label, 4, 11, gwa_label),
                                        activebackground='#DB5F44')
        g11_ss_minus_button.grid(row=5, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g11_ss_minus_button, 'subject_button', 'minus')
        g11_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g11_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g11_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[4]}", font=("Helvetica", 10))
        g11_ss_grade_label.grid(row=5, column=1, pady=5)

        g11_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g11_grades[4],
                                                                        g11_ss_grade_label, 4, 11, gwa_label),
                                      activebackground='#67C735')
        g11_ss_add_button.grid(row=5, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g11_ss_add_button, 'subject_button', 'add')
        g11_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g11_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # Research
        g11_res_label = tk.Label(self.window, text="   Research   ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g11_res_label.grid(row=4, column=4)

        g11_res_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g11_grades[5],
                                                                           g11_res_grade_label, 5, 11, gwa_label),
                                         activebackground='#DB5F44')
        g11_res_minus_button.grid(row=5, column=3)

        res_minus_button_hover = ButtonHover(g11_res_minus_button, 'subject_button', 'minus')
        g11_res_minus_button.bind('<Enter>', res_minus_button_hover.on_enter)
        g11_res_minus_button.bind('<Leave>', res_minus_button_hover.on_leave)

        g11_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[5]}", font=("Helvetica", 10))
        g11_res_grade_label.grid(row=5, column=4, pady=5)

        g11_res_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g11_grades[5],
                                                                         g11_res_grade_label, 5, 11, gwa_label),
                                       activebackground='#67C735')
        g11_res_add_button.grid(row=5, column=5)

        res_add_button_hover = ButtonHover(g11_res_add_button, 'subject_button', 'add')
        g11_res_add_button.bind('<Enter>', res_add_button_hover.on_enter)
        g11_res_add_button.bind('<Leave>', res_add_button_hover.on_leave)

        # Elective
        g11_elec_label = tk.Label(self.window, text="      Elective      ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g11_elec_label.grid(row=6, column=1)

        g11_elec_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g11_grades[6],
                                                                            g11_elec_grade_label, 6, 11, gwa_label),
                                          activebackground='#DB5F44')
        g11_elec_minus_button.grid(row=7, column=0, padx=(200, 0))

        elec_minus_button_hover = ButtonHover(g11_elec_minus_button, 'subject_button', 'minus')
        g11_elec_minus_button.bind('<Enter>', elec_minus_button_hover.on_enter)
        g11_elec_minus_button.bind('<Leave>', elec_minus_button_hover.on_leave)

        g11_elec_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g11_grades[6]}", font=("Helvetica", 10))
        g11_elec_grade_label.grid(row=7, column=1, pady=5)

        g11_elec_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g11_grades[6],
                                                                          g11_elec_grade_label, 6, 11, gwa_label),
                                        activebackground='#67C735')
        g11_elec_add_button.grid(row=7, column=2, padx=(0, 25))

        elec_add_button_hover = ButtonHover(g11_elec_add_button, 'subject_button', 'add')
        g11_elec_add_button.bind('<Enter>', elec_add_button_hover.on_enter)
        g11_elec_add_button.bind('<Leave>', elec_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G11', CalculateButtons.g11_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g11_core_grade_label, g11_math_grade_label, g11_eng_grade_label, g11_fil_grade_label,
                             g11_ss_grade_label, g11_res_grade_label, g11_elec_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G11', CalculateButtons.g11_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

        g11_buttons = [g11_core_label, g11_core_minus_button, g11_core_grade_label, g11_core_add_button,
                       g11_math_label, g11_math_minus_button, g11_math_grade_label, g11_math_add_button,
                       g11_eng_label, g11_eng_minus_button, g11_eng_grade_label, g11_eng_add_button,
                       g11_fil_label, g11_fil_minus_button, g11_fil_grade_label, g11_fil_add_button,
                       g11_ss_label, g11_ss_minus_button, g11_ss_grade_label, g11_ss_add_button,
                       g11_res_label, g11_res_minus_button, g11_res_grade_label, g11_res_add_button,
                       g11_elec_label, g11_elec_minus_button, g11_elec_grade_label, g11_elec_add_button,
                       back_button_g11, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def g12_update(self):
        self.window.config(bg='#FAA9FD')

        # Back button
        back_button_g12 = tk.Button(self.window, text="←", font=("Helvetica", 15),
                                    command=lambda: self.back_decision(1, g12_buttons, gwa_labels),
                                    activebackground='#DB5F44')
        back_button_g12.place(x=10, y=20)

        back_button_g12_hover = ButtonHover(back_button_g12, 'back_button')
        back_button_g12.bind('<Enter>', back_button_g12_hover.on_enter)
        back_button_g12.bind('<Leave>', back_button_g12_hover.on_leave)

        # GWA labels from GWA Calculation method; the purpose of this is for label removal.
        gwa_title_label, gwa_label = self.gwa_calculation('creation')
        gwa_labels = [gwa_title_label, gwa_label]

        # Grade 12 buttons

        # Core
        g12_core_label = tk.Label(self.window, text="        Core        ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g12_core_label.grid(row=0, column=1, pady=(15, 0))

        g12_core_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g12_grades[0],
                                                                            g12_core_grade_label, 0, 12, gwa_label),
                                          activebackground='#DB5F44')
        g12_core_minus_button.grid(row=1, column=0, padx=(200, 0))

        core_minus_button_hover = ButtonHover(g12_core_minus_button, 'subject_button', 'minus')
        g12_core_minus_button.bind('<Enter>', core_minus_button_hover.on_enter)
        g12_core_minus_button.bind('<Leave>', core_minus_button_hover.on_leave)

        g12_core_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[0]}", font=("Helvetica", 10))
        g12_core_grade_label.grid(row=1, column=1, pady=5)

        g12_core_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g12_grades[0],
                                                                          g12_core_grade_label, 0, 12, gwa_label),
                                        activebackground='#67C735')
        g12_core_add_button.grid(row=1, column=2, padx=(0, 25))

        core_add_button_hover = ButtonHover(g12_core_add_button, 'subject_button', 'add')
        g12_core_add_button.bind('<Enter>', core_add_button_hover.on_enter)
        g12_core_add_button.bind('<Leave>', core_add_button_hover.on_leave)

        # Mathematics
        g12_math_label = tk.Label(self.window, text="Mathematics", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g12_math_label.grid(row=0, column=4, pady=(15, 0))

        g12_math_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g12_grades[1],
                                                                            g12_math_grade_label, 1, 12, gwa_label),
                                          activebackground='#DB5F44')
        g12_math_minus_button.grid(row=1, column=3)

        math_minus_button_hover = ButtonHover(g12_math_minus_button, 'subject_button', 'minus')
        g12_math_minus_button.bind('<Enter>', math_minus_button_hover.on_enter)
        g12_math_minus_button.bind('<Leave>', math_minus_button_hover.on_leave)

        g12_math_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[1]}", font=("Helvetica", 10))
        g12_math_grade_label.grid(row=1, column=4, pady=5)

        g12_math_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g12_grades[1],
                                                                          g12_math_grade_label, 1, 12, gwa_label),
                                        activebackground='#67C735')
        g12_math_add_button.grid(row=1, column=5)

        math_add_button_hover = ButtonHover(g12_math_add_button, 'subject_button', 'add')
        g12_math_add_button.bind('<Enter>', math_add_button_hover.on_enter)
        g12_math_add_button.bind('<Leave>', math_add_button_hover.on_leave)

        # English
        g12_eng_label = tk.Label(self.window, text="      English      ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g12_eng_label.grid(row=2, column=1)

        g12_eng_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g12_grades[2],
                                                                           g12_eng_grade_label, 2, 12, gwa_label),
                                         activebackground='#DB5F44')
        g12_eng_minus_button.grid(row=3, column=0, padx=(200, 0))

        eng_minus_button_hover = ButtonHover(g12_eng_minus_button, 'subject_button', 'minus')
        g12_eng_minus_button.bind('<Enter>', eng_minus_button_hover.on_enter)
        g12_eng_minus_button.bind('<Leave>', eng_minus_button_hover.on_leave)

        g12_eng_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[2]}", font=("Helvetica", 10))
        g12_eng_grade_label.grid(row=3, column=1, pady=5)

        g12_eng_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g12_grades[2],
                                                                         g12_eng_grade_label, 2, 12, gwa_label),
                                       activebackground='#67C735')
        g12_eng_add_button.grid(row=3, column=2, padx=(0, 25))

        eng_add_button_hover = ButtonHover(g12_eng_add_button, 'subject_button', 'add')
        g12_eng_add_button.bind('<Enter>', eng_add_button_hover.on_enter)
        g12_eng_add_button.bind('<Leave>', eng_add_button_hover.on_leave)

        # Filipino
        g12_fil_label = tk.Label(self.window, text="    Filipino    ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g12_fil_label.grid(row=2, column=4)

        g12_fil_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g12_grades[3],
                                                                           g12_fil_grade_label, 3, 12, gwa_label),
                                         activebackground='#DB5F44')
        g12_fil_minus_button.grid(row=3, column=3)

        fil_minus_button_hover = ButtonHover(g12_fil_minus_button, 'subject_button', 'minus')
        g12_fil_minus_button.bind('<Enter>', fil_minus_button_hover.on_enter)
        g12_fil_minus_button.bind('<Leave>', fil_minus_button_hover.on_leave)

        g12_fil_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[3]}", font=("Helvetica", 10))
        g12_fil_grade_label.grid(row=3, column=4, pady=5)

        g12_fil_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g12_grades[3],
                                                                         g12_fil_grade_label, 3, 12, gwa_label),
                                       activebackground='#67C735')
        g12_fil_add_button.grid(row=3, column=5)

        fil_add_button_hover = ButtonHover(g12_fil_add_button, 'subject_button', 'add')
        g12_fil_add_button.bind('<Enter>', fil_add_button_hover.on_enter)
        g12_fil_add_button.bind('<Leave>', fil_add_button_hover.on_leave)

        # Social Science
        g12_ss_label = tk.Label(self.window, text="Social Science", font=("Helvetica", 10), borderwidth=2,
                                relief='groove')
        g12_ss_label.grid(row=4, column=1)

        g12_ss_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('-', CalculateButtons.g12_grades[4],
                                                                          g12_ss_grade_label, 4, 12, gwa_label),
                                        activebackground='#DB5F44')
        g12_ss_minus_button.grid(row=5, column=0, padx=(200, 0))

        ss_minus_button_hover = ButtonHover(g12_ss_minus_button, 'subject_button', 'minus')
        g12_ss_minus_button.bind('<Enter>', ss_minus_button_hover.on_enter)
        g12_ss_minus_button.bind('<Leave>', ss_minus_button_hover.on_leave)

        g12_ss_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[4]}", font=("Helvetica", 10))
        g12_ss_grade_label.grid(row=5, column=1, pady=5)

        g12_ss_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                      command=lambda: self.grade_change('+', CalculateButtons.g12_grades[4],
                                                                        g12_ss_grade_label, 4, 12, gwa_label),
                                      activebackground='#67C735')
        g12_ss_add_button.grid(row=5, column=2, padx=(0, 25))

        ss_add_button_hover = ButtonHover(g12_ss_add_button, 'subject_button', 'add')
        g12_ss_add_button.bind('<Enter>', ss_add_button_hover.on_enter)
        g12_ss_add_button.bind('<Leave>', ss_add_button_hover.on_leave)

        # Research
        g12_res_label = tk.Label(self.window, text="   Research   ", font=("Helvetica", 10), borderwidth=2,
                                 relief='groove')
        g12_res_label.grid(row=4, column=4)

        g12_res_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                         command=lambda: self.grade_change('-', CalculateButtons.g12_grades[5],
                                                                           g12_res_grade_label, 5, 12, gwa_label),
                                         activebackground='#DB5F44')
        g12_res_minus_button.grid(row=5, column=3)

        res_minus_button_hover = ButtonHover(g12_res_minus_button, 'subject_button', 'minus')
        g12_res_minus_button.bind('<Enter>', res_minus_button_hover.on_enter)
        g12_res_minus_button.bind('<Leave>', res_minus_button_hover.on_leave)

        g12_res_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[5]}", font=("Helvetica", 10))
        g12_res_grade_label.grid(row=5, column=4, pady=5)

        g12_res_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                       command=lambda: self.grade_change('+', CalculateButtons.g12_grades[5],
                                                                         g12_res_grade_label, 5, 12, gwa_label),
                                       activebackground='#67C735')
        g12_res_add_button.grid(row=5, column=5)

        res_add_button_hover = ButtonHover(g12_res_add_button, 'subject_button', 'add')
        g12_res_add_button.bind('<Enter>', res_add_button_hover.on_enter)
        g12_res_add_button.bind('<Leave>', res_add_button_hover.on_leave)

        # Elective
        g12_elec_label = tk.Label(self.window, text="      Elective      ", font=("Helvetica", 10), borderwidth=2,
                                  relief='groove')
        g12_elec_label.grid(row=6, column=1)

        g12_elec_minus_button = tk.Button(self.window, text=" - ", font=("Helvetica", 10),
                                          command=lambda: self.grade_change('-', CalculateButtons.g12_grades[6],
                                                                            g12_elec_grade_label, 6, 12, gwa_label),
                                          activebackground='#DB5F44')
        g12_elec_minus_button.grid(row=7, column=0, padx=(200, 0))

        elec_minus_button_hover = ButtonHover(g12_elec_minus_button, 'subject_button', 'minus')
        g12_elec_minus_button.bind('<Enter>', elec_minus_button_hover.on_enter)
        g12_elec_minus_button.bind('<Leave>', elec_minus_button_hover.on_leave)

        g12_elec_grade_label = tk.Label(self.window, text=f"{CalculateButtons.g12_grades[6]}", font=("Helvetica", 10))
        g12_elec_grade_label.grid(row=7, column=1, pady=5)

        g12_elec_add_button = tk.Button(self.window, text=" + ", font=("Helvetica", 10),
                                        command=lambda: self.grade_change('+', CalculateButtons.g12_grades[6],
                                                                          g12_elec_grade_label, 6, 12, gwa_label),
                                        activebackground='#67C735')
        g12_elec_add_button.grid(row=7, column=2, padx=(0, 25))

        elec_add_button_hover = ButtonHover(g12_elec_add_button, 'subject_button', 'add')
        g12_elec_add_button.bind('<Enter>', elec_add_button_hover.on_enter)
        g12_elec_add_button.bind('<Leave>', elec_add_button_hover.on_leave)

        # GWA Save button
        save_gwa = SaveGWA(self.window, 'G12', CalculateButtons.g12_grades)
        save_gwa_button, save_gwa_entry = save_gwa.save_button_and_entry()

        # Labels for import
        labels_for_import = [g12_core_grade_label, g12_math_grade_label, g12_eng_grade_label, g12_fil_grade_label,
                             g12_ss_grade_label, g12_res_grade_label, g12_elec_grade_label]

        # GWA Import button
        import_gwa = ImportGWA(self.window, 'G12', CalculateButtons.g12_grades, labels_for_import, gwa_label)
        import_gwa_button, import_gwa_entry = import_gwa.import_button_and_entry()

        g12_buttons = [g12_core_label, g12_core_minus_button, g12_core_grade_label, g12_core_add_button,
                       g12_math_label, g12_math_minus_button, g12_math_grade_label, g12_math_add_button,
                       g12_eng_label, g12_eng_minus_button, g12_eng_grade_label, g12_eng_add_button,
                       g12_fil_label, g12_fil_minus_button, g12_fil_grade_label, g12_fil_add_button,
                       g12_ss_label, g12_ss_minus_button, g12_ss_grade_label, g12_ss_add_button,
                       g12_res_label, g12_res_minus_button, g12_res_grade_label, g12_res_add_button,
                       g12_elec_label, g12_elec_minus_button, g12_elec_grade_label, g12_elec_add_button,
                       back_button_g12, save_gwa_button, save_gwa_entry, import_gwa_button, import_gwa_entry]

    def grade_change(self, operation, grade, label, index, grade_level, gwa_label):
        if operation == '+':
            if grade < 5.0:
                grade += 0.25

                if grade_level == 7:
                    CalculateButtons.g7_grades[index] = grade
                    self.gwa_calculation(7, CalculateButtons.g7_grades, gwa_label)
                elif grade_level == 8:
                    CalculateButtons.g8_grades[index] = grade
                    self.gwa_calculation(8, CalculateButtons.g8_grades, gwa_label)
                elif grade_level == 9:
                    CalculateButtons.g9_grades[index] = grade
                    self.gwa_calculation(9, CalculateButtons.g9_grades, gwa_label)
                elif grade_level == 10:
                    CalculateButtons.g10_grades[index] = grade
                    self.gwa_calculation(10, CalculateButtons.g10_grades, gwa_label)
                elif grade_level == 11:
                    CalculateButtons.g11_grades[index] = grade
                    self.gwa_calculation(11, CalculateButtons.g11_grades, gwa_label)
                elif grade_level == 12:
                    CalculateButtons.g12_grades[index] = grade
                    self.gwa_calculation(12, CalculateButtons.g12_grades, gwa_label)

                label.config(text=f"{grade}", font=("Helvetica", 10))
        elif operation == '-':
            if grade > 1.0:
                grade -= 0.25

                if grade_level == 7:
                    CalculateButtons.g7_grades[index] = grade
                    self.gwa_calculation(7, CalculateButtons.g7_grades, gwa_label)
                elif grade_level == 8:
                    CalculateButtons.g8_grades[index] = grade
                    self.gwa_calculation(8, CalculateButtons.g8_grades, gwa_label)
                elif grade_level == 9:
                    CalculateButtons.g9_grades[index] = grade
                    self.gwa_calculation(9, CalculateButtons.g9_grades, gwa_label)
                elif grade_level == 10:
                    CalculateButtons.g10_grades[index] = grade
                    self.gwa_calculation(10, CalculateButtons.g10_grades, gwa_label)
                elif grade_level == 11:
                    CalculateButtons.g11_grades[index] = grade
                    self.gwa_calculation(11, CalculateButtons.g11_grades, gwa_label)
                elif grade_level == 12:
                    CalculateButtons.g12_grades[index] = grade
                    self.gwa_calculation(12, CalculateButtons.g12_grades, gwa_label)

                label.config(text=f"{grade}", font=("Helvetica", 10))

    def gwa_calculation(self, grade_level, grades=None, gwa_label=None):
        if grade_level == 'creation':
            gwa_title_label = tk.Label(self.window, text="            GWA             ",
                                       font=("Helvetica", 10), bg='white', borderwidth=2, relief='groove')
            gwa_title_label.place(x=10, y=90)

            gwa_label = tk.Label(self.window, text='            1.000             ', font=("Helvetica", 10),
                                 bg='white', borderwidth=2, relief='groove')
            gwa_label.place(x=10, y=115)

            return gwa_title_label, gwa_label

        elif grade_level == 7:
            gwa_grade_7 = (grades[0] * 1.7) + (grades[1] * 1.7) + \
                          (grades[2] * 1.3) + (grades[3] * 1.0) + \
                          (grades[4] * 1.0) + (grades[5] * 1.0) + \
                          (grades[6] * 0.7) + (grades[7] * 1.0) + \
                          (grades[8] * 1.0)

            gwa_grade_7 = str(round((gwa_grade_7 / 10.4), 3))

            if len(gwa_grade_7) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_7))
                gwa_grade_7 = gwa_grade_7 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_7}             ')
            # return gwa_grade_7

        elif grade_level == 8:
            gwa_grade_8 = (grades[0] * 2.0) + (grades[1] * 1.7) + \
                          (grades[2] * 1.3) + (grades[3] * 1.0) + \
                          (grades[4] * 1.0) + (grades[5] * 1.0) + \
                          (grades[6] * 0.7) + (grades[7] * 1.0) + \
                          (grades[8] * 1.0) + (grades[9] * 0.7)

            gwa_grade_8 = str(round((gwa_grade_8 / 11.4), 3))

            if len(gwa_grade_8) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_8))
                gwa_grade_8 = gwa_grade_8 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_8}             ')

        elif grade_level == 9:
            gwa_grade_9 = (grades[0] * 1.0) + (grades[1] * 1.0) + \
                          (grades[2] * 1.0) + (grades[3] * 1.0) + \
                          (grades[4] * 1.0) + (grades[5] * 1.0) + \
                          (grades[6] * 1.0) + (grades[7] * 1.0) + \
                          (grades[8] * 1.0) + (grades[9] * 1.0)

            gwa_grade_9 = str(round((gwa_grade_9 / 10.0), 3))

            if len(gwa_grade_9) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_9))
                gwa_grade_9 = gwa_grade_9 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_9}             ')

        elif grade_level == 10:
            gwa_grade_10 = (grades[0] * 1.0) + (grades[1] * 1.0) + \
                          (grades[2] * 1.0) + (grades[3] * 1.3) + \
                          (grades[4] * 1.0) + (grades[5] * 1.0) + \
                          (grades[6] * 1.0) + (grades[7] * 1.0) + \
                          (grades[8] * 1.0) + (grades[9] * 1.0)

            gwa_grade_10 = str(round((gwa_grade_10 / 10.3), 3))

            if len(gwa_grade_10) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_10))
                gwa_grade_10 = gwa_grade_10 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_10}             ')

        elif grade_level == 11:
            gwa_grade_11 = (grades[0] * 1.7) + (grades[1] * 1.0) + \
                           (grades[2] * 1.0) + (grades[3] * 1.0) + \
                           (grades[4] * 1.0) + (grades[5] * 2.0) + \
                           (grades[6] * 1.7)

            gwa_grade_11 = str(round((gwa_grade_11 / 9.4), 3))

            if len(gwa_grade_11) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_11))
                gwa_grade_11 = gwa_grade_11 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_11}             ')

        elif grade_level == 12:
            gwa_grade_12 = (grades[0] * 1.7) + (grades[1] * 1.0) + \
                           (grades[2] * 1.0) + (grades[3] * 1.0) + \
                           (grades[4] * 1.0) + (grades[5] * 2.0) + \
                           (grades[6] * 1.7)

            gwa_grade_12 = str(round((gwa_grade_12 / 9.4), 3))

            if len(gwa_grade_12) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_12))
                gwa_grade_12 = gwa_grade_12 + trailing_zero

            if gwa_label is not None:
                gwa_label.config(text=f'            {gwa_grade_12}             ')


class AboutThisApp:
    def __init__(self, window):
        # Back button
        self.back_button = tk.Button(window, text="←", font=("Helvetica", 15),
                                     command=lambda: self.back_decision(widget_list),
                                     activebackground='#DB5F44')
        self.back_button.place(x=10, y=20)

        back_button_hover = ButtonHover(self.back_button, 'back_button')
        self.back_button.bind('<Enter>', back_button_hover.on_enter)
        self.back_button.bind('<Leave>', back_button_hover.on_leave)

        # Text
        self.window = window
        about_me = tk.Label(window, text="About this app", font=("Helvetica", 20), bg='black', fg='white')
        about_me.place(x=75, y=25)

        app_description = tk.Label(window, text="This is an application for the PSHS grading system",
                                   font=("Helvetica", 14), bg='black', fg='white')
        app_description.place(x=100, y=100)

        app_description2 = tk.Label(window, text="that includes storage of GWA (General Weighted",
                                    font=("Helvetica", 14), bg='black', fg='white')
        app_description2.place(x=100, y=125)

        app_description3 = tk.Label(window, text="Average), and GWA calculation for all grade levels.",
                                    font=("Helvetica", 14), bg='black', fg='white')
        app_description3.place(x=100, y=150)

        created_by = tk.Label(window, text="xbryan25", font=("Helvetica", 15), bg='black', fg='white')
        created_by.place(x=425, y=225)

        version = tk.Label(window, text="v1.0 (07-17-22)", font=("Helvetica", 15), bg='black', fg='white')
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
