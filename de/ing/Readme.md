# ING
You'll need to edit the exported CSV before the import configuration will work.

1. Convert the file to UTF-8

2. Remove everything above the table of transactions (except the headers)

## Important
This only works, if you are not using tags in your bank account.

Each tag will create an extra column between "Buchungstext" and "Verwendungszweck" in your exported CSV. So you'll either need to clean this up manually or add one (or multiple, depending on the amount of additional columns) "_ignore" entries in the configuration file. Be aware that the number of "hashtag" columns can change from month to month and is determined by the transaction with the most tags.
