import csv


def find_num_companies():
    companies = []
    counter = 0

    with open("all_accounts.csv", 'r') as input:
        reader = csv.reader(input)
        for row in reader:
            company = row[3]
            if company not in companies:
                companies.append(company)
                counter += 1

    print(companies)
    print(counter)


# find_num_companies()

def parse_int(string: str):
    string = string[1:]
    string = string.replace(',', '')
    return float(string)


def calculate_holdings():
    holdings = {'GOOG': 0.0,
                'VIG': 0.0,
                'XUS': 0.0,
                'ZEF': 0.0,
                'VAB': 0.0,
                'BAM.A': 0.0}

    with open("all_accounts.csv", 'r') as input:
        with open("portfolio_holdings.csv", 'w') as output:
            reader = csv.reader(input)
            writer = csv.writer(output)
            date = ''

            header = ['Date', 'GOOG', 'VIG', 'XUS', 'ZEF', 'VAB', 'BAM.A']
            writer.writerow(header)

            for row in reader:
                if row[0] == 'Date':
                    pass
                else:
                    action = row[2]
                    company = row[3]
                    amount = parse_int(row[4])

                    if date == '' or row[0] != date:
                        row = [row[09]]
                        sum = 0

                        for key in holdings:
                            sum += holdings.get(key)

                        for key in holdings:
                            if sum == 0:
                                row.append(0)
                            else:
                                row.append(holdings.get(key) / sum)

                        writer.writerow(row)
                        date = row[0]

                    if action == 'Bought':
                        holdings[company] += amount
                    elif action == 'Sold':
                        holdings[company] -= amount


calculate_holdings()
