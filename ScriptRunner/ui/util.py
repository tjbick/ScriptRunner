import curses
import time

def debug(stdscr, output):
    stdscr.clear()
    y,x=stdscr.getmaxyx()
    stdscr.addstr(0,0, output)
    stdscr.refresh(0,0, 0, 0,y,x )
    stdscr.getch()

def _print_options(stdscr, options, index):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    y = -1
    # debug(stdscr, str(y))
    for idx, row in enumerate(options):
        x = w//2 - len(row)//2
        y += 1
        # debug(stdscr, str(y))
        if idx == index:
            stdscr.attron(curses.color_pair(1))
            # stdscr.addstr(y, x, row)
            rows_used = _addstr(stdscr, y, x, row)

            stdscr.attroff(curses.color_pair(1))
        else:
            # stdscr.addstr(y, x, row)
            rows_used = _addstr(stdscr, y, x, row)
        if rows_used > 1:
            y += rows_used -1
    stdscr.refresh(0, 0, 0, 0, h, w)
   

def option_loop(stdscr, options, is_first, has_more):
    current_index = 0
    while 1:
        _print_options(stdscr, options, current_index)
        
        key = stdscr.getch()
        stdscr.clear()
        # debug(stdscr, "Got a key {}".format(key))
        if key == curses.KEY_UP:
            # debug(stdscr, "Got up key")
            if current_index == 0:
                if not is_first:
                    return current_index - 10, False
                else:
                    continue
            current_index -=1
        
        elif key == curses.KEY_DOWN:
            # debug(stdscr, "Got down key")
            if current_index == len(options) - 1:
                if has_more:
                    return current_index, False
                else:
                    continue
            current_index +=1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            # debug(stdscr, "Got enter key")
            return current_index, True
                # if self._has_script and current_index == len(options) - 2:
                #     self._script_options()
                #     continue
                # if current_index == len(options) - 1:
                #     break
                # # functionOnSelection(self._stdscr, self._dir + options[current_index])
                # print("This will call the funciton that you give as the third argument")

# This will return how many rows were written
def _addstr(stdscr, row, column, output):
    y, x = stdscr.getmaxyx()
    chars_to_write = len(output)
    num_rows_used = 0
    while chars_to_write > x:
        # debug(stdscr, "This one is too long")
        stdscr.addstr(row + num_rows_used, column, output[(num_rows_used*x):x:])
        num_rows_used += 1
        chars_to_write -= x
    # debug(stdscr, "row = {}, num_rows_used = {}".format(row, num_rows_used))
    stdscr.addstr(row + num_rows_used, column, output[(num_rows_used*x):chars_to_write:])

    return num_rows_used + 1
    
