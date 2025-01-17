def main():
    path = 'books/frankenstein.txt'
    #with open(path) as f:
    #    file_contents = f.read()
    #print(count_words(file_contents))
    #print(count_characters(file_contents))
    generate_report(path)

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def generate_report(path):
    print(f'--- Begin report of {path} ---')
    with open(path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f'{word_count} words found in the document \n')

        for character, count in count_characters(file_contents).items():
            print(f"The '{character}' character was found {count} times")

main()