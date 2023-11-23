from execution import IO_Execution
from request import IO_Request


class IO_Algorithm:
    """
    This Class is used to simulate the various IO Algorithms
    """

    def __init__(self, io_request):
        """
        Initializes the IO_Algorithm object
        :param io_request: The IO_Request object containing the information about the IO Requests
        """
        self.io_request = io_request
        self.io_execution = IO_Execution(self.io_request.current_track)
        self.Queue = self.io_request.requested_tracks.copy()
        self.simulate()

    def simulate(self):
        """
        Simulates the IO Algorithm
        :return: None
        """
        if (self.io_request.algorithm == 'FCFS'):
            self.fcfs()
        elif (self.io_request.algorithm == 'SSTF'):
            self.sstf()
        elif (self.io_request.algorithm == 'SCAN'):
            self.scan()
        elif (self.io_request.algorithm == 'CSCAN'):
            self.cscan()
        elif (self.io_request.algorithm == 'LOOK'):
            self.look()
        elif (self.io_request.algorithm == 'CLOOK'):
            self.clook()
        else:
            print('Invalid Algorithm!')

    def fcfs(self):
        """
        Simulates the FCFS Algorithm
        :return: None
        """
        while (len(self.Queue) > 0):
            self.io_execution.add_head_movement(self.Queue.pop(0))

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)

    def sstf(self):
        """
        Simulates the SSTF Algorithm
        :return: None
        """
        while (len(self.Queue) > 0):
            min_distance = self.io_request.disk_size + 1
            min_index = -1
            for i in range(len(self.Queue)):
                if (abs(self.Queue[i] - self.io_execution.head_movement_sequence[-1]) < min_distance):
                    min_distance = abs(
                        self.Queue[i] - self.io_execution.head_movement_sequence[-1])
                    min_index = i
            self.io_execution.add_head_movement(self.Queue.pop(min_index))

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)

    def scan(self):
        """
        Simulates the SCAN Algorithm
        :return: None
        """
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Reverse direction and move towards the lowest track
        current_track = highest_track - 1
        while current_track >= lowest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track -= 1

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)

    def cscan(self):
        """
        Simulates the C-SCAN Algorithm
        :return: None
        """
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Move towards the lowest track
        current_track = lowest_track
        while current_track < self.io_request.disk_size:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)

    def look(self):
        """
        Simulates the LOOK Algorithm
        :return: None
        """
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Reverse direction and move towards the lowest track
        current_track = highest_track - 1
        while current_track >= lowest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track -= 1

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)

    def clook(self):
        """
        Simulates the C-LOOK Algorithm
        :return: None
        """
        current_track = self.io_request.current_track
        highest_track = max(self.Queue)
        lowest_track = min(self.Queue)

        # Move towards the highest track
        while current_track <= highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        # Move towards the lowest track
        current_track = lowest_track
        while current_track < highest_track:
            if current_track in self.Queue:
                self.io_execution.add_head_movement(current_track)
                self.Queue.remove(current_track)
            current_track += 1

        print()
        print('Head Movement Sequence:',
              self.io_execution.head_movement_sequence)
        print('Total Head Movements:', self.io_execution.total_head_movements)


def main():
    """
    Main Function
    :return: None
    """
    io_request = IO_Request()
    io_request.read_input('OS\IOManagement\input.txt')
    # io_request.take_input()
    io_request.print_input()

    io_algorithm = IO_Algorithm(io_request)


if __name__ == '__main__':
    main()
