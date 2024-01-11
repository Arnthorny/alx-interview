#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def append_recurse(unique_boxes, box, boxes):
    """
    This recursive function appends each box uniquely

    Once box is opened, this function uses the keys there
    to access their respective boxes and it also checks if
    a box had not been visited before.
    """

    if box in unique_boxes:
        return

    if box != 0:
        unique_boxes.append(box)
    for key in boxes[box]:
        append_recurse(unique_boxes, key, boxes)


def canUnlockAll(boxes):
    """
    Arg:
        boxes(`list`): List of lists

    Description:
        A key with the same number as a box opens that box
        You can assume all keys will be positive integers
        There can be keys that do not have boxes
        The first box boxes[0] is unlocked

    Return:
        True if all boxes can be opened, else return False
    """
    opened_boxes = []

    for key in boxes[0]:
        append_recurse(opened_boxes, key, boxes)

    return len(opened_boxes) == len(boxes) - 1
