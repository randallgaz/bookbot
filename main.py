
def main():
    with open('books/frankenstein.txt') as f:
        content = f.read().lower()
#    print(content)
    chars_dict = dict()
    for c in content:
        if (c.isalpha()):
            if (not c in chars_dict):
                chars_dict[c] = 0
            chars_dict[c] += 1
    ordered_dict = dict(sorted(chars_dict.items(), reverse=True, key=lambda item: item[1]))
 #   print( ordered_dict.items())
#    print(ordered_dict)

    for entry in ordered_dict.items():
        print(entry)
        
main()


        
