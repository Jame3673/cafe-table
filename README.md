# CAFE-TABLE
This is a cli app use to create a table for coffee ordering

## Feature
Command:
- "add" to add new order
- "list" to show a whole table
- "delete" or "del" + ID(from 1 to n) to delete a order
- "reset" or "res" to clear whole table

## installation

from source code
```bash
git clone https://github.com/Jame3673/cafe-table
cd cafe-table
pip install .
```
NOTE*: make sure you have python on your computer, if you don't have [click me](https://www.python.org/downloads/)

## Uasge
```bash
# Add order
cafe add

# Show order
cafe list

# Delete order with ID
cafe delete <id>
cafe del <id>

# Delete table
cafe reset
cafe rs
```
