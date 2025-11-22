# CAFE-TABLE
This is a cli app use to create a table for coffee ordering

## Feature
Command:
- "add" to add new order
- "list" to show a whole table
- "delete" or "del" + ID(from 1 to n) to delete a order
- "reset" or "res" to clear whole table

## installation
from Pypi
```bash
pip install cafe-table
```

from source code
```bash
git clone <link_github_repo>
cd cafe-table
pip install .
```

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
cafe res
```
