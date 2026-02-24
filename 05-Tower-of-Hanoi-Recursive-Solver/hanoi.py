"""
Project 5: Tower of Hanoi Solver
Part of the freeCodeCamp "Python Certification" (Python v9)

Key Features:
- Recursive Algorithm: Implements the classic recursive solution for the Tower of Hanoi puzzle.
- State Tracking: Captures the visual state of all three rods after every move.
- Dynamic Disk Management: Uses list stacks to simulate physical movement of disks.
- Complexity: Demonstrates O(2^n) exponential time complexity management.
"""

def hanoi_solver(n):
    rods = [list(range(n,0,-1)),[],[]]

    history = []

    def move(number, start, middle,end):
        if number == 1: # Base case
            current_disk = rods[start].pop()
            rods[end].append(current_disk)
            history.append(" ".join([str(rods[0]), str(rods[1]), str(rods[2])]))
        else:   # To move n disks:
                # - Move n‑1 disks from A to B
                # - Move the last disk from A to C
                # - Move n‑1 disks from B to C
            move(number-1, start,end,middle)  # recursion
            move(1, start,middle,end)  # recursion
            move(number-1, middle,start,end)  # recursion

    history.append(" ".join([str(rods[0]), str(rods[1]), str(rods[2])]))
    move(n, 0, 1, 2)
    return "\n".join(history)

print(hanoi_solver(5))
