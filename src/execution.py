class IO_Execution:
    """
    This Class is used to store the information about the execution of the IO Requests
    This Class is also used for useful calculations about the execution of the IO Requests
    """

    def __init__(self, current_track):
        self.head_movement_sequence = []  # The sequence of the head movements
        self.head_movement_sequence.append(current_track)
        self.total_head_movements = 0  # The total number of head movements

    def add_head_movement(self, head_movement):
        """
        Adds a head movement to the head_movement_sequence
        This will systematically update the total_head_movements
        :param head_movement: The head movement to be added
        :return: None
        """
        if (head_movement > self.head_movement_sequence[-1]):
            self.total_head_movements += head_movement - \
                self.head_movement_sequence[-1]
        else:
            self.total_head_movements += self.head_movement_sequence[-1] - \
                head_movement
        self.head_movement_sequence.append(head_movement)

    def get_head_movement_sequence(self):
        """
        Returns the head movement sequence
        :return: The head movement sequence
        """
        return self.head_movement_sequence

    def get_total_head_movements(self):
        """
        Returns the total number of head movements
        :return: The total number of head movements
        """
        return self.total_head_movements

    def print(self):
        """
        Prints the graph of the head movement sequence
        :return: None
        """
        for i in range(len(self.head_movement_sequence)):
            print('Track', i, ':', self.head_movement_sequence[i])
        print('------------------------------------')
        print('Total Head Movements:', self.total_head_movements)
        print('------------------------------------')




def test():
    """
    Test function
    :return: None
    """

    io_execution = IO_Execution(70)
    io_execution.add_head_movement(118)
    io_execution.add_head_movement(59)
    io_execution.add_head_movement(110)
    io_execution.add_head_movement(25)
    io_execution.add_head_movement(105)
    io_execution.add_head_movement(63)
    io_execution.add_head_movement(100)
    io_execution.add_head_movement(28)
    io_execution.add_head_movement(80)

    print()
    print('Head Movement Sequence:', io_execution.head_movement_sequence)
    print('Total Head Movements:', io_execution.total_head_movements)
    print()
    io_execution.print_graph_gui()


if __name__ == '__main__':
    test()
