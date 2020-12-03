from sys import argv, exit
from csv import reader, writer

NAME_COLLUMN_NUMBER = 11
IBAN_COLLUMN_NUMBER = 12
BIC_COLLUMN_NUMBER = 13
AMOUNT_COLLUMN_NUMBER = 14

FAULTY_BANK_BIC = '61150020'
CORRECT_BANK_BIC = 'ESSLDE66XXX'
# Maybe choose something else here
CORRECT_BANK_IBAN = 'DE00000000000061150020'
BANK_NAME = 'KSK ES'

if not argv[1]:
    print('Please pass a csv file')
    exit(1)
FILENAME = argv[1]

with open(FILENAME, 'r') as csv_file:
    CSV_READER = reader(csv_file, delimiter=';', quotechar='"')
    ROWS = [x for x in CSV_READER]
    for row in ROWS:
        if row[BIC_COLLUMN_NUMBER] == FAULTY_BANK_BIC:
            row[NAME_COLLUMN_NUMBER] = BANK_NAME
            row[IBAN_COLLUMN_NUMBER] = CORRECT_BANK_IBAN
            row[BIC_COLLUMN_NUMBER] = CORRECT_BANK_BIC

with open(FILENAME, 'w') as csv_file:
    CSV_WRITER = writer(csv_file, delimiter=';', quotechar='"')
    for index, row in enumerate(ROWS):
        if index == 0:
            CSV_WRITER.writerow(row)
            continue
        if float(row[AMOUNT_COLLUMN_NUMBER].replace(',', '.')) != 0:
            CSV_WRITER.writerow(row)
