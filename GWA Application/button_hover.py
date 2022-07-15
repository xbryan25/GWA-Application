
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

        elif self.button_type == 'g7_button':
            if self.sign == 'minus':
                self.button['background'] = '#DB5F44'
                self.button['foreground'] = 'black'
            if self.sign == 'add':
                self.button['background'] = '#DB5F44'
                self.button['foreground'] = 'black'

    def on_leave(self, entry):
        if self.button_type == 'calculate' or 'credits':
            self.button['background'] = 'white'
            self.button['foreground'] = 'black'

        elif self.button_type == 'back_button':
            self.button['background'] = 'white'
            self.button['foreground'] = 'black'

        elif self.button_type == 'grade_level_button':
            self.button['background'] = 'white'
            self.button['foreground'] = 'black'

        elif self.button_type == 'save_button':
            self.button['background'] = 'white'
            self.button['foreground'] = 'black'

        elif self.button_type == 'import_button':
            self.button['background'] = 'white'
            self.button['foreground'] = 'black'

        elif self.button_type == 'g7_button':
            if self.sign == 'minus':
                self.button['background'] = 'white'
                self.button['foreground'] = 'black'
            if self.sign == 'add':
                self.button['background'] = 'white'
                self.button['foreground'] = 'black'
