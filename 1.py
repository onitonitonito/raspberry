import os, sys, csv, random
from datetime import datetime
# from sense_HAT import func_HAT as fh    # get_sense, TABLE

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_variable():
    global DESTIN_DIR, MY_HAT, HELP_MESSAGE, HEADER

    DESTIN_DIR='./data_doc/'
    MY_HAT = 'log_HAT.pdb'

    HELP_MESSAGE='''\n\n\
    ====================================================
               log_HAT.PY -- HELP MESSAGE
    ---------------------------------------------------
    This is simple example of read & write file funtion

    USAGE:    python log_HAT.py {mode}, [args1]
    =====
       -a, --append:     ADD log = args1
       -v, --verbose:    VIEW log w/o args1
    ----------------------------------------------------
    '''

    HEADER='''\n
    ====================================================
            %s
    ----------------------------------------------------'''


def is_dir():
    if not os.path.isdir(DESTIN_DIR):
        os.mkdir(DESTIN_DIR)
        return False
    else: 
        return True


def is_logfile():
    if not os.path.exists(DESTIN_DIR+MY_HAT):
        f = open(DESTIN_DIR+MY_HAT, 'w', encoding='utf8')
        f.write('****** START LOG : time_log(6), temp, humid, press \n')
        f.close()     # write HEADER in 1st.line
        return False
    else: 
        return True


def count_lines():      # return <class 'int'>
    with open(DESTIN_DIR+MY_HAT, 'r') as f:
         line_number = len(f.readlines())        # len(<class 'list'>)
    return line_number


def add_lines():
    # sense = fh.get_sense(fh.hat)   # <class 'dict'> -- temp, humid, press
    sense = {
        'temp': random.randint(800,1000),
        'humid': random.randint(800,1000),
        'press': random.randint(800,1000),
    }

    dt = datetime.now()
    ctime = dt.strftime("%l:%M:%S, %p, %Y-%m-%d") # pm 05:34:57 July 16 Mon 2017
    data = ctime + ", %s, %s, %s\n" % (sense['temp'], sense['humid'], sense['press'])
    lines = count_lines()   # get <class 'int'>

    with open(DESTIN_DIR+MY_HAT, 'a', encoding='utf8') as f:
        print("%s-line's added=" % str(lines+1), data)
        f.write(data)


def read_file():
    with open(DESTIN_DIR+MY_HAT, 'r', encoding='utf8') as f:
        int_number = count_lines()    # <class 'int'>
        for n in range(int_number):
            line = f.readline()
            print(line, "")


def is_argv():      # False or True
    if len(sys.argv) < 2:
        return False
    else:
        return True


def is_argv_act():      # False or True
    if is_argv() == False:
        print('\n**** ERR: YOU NEED MORE THAN 1 Argv(option)! ****')
        print(HELP_MESSAGE)
        raise SystemExit(1)         # Exception and forced shutdown.
    else:
        option = sys.argv[1]        # [ argv_list, args1, args2...]
        MESSAGE = "LOG OPTION: "+option
        print(HEADER % MESSAGE)


def plot_bars_lines(data, title=None):
    data = pd.Series(data)
    num_data = len(data)
    scale_width = 0.6

    x = np.arange(0, num_data, 1)
    y = data.values

    plt.figure(figsize=(num_data * scale_width, 5))          # window size
    plt.plot(y, 'rs--')                 # line plot - trends
    plt.title(title)

    for x,y in zip(x,y):                # Bar chart
        plt.bar(x, y, facecolor='#ffaaaa', edgecolor='grey')
        plt.text(x, y+0.05, '%.1f'%y, ha='center', va= 'bottom')

    plt.grid()
    plt.show()


def get_chosen_data(pos, find_key):
    header = []             # <class 'list'>
    CHOSEN_DATA = []        # <class 'list' in 'list'>

    with open(DESTIN_DIR + MY_HAT, 'r', encoding='utf8') as pop_file:
        csv_data = csv.reader(pop_file) # Data reading using CSV object
        row_num = 0                     # when row_list[0] = header

        for row_list in csv_data:       # csv_dara = <class 'csv.reader'> = object type
            if row_num == 0:
                header = row_list
                row_num +=1

            if row_list[pos].find(find_key) != -1:   # find()= position call
                CHOSEN_DATA.append(row_list)
                row_num +=1

    return CHOSEN_DATA


def get_split_data(find_pos=0, find_key=None, get_pos=0):
    result = get_chosen_data(pos=find_pos, find_key=find_key)

    arr_parameter = []
    for n in range(len(result)):
        arr_parameter.append(int(result[n][get_pos]))
    return arr_parameter


def get_setup():
    if is_argv() == False:
        is_argv_act() # do raise = break

    is_dir()          # if not = make!
    is_logfile()      # if not = make & add header!


get_variable()
get_setup()

arr_temp = get_split_data(find_pos=2, find_key='2017', get_pos=3)
arr_humid = get_split_data(find_pos=2, find_key='2017', get_pos=4)
arr_press = get_split_data(find_pos=2, find_key='2017', get_pos=5)

def main():
    # add_lines()
    # dt = datetime.now()
    # plot_bars_lines(data1,title='Temperature: %s' % dt.strftime('%Y-%m-%d'))

    # check_sum
    print('Temp  =', arr_temp )
    print('Humid =', arr_humid )
    print('Press =', arr_press )

    plot_bars_lines(pd.Series(arr_temp ), title='Temperature')
    plot_bars_lines(pd.Series(arr_humid), title='Humidity')
    plot_bars_lines(pd.Series(arr_press), title='Pressure')


if __name__ == '__main__':
    main()

