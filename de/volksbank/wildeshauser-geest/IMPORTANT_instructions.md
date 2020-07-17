## Instructions for importing Volksbank Wildeshauser Geest eG CSV

The CSV files provided by Volksbank Wildeshauser Geest eG are pretty dirty. 
They contain lots of header information and some footers as well, and they're delivered in ANSI format.
They also use a non-common credit / debit indicator (s/h, Soll / Haben, debit / credit) while providing all transaction amounts in positive values.

The following steps are necessary:

### Create a rule to convert a transaction to a withdrawal
1. Create a new Rule
2. Set it active and to strict mode
3. Add a new Trigger - "Notes are..": S
4. Add a new Action - "Convert the transaction to a withdrawal"

By specifyign the credit / debit indicator as a Note in the import configuration, 
Firefly will now pick up all transactions containing an S in the Note field as a withdrawal.

### Sanitize the CSV file before import
1. Download a fresh CSV from your account details
2. Convert the file to UTF-8 encoding using a tool like Notepad++, Visual Studio Code, Vi etc.
3. Remove lines 1-12 since they contain header information that is not supposed to be imported.
4. Remove transactions that were already imported into Firefly. Deduplication doesn't seem to always work.
5. Remove the last three lines since they contain footer information that will result in faulty transactions messing up your balance.

After completing these steps, you can then use the csv-importer, provide your csv and my import.json and import your transactions.
