The CSV needs to be stripped both before AND after the data. To do so:
- Delete everything before the header line
- Delete everything after the last transaction
- During import, you may encounter an error with the first line but it can be ignored. The first transaction in the csv is a 0 credit/debit line to tell you the previous balance. Unless you're automating the process of preparing the csv, its easier just to ignore the error.
