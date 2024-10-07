
def main():
    with open('books/frankenstein.txt') as f:
        content = f.read()
    print(content)

    count = content.split()
    print(len(count))


main()


        
