#!/usr/bin/python3
"""
This python file implements a singly linked list
"""


class Node:
    """
    This class defines a node. it has the properties:
    data: the value of the node
    next_node: points to the next node in the linked list
    """

    def __init__(self, data=0, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """int: returns the value of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set value of next node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a linked list.
    it sets up the linked list and keeps track of it
    """

    def __init__(self):
        """initializes the node with instance variables"""
        self.__head = None

    def sorted_insert(self, value):
        """
        testing to see if my headache goes away
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head

            while temp.data < value and temp.next_node is not None\
                    and temp.next_node.data < value:
                temp = temp.next_node

            if temp == self.__head and value < temp.data:
                new_node.next_node = temp
                self.__head = new_node
                return

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """
        testing to see if my headache goes away
        """
        output = ""
        temp = self.__head

        while temp is not None:
            output += str(temp.data)
            output += "\n"
            temp = temp.next_node

        return output
