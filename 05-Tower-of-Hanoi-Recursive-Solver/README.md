# 🗼 Tower of Hanoi Recursive Solver (Project 5)

## 📝 Project Overview
This final project for the **freeCodeCamp Python Certification** is a mathematical solver for the legendary Tower of Hanoi puzzle. It demonstrates a deep understanding of **recursive functions** and state management in Python.

## 🛠️ Technical Highlights
* **Recursive Problem Solving**: Solves the puzzle by breaking it down into three logical steps: moving the $n-1$ stack to a helper rod, moving the largest disk to the target, and finally moving the $n-1$ stack to the target.
* **Stack Data Structure**: Utilizes Python lists as **Stacks** (`pop` and `append`) to represent the physical constraints of the rods (Last-In, First-Out).
* **Step-by-Step History**: Implements a recording mechanism that tracks the distribution of disks across all rods at every single step, allowing for a complete audit of the solution.
* **Base Case Logic**: Features a robust recursion base case to prevent infinite loops and ensure mathematical correctness.

## 🚀 Key Skills Demonstrated
* **Recursive Thinking**: The ability to visualize and code solutions for self-referential problems.
* **State Visualization**: Transforming internal list data into a readable string-based history.
* **Computational Logic**: Managing rod indices and disk movements accurately across recursive calls.
