
class ButtonHover:
    def __init__(self, button, button_type, sign=None):
        self.button = button
        self.button_type = button_type

        if sign is not None:
            self.sign = sign

    def on_enter(self, entry):
        if self.button_type == 'calculate' or self.button_type == 'credits':
            self.button['background'] = '#9F9E9D'
            self.button['foreground'] = 'black'

        elif self.button_type == 'back_button':
            self.button['background'] = '#DB5F44'
            self.button['foreground'] = 'black'

        elif self.button_type == 'grade_level_button':
            self.button['background'] = '#9F9E9D'
            self.button['foreground'] = 'black'

        elif self.button_type == 'save_button':
            self.button['background'] = '#9F9E9D'
            self.button['foreground'] = 'black'

        elif self.button_type == 'import_button':
            self.button['background'] = '#9F9E9D'
            self.button['foreground'] = 'black'

        elif self.button_type == 'subject_button':
            if self.sign == 'minus':
                self.button['background'] = '#FF5649'
                self.button['foreground'] = 'black'
            elif self.sign == 'add':
                self.button['background'] = '#78E93D'
                self.button['foreground'] = 'black'

    def on_leave(self, entry):
        if self.button_type == 'calculate' or self.button_type == 'credits':
            self.button['background'] = '#E2E2E2'
            self.button['foreground'] = 'black'

        elif self.button_type == 'back_button':
            self.button['background'] = '#E2E2E2'
            self.button['foreground'] = 'black'

        elif self.button_type == 'grade_level_button':
            self.button['background'] = '#E2E2E2'
            self.button['foreground'] = 'black'

        elif self.button_type == 'save_button':
            self.button['background'] = '#E2E2E2'
            self.button['foreground'] = 'black'

        elif self.button_type == 'import_button':
            self.button['background'] = '#E2E2E2'
            self.button['foreground'] = 'black'

        elif self.button_type == 'subject_button':
            if self.sign == 'minus':
                self.button['background'] = '#E2E2E2'
                self.button['foreground'] = 'black'
            elif self.sign == 'add':
                self.button['background'] = '#E2E2E2'
                self.button['foreground'] = 'black'
