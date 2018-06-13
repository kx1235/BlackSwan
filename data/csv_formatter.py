import csv

date = ''
account = ''
action = ''
company = ''
info = ''
is_total = True


def text_between_brackets(text: str) -> str:
    return text[text.find('(') + 1:text.find(')')]


with open("all_accounts.txt", 'r') as input:
    with open("all_accounts.csv", 'w') as output:
        # Set up writer
        writer = csv.writer(output)

        # Print header
        header = ['Date', 'Account', 'Action', 'Company', 'Amount', 'Info']
        writer.writerow(header)

        # Parsing the text file
        for line in input:
            if line[0] == '-':
                date = line[2:]
            elif line.startswith('Asset') or line.startswith('Funds'):
                account = text_between_brackets(line)
                is_total = True
            elif line.startswith('Sold') or line.startswith('Bought'):
                words = line.split()
                action = words[0]
                company = words[1]
                info = text_between_brackets(line)
                is_total = False
            elif line.startswith('$'):
                if not is_total:
                    row = [date, account, action, company, line, info]
                    writer.writerow(row)
            else:
                print(line)
