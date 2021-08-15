def formatter():
    Avl_formatter = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list',
                     'unordered-list']
    spec_formatter = ['!help', '!done']
    string = [""]
    while True:
        choice = input('Choose a formatter:')
        if choice in Avl_formatter:
            if choice == 'plain':
                string[len(string)-1] = plain(string[len(string)-1])
                lis_print(string)
            elif choice == 'new-line':
                string.append("")
                lis_print(string)
            elif choice == 'bold':
                string[len(string)-1] = bold(string[len(string)-1])
                lis_print(string)
            elif choice == 'italic':
                string[len(string)-1] = italic(string[len(string)-1])
                lis_print(string)
            elif choice == 'inline-code':
                string[len(string)-1] = inline(string[len(string)-1])
                lis_print(string)
            elif choice == 'header':
                string[len(string)-1] = header(string[len(string)-1])
                string.append("")
                lis_print(string)
            elif choice == 'link':
                string[len(string)-1] = link(string[len(string)-1])
                lis_print(string)
            elif choice == 'ordered-list':
                string = ordered_list(string)
                lis_print(string)
            elif choice == 'unordered-list':
                string = unordered_list(string)
                lis_print(string)

        elif choice == '!help':
            print("Available formatters:", end=" ")
            for i in Avl_formatter:
                print(i, end=" ")
            print("\nSpecial commands:", end=" ")
            for i in spec_formatter:
                print(i, end=" ")
            print()

        elif choice == '!done':
            return string

        else:
            print("Unknown formatting type or command")





def plain(string):
    text = input('Text: ')
    return string + text


def new_line(string):
    return string + '\n'


def bold(string):
    text = input('Text: ')
    return string + "**" + text + "**"


def italic(string):
    text = input('Text: ')
    return string + "*" + text + "*"


def inline(string):
    text = input('Text: ')
    return string + "`" + text + "`"


def link(string):
    label = input("Label: ")
    url = input("URL:")
    return string + f"[{label}]({url})"


def header(string):

    level = int(input("Level: "))
    while True:
        if 1 <= level <= 6:
            text = input('Text: ')
            return string + ("#" * level) + " " + text

        else:
            print("The level should be within the range of 1 to 6")
            level = int(input("Level: "))


def lis_print(lst):
    for j in lst:
        print(j)


def ordered_list(string):
    if string[len(string)-1] == '':
        string.pop()
    new_list = []
    rows = int(input('Number of rows: '))
    while True:
        if rows > 0:
            y = ""
            for i in range(rows):
                x = input(f'Row #{i+1}: ')
                y += f"{i+1}. " + x + '\n'
            new_list += [y]
            return string + new_list
        else:
            print("The number of rows should be greater than zero")
            rows = int(input('Number of rows: '))


def unordered_list(string):
    if string[len(string)-1] == '':
        string.pop()
    new_list = []
    rows = int(input('Number of rows: '))
    while True:
        if rows > 0:
            y = ""
            for i in range(rows):
                x = input(f'Row #{i + 1}: ')
                y += "* " + x + '\n'
            new_list += [y]
            return string + new_list
        else:
            print("The number of rows should be greater than zero")
            rows = int(input('Number of rows: '))


new_file = formatter()

file = open("output.md", "w", encoding="utf-8")
for line in new_file:
    file.write(line + "\n")
file.close()
