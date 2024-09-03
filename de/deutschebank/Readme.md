# Deutsche Bank
You'll need to edit the exported CSV before the import configuration will work.

### Preprocessing

#### Create a valid CSV out of the downloaded file

Remove everything above the table of transactions (except the headers) and the last line (the summary):
  - Automatically in Linux: run `tail -n +5 /path/to/your/Accounts.csv > /path/to/your/Accounts_edit.csv`
  - Manually removing the first 4 lines

#### Replace `�` with matching umlauts (optional)

Although the csv file is formatted UTF-8, all umlauts are represented by a placeholder.

### Example header

`Buchungstag;Wert;Umsatzart;Begünstigter / Auftraggeber;Verwendungszweck;IBAN;BIC;Kundenreferenz;Mandatsreferenz;Gläubiger ID;Fremde Gebühren;Betrag;Abweichender Empfänger;Abweichender Auftraggeber;Anzahl der Aufträge;Anzahl der Schecks;Soll;Haben;Währung`
