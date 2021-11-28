### Alpha Bank CSV import instructions

Alpha Bank provides 3 different types of CSV files depending on which interface you use.
All of them will need preprocessing before importing to Firefly III.

## Preprocessing

We need to remove the first six lines from any Alpha Bank CSV file before importing to Firefly. 
An easy way to do this is by running:

`tail -n +6 /path/to/your/Accounts.csv`

Or just open the file, delete the first six lines until the csv headers and save it back.

## Accounts
Delete the first 6 lines of the CSV file and then use the `default.json` configuration.

Also keep in mind, this type only includes a Description
for the transactions, and missing the categories provided by Alpha Bank. You can get
these by using the [Cards](#Cards) export.

## Cards
Delete the first 6 lines of the CSV file and then go with the `cards.json` configuration

## Ebanking transactions
Delete the first 3 lines of the CSV file and then go with the `report.json` configuration
