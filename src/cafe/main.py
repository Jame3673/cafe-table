import json
import sys
from pathlib import Path


FILE = Path("table.json")

def load():
    if not FILE.exists():
        return[]
    content = FILE.read_text().strip()
    if not content:
        FILE.write_text("[]")
        return []
    return json.loads(content)

def save(table):
    FILE.write_text(json.dumps(table, indent=2))

def add():
    table = load()
    new_id = 1 if not table else table[-1]['id'] + 1 

    coffee = input('coffee: ').strip()
    customer = input('customer: ').strip()
    note = input('note: ').strip()

    if not coffee:
        coffee = "normal"
    if not customer:
        print("CUSTOMER NOT FOUND")
        return
    if not note:
        note = "X"

    entry = {
        'id': new_id,
        'coffee': coffee,
        'customer': customer,
        'note': note
    }

    table.append(entry)
    save(table)
    #print(json.dumps(entry, indent=2))  #Print the json data
    print('Coffee order added.')

def list_table():
    table = load()
    if not table:
        print('Order not found')
        return 
    print(f"id |    coffee    |    customer    |    note")
    for entry in table:
        print(f"{entry['id']}  |    {entry['coffee']}    |    {entry['customer']}    |    {entry['note']}")

def delete(id_):
    table = load()
    original_len = len(table)
    table = [t for t in table if t['id'] != id_]
    save(table)
    if len(table) < original_len:
        print('order removed')
    else:
        print('order not found')

def reset():
    save([])
    print("All orders cleared.")


def main():
    if len(sys.argv) < 2:
        print("Commands: add, list, del, delete, reset")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add()

    elif command == "list":
        list_table()

    elif command in ("del", "delete"):
        if len(sys.argv) < 3:
            print('Missing ID. Usage: python main.py del <id>')
        else:
            try:
                id_to_delete = int(sys.argv[2])
            except ValueError:
                print("ID must be a number")
            else:
                delete(id_to_delete)

    elif command in ("res", "reset"):
        reset()


    else:
        print("command not found")


if __name__ == "__main__":
    main()

