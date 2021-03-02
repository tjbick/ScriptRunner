import curses

class Screen:
    def __init__(self, parentScreen, title, folder):
        self.folder = folder
        #adding this to see if it gits changed
        self.rows, self.columns = parentScreen.getmaxyx()
        if self.rows < len(self.folder._all_contents):
            self.rows = self.folder._all_contents

        self.pad = curses.newpad(self.rows, self.columns)
        self.pad.keypad(True)
