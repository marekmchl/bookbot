def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(words(file_contents))

def words(string):
    words = string.split()
    return len(words)

main()
