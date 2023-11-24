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
    print('+----------------------------------+')
    print('|--- *IO Management Simulation* ---|')
    print('+----------------------------------+\n')
    print('[1] FCFS')
    print('[2] SSTF')
    print('[3] SCAN')
    print('[4] CSCAN')
    print('[5] LOOK')
    print('[6] CLOOK')
    print('[0] Exit\n')


def main():
    """
    Main Function
    :return: None
    """
    while True:
        menu()
        choice = int(input('Enter your choice: '))
        if choice == 0:
            print('Exiting...')
            break
        elif 1 <= choice <= 6:
            clear()
            algorithm_names = {
                1: 'FCFS', 2: 'SSTF', 3: 'SCAN',
                4: 'CSCAN', 5: 'LOOK', 6: 'CLOOK'
            }
            algorithm_name = algorithm_names[choice] + ' Algorithm'
            print(algorithm_name)
            print('------------------------------------')
            io_algorithm.set_algorithm(algorithm_names[choice])
            io_algorithm.simulate()

            # Pause to display results before showing menu again
            input("Press Enter to continue...")
            clear()
        else:
            clear()
            print('Invalid Choice!')


if __name__ == '__main__':
    main()
