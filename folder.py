import time
import curses
import subprocess
import os
from ScriptRunner.ui.util import debug, option_loop
from bash_script import Bash_Script

# TODO: THINKING ABOUT HOW TO MAKE THE SCRIPT MENU AND FOLDER MENU TO BE ABLE TO USE THE SAME FUNCTION - maybe try doing enumerations - maybe change the last option from auto
# opening a new Folder to be a function pointer. Maybe create a new class called Script and delegate from that class

class Folder:
    def __init__(self, stdscr, dir):
        self._dir = dir + "/"
        self._inner_folders = []
        self._bash_scripts = []

        self._get_contents()
        self.hight, self.width = stdscr.getmaxyx()
        if self.hight < len(self._inner_folders) + len(self._bash_scripts):
            self.hight = len(self._inner_folders) + len(self._bash_scripts)
        
        self._stdscr = curses.newpad(self.hight, self.width)
        self._stdscr.keypad(1)
        
    def _get_contents(self):
        if not os.path.isdir(self._dir):
            # debug(self._stdscr, '{} is not a valid directory'.format(self._dir))
            return -1
        try:
            folder_contents = subprocess.run(['ls', self._dir], stdout=subprocess.PIPE).stdout.decode('utf-8')
            self._all_contents = folder_contents.split('\n')

            for item in self._all_contents:
                if os.path.isdir(self._dir + item):
                    self._inner_folders.append(item)
                elif item[-3::] == '.sh':
                    self._bash_scripts.append(item)
            self._all_contents.append('Return')
        except Exception as e:
            pass
            # debug(self._stdscr, e)

    def launch(self):
        choice_index = 0
        has_chosen = False
        while True:
            start_index = 0
            while not has_chosen:
                start_index += choice_index
                if start_index < 0 or start_index > len(self._all_contents):
                    start_index = 0

                screen_options = self._all_contents[start_index:start_index+self.hight-1:]
                choice_index, has_chosen = option_loop(self._stdscr, screen_options, start_index == 0, start_index +self.hight < len(self._all_contents))
            choice_index += start_index
            choice = self._all_contents[choice_index]
            # debug(self._stdscr, self._dir + choice)
            # debug(self._stdscr, str(self._bash_scripts) + choice)
            if choice in self._inner_folders:
                inner = Folder(self._stdscr, self._dir + choice)
                inner.launch()
            elif choice in self._bash_scripts:
                script = Bash_Script(self._dir + choice)
                debug(self._stdscr, str(script._argv_labels))
            if choice_index == len(self._all_contents) - 1:
                break
            print("Hi")
            # debug(self._stdscr, str(choice_index))
            start_index = 0
            has_chosen = False
        
    # def _get_menu_options(self):
    #     if not os.path.isdir(self._dir):
    #         debug(self._stdscr, "{} is not a valid directory".format(self._dir))
    #         return -1
    #     try:
    #         start = 0
    #         debug(self._stdscr, folder_contents)
    #         for idx, c in enumerate(folder_contents):
    #             # debug(self._stdscr, c.encode())
    #             if c == '\n':
    #                 option = folder_contents[start: idx]
    #                 start = idx + 1
    #                 if option[-3::] == ".sh":
    #                     self._has_script = True
    #                     self._scripts.append(self._dir + option)
    #                 if os.path.isdir(self._dir + option):
    #                     self._menu_options.append(option)

    #         if self._has_script:
    #             self._menu_options.append("Run a script")
    #             self._scripts.append("Never Mind")

    #         self._menu_options.append('Up a level')
    #     except Exception as e:
    #         print("Unable to create menu options")
    #         print(e)

    # def _print_options(self):
    #     self._stdscr.clear()
    #     h, w = self._stdscr.getmaxyx()
    #     title_x = w//2 - len(self._dir)//2
    #     self._stdscr.addstr(0, title_x, self._dir)

    #     for idx, row in enumerate(self._menu_options):
    #         x = w//2 - len(row)//2
    #         y = h//2 - len(self._menu_options)//2 + idx
    #         if idx == self._selected_row_index:
    #             self._stdscr.attron(curses.color_pair(1))
    #             self._stdscr.addstr(y, x, row)
    #             self._stdscr.attroff(curses.color_pair(1))
    #         else:
    #             self._stdscr.addstr(y, x, row)

    #     self._stdscr.refresh()

    # def _script_options(self):
    #     debug(self._stdscr, "This will be an input for scripts")

    # def menu_loop(self):
        
    #     while 1:
    #         self._print_options()
    #         self._stdscr.refresh()

    #         key = self._stdscr.getch()

    #         self._stdscr.clear()

    #         if key == curses.KEY_UP and self._selected_row_index > 0:
    #             self._selected_row_index -=1
    #         elif key == curses.KEY_DOWN and self._selected_row_index < len(self._menu_options) -1:
    #             self._selected_row_index +=1
    #         elif key == curses.KEY_ENTER or key in [10, 13]:
    #             if self._has_script and self._selected_row_index == len(self._menu_options) - 2:
    #                 self._script_options()
    #                 continue
    #             if self._selected_row_index == len(self._menu_options) - 1:
    #                 break
    #             selected = Folder(self._stdscr, self._dir + self._menu_options[self._selected_row_index])
    #             selected.menu_loop()
