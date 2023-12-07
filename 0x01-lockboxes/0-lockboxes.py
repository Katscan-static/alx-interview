#!/usr/bin/python3
"""
    this module checks if all boxes have keys to open all boxes
"""

def canUnlockAll(boxes):
    """
        canUnlockAll:
            this function check if all boxes can be unlocked

        Args:
            boxes (array): a box with keys to other boxes

        Returns:
            boolean: returns True if all boxes can be opened or else false
    """

    visited = {0}
    keys = boxes[0]

    while keys:
            new_keys = []
            for key in keys:
                if key < len(boxes) and key not in visited:
                    visited.add(key)
                    new_keys.extend(boxes[key])

            keys = new_keys

    return len(visited) == len(boxes)
