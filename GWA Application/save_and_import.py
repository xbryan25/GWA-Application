import tkinter as tk
import csv
import os
from button_hover import ButtonHover


class SaveGWA:
    def __init__(self, window, grade_level=None, grades=None):
        self.window = window

        self.grade_level = grade_level
        self.grades = grades
        self.gwa = 0

        # Entry widget
        self.entry = tk.Entry(self.window, font=("Helvetica", 10), justify='center', width=19)
        self.entry.place(x=10, y=180)

    def save_button_and_entry(self):
        # Save button
        save_button = tk.Button(self.window, text="            Save            ", font=("Helvetica", 10),
                                command=lambda: self.save_to_csv(self.entry))
        save_button.place(x=10, y=151)

        save_button_hover = ButtonHover(save_button, 'save_button')

        save_button.bind('<Enter>', save_button_hover.on_enter)
        save_button.bind('<Leave>', save_button_hover.on_leave)

        return save_button, self.entry

    def save_to_csv(self, entry):
        with open('data.csv', 'r', newline='') as csv_file1:
            csv_read = csv.reader(csv_file1)

            file_size = os.path.getsize('data.csv')

            if file_size == 0 and entry.get() == '':
                entry.insert(0, 'Input name.')
                entry.config(state='disabled')
                entry.bind("<Button-1>", self.input_name_click)
                return

            for line in csv_read:
                if entry.get() == '':
                    entry.insert(0, 'Input name.')
                    entry.config(state='disabled')
                    entry.bind("<Button-1>", self.input_name_click)
                    return
                elif entry.get() in line[0]:
                    entry.delete(0, len(entry.get()))
                    entry.insert(0, 'Name taken.')
                    entry.config(state='disabled')
                    entry.bind("<Button-1>", self.name_taken_click)
                    return

            with open('data.csv', 'a', newline='', encoding='utf-8') as csv_file2:
                csv_write = csv.writer(csv_file2, delimiter=',')

                self.get_gwa()
                self.grades.append(self.gwa)
                self.grades.insert(0, self.grade_level)
                self.grades.insert(0, entry.get())

                if entry.get() != 'Name taken.' and entry.get() != 'Name saved!' and entry.get() != 'Input name.'\
                        and entry.get() != '':
                    csv_write.writerow(self.grades)

                self.grades.pop()
                self.grades.pop(0)
                self.grades.pop(0)

                entry.delete(0, len(entry.get()))
                entry.insert(0, 'Name saved!')
                entry.config(state='disabled')
                entry.bind("<Button-1>", self.save_taken_click)
                return

    def get_gwa(self):
        if self.grade_level == 'G7':
            gwa_grade_7 = (self.grades[0]) * 1.7 + (self.grades[1] * 1.7) + \
                          (self.grades[2] * 1.3) + (self.grades[3] * 1.0) + \
                          (self.grades[4] * 1.0) + (self.grades[5] * 1.0) + \
                          (self.grades[6] * 0.7) + (self.grades[7] * 1.0) + \
                          (self.grades[8] * 1.0)

            gwa_grade_7 = str(round((gwa_grade_7 / 10.4), 3))

            if len(gwa_grade_7) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_7))
                gwa_grade_7 = gwa_grade_7 + trailing_zero
            self.gwa = gwa_grade_7

        elif self.grade_level == 'G8':
            gwa_grade_8 = (self.grades[0] * 2.0) + (self.grades[1] * 1.7) + \
                          (self.grades[2] * 1.3) + (self.grades[3] * 1.0) + \
                          (self.grades[4] * 1.0) + (self.grades[5] * 1.0) + \
                          (self.grades[6] * 0.7) + (self.grades[7] * 1.0) + \
                          (self.grades[8] * 1.0) + (self.grades[9] * 0.7)

            gwa_grade_8 = str(round((gwa_grade_8 / 11.4), 3))

            if len(gwa_grade_8) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_8))
                gwa_grade_8 = gwa_grade_8 + trailing_zero
            self.gwa = gwa_grade_8

        elif self.grade_level == 'G9':
            gwa_grade_9 = (self.grades[0] * 1.0) + (self.grades[1] * 1.0) + \
                          (self.grades[2] * 1.0) + (self.grades[3] * 1.0) + \
                          (self.grades[4] * 1.0) + (self.grades[5] * 1.0) + \
                          (self.grades[6] * 1.0) + (self.grades[7] * 1.0) + \
                          (self.grades[8] * 1.0) + (self.grades[9] * 1.0)

            gwa_grade_9 = str(round((gwa_grade_9 / 10.0), 3))

            if len(gwa_grade_9) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_9))
                gwa_grade_9 = gwa_grade_9 + trailing_zero
            self.gwa = gwa_grade_9

        elif self.grade_level == 'G10':
            gwa_grade_10 = (self.grades[0] * 1.0) + (self.grades[1] * 1.0) + \
                           (self.grades[2] * 1.0) + (self.grades[3] * 1.3) + \
                           (self.grades[4] * 1.0) + (self.grades[5] * 1.0) + \
                           (self.grades[6] * 1.0) + (self.grades[7] * 1.0) + \
                           (self.grades[8] * 1.0) + (self.grades[9] * 1.0)

            gwa_grade_10 = str(round((gwa_grade_10 / 10.3), 3))

            if len(gwa_grade_10) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_10))
                gwa_grade_10 = gwa_grade_10 + trailing_zero
            self.gwa = gwa_grade_10

        elif self.grade_level == 'G11':
            gwa_grade_11 = (self.grades[0] * 1.7) + (self.grades[1] * 1.0) + \
                           (self.grades[2] * 1.0) + (self.grades[3] * 1.0) + \
                           (self.grades[4] * 1.0) + (self.grades[5] * 2.0) + \
                           (self.grades[6] * 1.7)

            gwa_grade_11 = str(round((gwa_grade_11 / 9.4), 3))

            if len(gwa_grade_11) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_11))
                gwa_grade_11 = gwa_grade_11 + trailing_zero
            self.gwa = gwa_grade_11

        elif self.grade_level == 'G12':
            gwa_grade_12 = (self.grades[0] * 1.7) + (self.grades[1] * 1.0) + \
                           (self.grades[2] * 1.0) + (self.grades[3] * 1.0) + \
                           (self.grades[4] * 1.0) + (self.grades[5] * 2.0) + \
                           (self.grades[6] * 1.7)

            gwa_grade_12 = str(round((gwa_grade_12 / 9.4), 3))

            if len(gwa_grade_12) < 5:
                trailing_zero = '0' * (5 - len(gwa_grade_12))
                gwa_grade_12 = gwa_grade_12 + trailing_zero
            self.gwa = gwa_grade_12

    def name_taken_click(self, event):
        self.entry.config(state='normal')
        self.entry.delete(0, 11)

    def input_name_click(self, event):
        self.entry.config(state='normal')
        self.entry.delete(0, 11)

    def save_taken_click(self, event):
        self.entry.config(state='normal')
        self.entry.delete(0, 11)


