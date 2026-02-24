# 💰 Budget App (Project 2)

## 📝 Project Overview
Developed as part of the **freeCodeCamp Python Certification**, this application is a sophisticated budget tracking system. It allows users to create multiple budget categories, manage a ledger of transactions, and visualize spending distributions through a custom-built bar chart.

## 🛠️ Technical Highlights
* **Object-Oriented Programming (OOP)**: Utilizes a `Category` class to manage independent ledgers, providing a clean structure for deposits, withdrawals, and balance tracking.
* **Complex Transaction Logic**: Implements a robust `transfer` system that handles inter-category movements while ensuring sufficient funds are available.
* **Custom String Representation**: Overrides the `__str__` method to generate formatted, alignment-perfect receipts using `.ljust()`, `.rjust()`, and `.center()`.
* **Data Visualization Algorithm**: Features a specialized function `create_spend_chart` that calculates spending ratios and renders a vertical ASCII bar chart from scratch, demonstrating advanced loop and coordinate logic.

## 🚀 Key Skills Demonstrated
* **Encapsulation**: Keeping data (ledger) and methods (deposit/withdraw) bundled within class instances.
* **Algorithm Design**: Crafting the logic to round down percentages and transpose text for vertical display on the chart's X-axis.
* **Precision Formatting**: Handling floating-point numbers and string slicing to maintain a consistent UI layout.
