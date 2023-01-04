#!/usr/bin/python3
"""Matrix multiplication module"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices"""

    """tests"""


    """code that does actual work"""
    matrix = []
    b_length = len(m_b[0])
    a_height = len(m_a)
    for list1 in m_a:
        matrix_row = []
        a_index = 0
        b_index = 0
        matrix_row_item = 0
        for number, list2 in zip(list1*b_length, m_b*b_length):


