import os

FILE = './clippings.txt'

def parse_input(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

def organize_highlights(lines):
    books = {}
    title = ""
    for line in lines:
        if line and not line.startswith("- Your Highlight") and line != "==========":
            if title:
                books[title] = books.get(title, []) + [line]
            else:
                title = line
        elif line == "==========":
            title = ""
    return books

def format_highlights(highlights):
    return "\n\n---\n\n".join(highlights)

def write_highlights_to_files(books, directory="books"):
    os.makedirs(directory, exist_ok=True)
    for title, highlights in books.items():
        file_path = os.path.join(directory, f"{title.replace('/', '-').replace(':', '-')}.md")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(format_highlights(highlights))
        print(f"Highlights for '{title}' written to {file_path}")

def main():
    pairs = parse_input(FILE)
    books = organize_highlights(pairs)
    
    print("Available books:")
    for i, title in enumerate(books.keys()):
        print(f"{i}: {title}")
    print("all: All books")
    
    index = input("Enter a book index: ").strip()
    if index.lower() == "all":
        write_highlights_to_files(books)
    elif index.isdigit() and int(index) < len(books):
        selected_book = list(books.keys())[int(index)]
        write_highlights_to_files({selected_book: books[selected_book]})
    else:
        print("Invalid selection. Exiting.")
        exit()

if __name__ == "__main__":
    main()
