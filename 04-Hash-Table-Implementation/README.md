# 🗄️ Hash Table Implementation (Project 4)

## 📝 Project Overview
This project is a deep dive into computer science fundamentals, developed for the **freeCodeCamp Python Certification**. It involves building a **Hash Table** data structure from the ground up, simulating how modern languages handle key-value storage behind the scenes.

## 🛠️ Technical Highlights
* **Manual Hashing Function**: Implemented a logic that iterates through character Unicode values (`ord()`) to generate unique hash keys.
* **Collision Handling Strategy**: To account for multiple keys generating the same hash value, the implementation uses a "bucket" system (nested dictionaries), ensuring that data is never overwritten by a collision.
* **Efficient Lookup (O(1) approach)**: Designed the `lookup` and `add` methods to provide near-constant time complexity for data retrieval.
* **Robust Error Handling**: Methods are engineered to fail gracefully, returning `None` for missing keys instead of crashing the program.

## 🚀 Key Skills Demonstrated
* **Algorithm Design**: Crafting a deterministic hashing process.
* **Data Structure Manipulation**: Managing complex nested collections to maintain data mapping.
* **Memory Logic**: Understanding how keys are transformed into indices (or hash values) for efficient storage.
