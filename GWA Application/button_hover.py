
class ButtonHover:
    def __init__(self, button):
        self.button = button

    def on_enter(self, entry):
        self.button['background'] = 'red'
        self.button['foreground'] = 'blue'

    def on_leave(self, entry):
        self.button['background'] = 'white'
        self.button['foreground'] = 'black'
