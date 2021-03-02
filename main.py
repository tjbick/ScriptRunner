
from folder import Folder
import curses
import time
from ScriptRunner.ui.util import option_loop

def main(stdscr):
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    main_menu = ['Homework', 'Labs', 'Exit']
    base_folder = '/users/groups/cs324ta/grading'

    home = Folder(stdscr, base_folder)
    home.launch()

    # chosen = option_loop(stdscr, main_menu)
    # if main_menu[chosen] != 'Exit':
    #     print('This is where we go into the folder')
    # else
    #     print ('The end')
    #     return
    # stdscr.addstr(y,x, "Hello, which would you like to grade: homeworks or a labs?")
    # base_folder = Folder(stdscr, "/users/groups/cs324ta/grading")
    # base_folder.menu_loop()
    # _get_menu_options()

curses.wrapper(main)
# _get_menu_options("/users/groups/cs324ta/grading/")
# print(MENU_OPTIONS)