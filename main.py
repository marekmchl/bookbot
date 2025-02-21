def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(words(file_contents))
    print(symbol_count(file_contents))

def words(string):
    words = string.split()
    return len(words)

# Returns a dictionary, symbol->count, of a given string
def symbol_count(input_string):
    result = {}
    lowered_string = input_string.lower()
    # Add all symbols into the result dictionary
    for symbol in lowered_string:
        result[symbol] = 0
    # Count all the symbols in the string
    for symbol in lowered_string:
        result[symbol] += 1

    return result

main()
