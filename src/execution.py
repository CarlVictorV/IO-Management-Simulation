class IO_Execution:
    """
    This Class is used to store the information about the execution of the IO Requests
    This Class is also used for useful calculations about the execution of the IO Requests
    """

    def __init__(self):
        self.head_movement_sequence = []  # The sequence of the head movements
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