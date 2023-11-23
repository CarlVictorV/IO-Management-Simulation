import os
import management as m

io_request = m.IO_Request()
io_algorithm = m.IO_Algorithm(io_request)

if os.name != 'nt':
    io_request.read_input(r"src/input.txt")
else:
    io_request.read_input(r'src\input.txt')


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """
    Displays the Menu
    :return: None
    """
    print('[1] FCFS')
    print('[2] SSTF')
    print('[3] SCAN')
    print('[4] CSCAN')
    print('[5] LOOK')
    print('[6] CLOOK')
    print('[0] Exit')


def main():
    """
    Main Function
    :return: None
    """
    while True:
        menu()
        choice = int(input('Enter your choice: '))
        if (choice == 0):
            print('Exiting...')
            break
        elif (choice == 1):
            clear()
            print('FCFS Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('FCFS')
            io_algorithm.simulate()
        elif (choice == 2):
            clear()
            print('SSTF Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('SSTF')
            io_algorithm.simulate()
        elif (choice == 3):
            clear()
            print('SCAN Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('SCAN')
            io_algorithm.simulate()
        elif (choice == 4):
            clear()
            print('CSCAN Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('CSCAN')
            io_algorithm.simulate()
        elif (choice == 5):
            clear()
            print('LOOK Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('LOOK')
            io_algorithm.simulate()
        elif (choice == 6):
            clear()
            print('CLOOK Algorithm')
            print('------------------------------------')
            io_algorithm.set_algorithm('CLOOK')
            io_algorithm.simulate()
        else:
            clear()
            print('Invalid Choice!')


if __name__ == '__main__':
    main()