class ImportGWA:
    def __init__(self, window, grade_level, grades, subject_labels, gwa_label):
        self.window = window
        self.grade_level = grade_level
        self.grades = grades
        self.subject_labels = subject_labels
        self.gwa_label = gwa_label

        # Entry widget
        self.entry = tk.Entry(self.window, font=("Helvetica", 10), justify='center', width=19)
        self.entry.place(x=10, y=234)

    def import_button_and_entry(self):
        import_button = tk.Button(self.window, text="           Import           ", font=("Helvetica", 10),
                                  command=lambda: self.read_csv())
        import_button.place(x=10, y=205)

        import_button_hover = ButtonHover(import_button, 'import_button')

        import_button.bind('<Enter>', import_button_hover.on_enter)
        import_button.bind('<Leave>', import_button_hover.on_leave)

        return import_button, self.entry

    def read_csv(self):
        with open('data.csv', 'r', newline='') as csv_file1:
            csv_read = csv.reader(csv_file1)

            file_size = os.path.getsize('data.csv')

            if file_size > 0:
                for line in csv_read:
                    if self.in_csv(line) == 'name exists':
                        self.entry.delete(0, len(self.entry.get()))
                        self.entry.insert(0, 'Success!')
                        self.entry.config(state='disabled')
                        self.entry.bind("<Button-1>", self.success_click)

                        if self.grade_level == line[1] and self.grade_level == 'G7':
                            self.gwa_label.config(text=f'            {line[11]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                            self.grades[7] = float(line[9])
                            self.subject_labels[7].config(text=f"{self.grades[7]}", font=("Helvetica", 10))

                            self.grades[8] = float(line[10])
                            self.subject_labels[8].config(text=f"{self.grades[8]}", font=("Helvetica", 10))

                        elif self.grade_level == line[1] and self.grade_level == 'G8':
                            self.gwa_label.config(text=f'            {line[12]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                            self.grades[7] = float(line[9])
                            self.subject_labels[7].config(text=f"{self.grades[7]}", font=("Helvetica", 10))

                            self.grades[8] = float(line[10])
                            self.subject_labels[8].config(text=f"{self.grades[8]}", font=("Helvetica", 10))

                            self.grades[9] = float(line[11])
                            self.subject_labels[9].config(text=f"{self.grades[9]}", font=("Helvetica", 10))

                        elif self.grade_level == line[1] and self.grade_level == 'G9':
                            self.gwa_label.config(text=f'            {line[12]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                            self.grades[7] = float(line[9])
                            self.subject_labels[7].config(text=f"{self.grades[7]}", font=("Helvetica", 10))

                            self.grades[8] = float(line[10])
                            self.subject_labels[8].config(text=f"{self.grades[8]}", font=("Helvetica", 10))

                            self.grades[9] = float(line[11])
                            self.subject_labels[9].config(text=f"{self.grades[9]}", font=("Helvetica", 10))

                        elif self.grade_level == line[1] and self.grade_level == 'G10':
                            self.gwa_label.config(text=f'            {line[12]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                            self.grades[7] = float(line[9])
                            self.subject_labels[7].config(text=f"{self.grades[7]}", font=("Helvetica", 10))

                            self.grades[8] = float(line[10])
                            self.subject_labels[8].config(text=f"{self.grades[8]}", font=("Helvetica", 10))

                            self.grades[9] = float(line[11])
                            self.subject_labels[9].config(text=f"{self.grades[9]}", font=("Helvetica", 10))

                        elif self.grade_level == line[1] and self.grade_level == 'G11':
                            self.gwa_label.config(text=f'            {line[9]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                        elif self.grade_level == line[1] and self.grade_level == 'G12':
                            self.gwa_label.config(text=f'            {line[9]}             ')

                            self.grades[0] = float(line[2])
                            self.subject_labels[0].config(text=f"{self.grades[0]}", font=("Helvetica", 10))

                            self.grades[1] = float(line[3])
                            self.subject_labels[1].config(text=f"{self.grades[1]}", font=("Helvetica", 10))

                            self.grades[2] = float(line[4])
                            self.subject_labels[2].config(text=f"{self.grades[2]}", font=("Helvetica", 10))

                            self.grades[3] = float(line[5])
                            self.subject_labels[3].config(text=f"{self.grades[3]}", font=("Helvetica", 10))

                            self.grades[4] = float(line[6])
                            self.subject_labels[4].config(text=f"{self.grades[4]}", font=("Helvetica", 10))

                            self.grades[5] = float(line[7])
                            self.subject_labels[5].config(text=f"{self.grades[5]}", font=("Helvetica", 10))

                            self.grades[6] = float(line[8])
                            self.subject_labels[6].config(text=f"{self.grades[6]}", font=("Helvetica", 10))

                        else:
                            self.entry.config(state='normal')
                            self.entry.delete(0, len(self.entry.get()))
                            self.entry.insert(0, 'Wrong grade level.')
                            self.entry.config(state='disabled')
                            self.entry.bind("<Button-1>", self.import_trouble_click)

                        return

                    elif self.in_csv(line) == 'no name':
                        self.entry.delete(0, len(self.entry.get()))
                        self.entry.insert(0, 'Name is blank.')
                        self.entry.config(state='disabled')
                        self.entry.bind("<Button-1>", self.import_trouble_click)

                    elif self.in_csv(line) == 'not in record':
                        self.entry.delete(0, len(self.entry.get()))
                        self.entry.insert(0, 'Name is not in record.')
                        self.entry.config(state='disabled')
                        self.entry.bind("<Button-1>", self.import_trouble_click)

            else:
                self.entry.delete(0, len(self.entry.get()))
                self.entry.insert(0, 'Record is empty.')
                self.entry.config(state='disabled')
                self.entry.bind("<Button-1>", self.import_trouble_click)

    def in_csv(self, line):
        user_entry = self.entry.get()
        if user_entry == '':
            return 'no name'
        elif user_entry == line[0]:
            return 'name exists'
        else:
            return 'not in record'

    def success_click(self, event):
        self.entry.config(state='normal')
        self.entry.delete(0, 10)

    def import_trouble_click(self, event):
        self.entry.config(state='normal')
        self.entry.delete(0, 22)

    @staticmethod
    def label_for_import(labels):
        return labels
