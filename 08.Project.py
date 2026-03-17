def load_cons(filename):
    with open(filename, "r") as file:
        return [line.rstrip("\n") for line in file] #removes linefeed

def find_section(lines, index):
    start = index
    while start > 0 and lines[start].strip() != "":
        start -= 1
    end = index
    while end < len(lines) and lines[end].strip() != "":
        end += 1
    return start, end

def search_cons(lines, term):
    i = 0
    found = False
    while i < len(lines):
        if term.lower() in lines[i].lower():
            start, end = find_section(lines, i)

            for j in range(start, end + 1):
                if j < len(lines):
                    print(f"Line {j}: {lines[j]}")

            print() 

            found = True
            i = end + 1  
        else:
            i += 1

    if not found:
        print("No matches found.\n")


def main():
    lines = load_cons("constitution.txt")
    while True:
        term = input("Enter search term: ").strip()
        if term == "":
            break

        search_cons(lines, term)

if __name__ == "__main__":
    main()