# Deutsche Bank
You'll need to edit the exported CSV before the import configuration will work.

### Preprocessing

#### Create a valid CSV out of the downloaded file

Remove everything above the table of transactions (except the headers) and the last line (the summary):
  - Automatically in Linux: run 
    - `sed -i '1,7d;$d' /path/to/your/Accounts.csv` or
    - `sed '1,7d;$d' /path/to/your/Accounts.csv > /path/to/your/Accounts_edit.csv` if you want to keep the original file
  - Manually removing the first 4 lines and the last line in a text editor

### Example header

`Buchungstag;Wert;Umsatzart;Begünstigter / Auftraggeber;Verwendungszweck;IBAN / Kontonummer;BIC;Kundenreferenz;Mandatsreferenz;Gläubiger ID;Fremde Gebühren;Betrag;Abweichender Empfänger;Anzahl der Aufträge;Anzahl der Schecks;Soll;Haben;Währung`
