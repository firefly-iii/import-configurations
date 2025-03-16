# Deutsche Bank
You'll need to edit the exported CSV before the import configuration will work.

### Preprocessing

#### Create a valid CSV out of the downloaded file

Remove everything above the table of transactions (except the headers) and the last line (the summary):
  - Automatically in Linux: run 
    - `sed -i '1,4d;$d' /path/to/your/Accounts.csv` or
    - `sed '1,4d;$d' /path/to/your/Accounts.csv > /path/to/your/Accounts_edit.csv` if you want to keep the original file
  - Manually removing the first 4 lines and the last line in a text editor

#### Fix `�` in the export (optional)

The csv file is encoded in ISO-8859-1, therefore all umlauts are represented by a placeholder. You can try to change the encoding in whatever text editor you use, or run the following command in Linux: `iconv -f ISO-8859-1 -t UTF-8 /path/to/your/Accounts_edit.csv > /path/to/your/Accounts_utf8.csv`

### Example header

`Buchungstag;Wert;Umsatzart;Begünstigter / Auftraggeber;Verwendungszweck;IBAN;BIC;Kundenreferenz;Mandatsreferenz;Gläubiger ID;Fremde Gebühren;Betrag;Abweichender Empfänger;Abweichender Auftraggeber;Anzahl der Aufträge;Anzahl der Schecks;Soll;Haben;Währung`
