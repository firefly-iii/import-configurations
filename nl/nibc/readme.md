# Usage Instructions

For each savings account CSV you have exported from the NIBC Bank:  

1. Ensure you have the relevant accounts created in Firefly III. This includes a revenue account for the NIBC Bank itself to represent interest payouts.
2. Strip the very first line from the CSV. This is a comment containing the account number, the actual data starts on the second line (header) and onward (transactions). E.g. `sed '1d' nibc-full.csv > nibc-transactions.csv`.
3. Select your transactions CSV file and the configuration JSON file.
4. **Make sure to set the "Default import account" to the NIBC (savings) account matching the selected CSV file!**
5. Map the data (see notes).


## Data Mapping Notes

TL/DR; the opposing account values have to be mapped to accounts other than the "Default import account".  
If you do not do so, the importer will reject these transactions; the source and destination of the transaction would be the same.  


### Opposing Account IBAN
Interest payouts are recorded with an opposing account IBAN that is equal to the IBAN of the savings account itself or with an empty/blank value.  
You should map both of these values to the revenue account that represents the NIBC Bank itself, *NOT* to the savings account matching the IBAN!  

### Opposing Account Name
Interest payouts will have a blank/empty value for this field.  
You should map this value to the revenue account that represents the NIBC Bank itself.  
