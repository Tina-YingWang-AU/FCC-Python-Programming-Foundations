# 📐 Polygon Area Calculator (Project 3)

## 📝 Project Overview
This project, developed for the **freeCodeCamp Python Certification**, implements a geometric shape calculator. It focuses on using Object-Oriented Programming (OOP) to model rectangles and squares, showcasing how inheritance can simplify code structure and logic.

## 🛠️ Technical Highlights
* **Inheritance & Subclassing**: The `Square` class inherits directly from the `Rectangle` class, efficiently reusing methods for area, perimeter, and diagonal calculations.
* **Method Overriding**: Specifically redefined setter methods in the `Square` class to ensure the side length remains consistent for all dimensions, maintaining the mathematical integrity of a square.
* **Super() Integration**: Utilizes the `super().__init__` call to bridge the parent and child classes during instantiation.
* **Dynamic Visualization**: Features a `get_picture` method that renders the shape using ASCII characters (`*`), including error handling for oversized shapes.
* **Spatial Calculation**: Implements `get_amount_inside`, a logic-based method to determine how many times one shape can fit inside another based on area.

## 🚀 Key Skills Demonstrated
* **OOP Inheritance**: Understanding how to share functionality between related classes.
* **Polymorphism**: Using the same method interface to produce different outputs based on the object type.
* **Mathematical Implementation**: Translating geometric formulas ($Area = w \times h$) into clean, executable Python code.
