def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()  # Reads all lines into a list
    print(f"Number of lines: {len(lines)}")

count_lines("sometext.txt")