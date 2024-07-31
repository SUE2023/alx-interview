#!/usr/bin/python3
""" Method to unlock all boxes - graph representation"""


def canUnlockAll(boxes):
    """ Determines if all boxes can be opened"""
    if not boxes:
        return False
    
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked
    
    queue = [0]  # Start with the first box
    
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
    
    return all(visited)
