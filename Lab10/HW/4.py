def print_table(table):
    if not table:
        print("Table is empty.")
        return

    column_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
    header = table[0]
    for i, column in enumerate(header):
        print(f"{column:{column_widths[i]}}", end=" ")
    print()

    for row in table[1:]:
        for i, value in enumerate(row):
            print(f"{value:{column_widths[i]}}", end=" ")
        print()

table1 = [
["X", "Y"],
["10", "10"],
["10", "10"],
[200, 200]
]

table2 = [
["ID", "Name", "Surname"],
["001", "Guido", "van Rossum"],
["002", "Donald", "Knuth"],
["003", "Gordon", "Moore"]
]

print_table(table1)
print()
print_table(table2)
