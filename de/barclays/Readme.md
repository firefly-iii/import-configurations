# Barclays Bank Germany
Barclays Bank Germany does not provide a CSV export option, but you can download the transactions in MS Excel format.

### Preprocessing

#### Create a valid CSV out of the downloaded Excel file

Open the Excel file in MS Excel or any alternative like Libre Office Calc and save it as a CSV file. Than remove the first 12 lines (everthing till the header of the table). You can do that:
  - Automatically in Linux: 
    - `tail -n +13 /path/to/your/Accounts.csv > /path/to/your/Accounts_edit.csv`or 
    - `sed -i '1,12d' /path/to/your/Accounts.csv` or 
    - `sed '1,12d' /path/to/your/Accounts.csv > /path/to/your/Accounts_edit.csv` if you want to keep the original file
  - Manually removing the first 12 lines in a text editor


### Example header

`Referenznummer;Buchungsdatum;Buchungsdatum;Betrag;Beschreibung;Typ;Status;Kartennummer;Originalbetrag;Mögliche Zahlpläne;Land;Name des Karteninhabers;Kartennetzwerk;Kontaktlose Bezahlung;Händlerdetails`
