
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


if __name__ == '__main__':
    test()
