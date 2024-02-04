# RBC Import Configuration for Firefly III Data Importer

This JSON configuration file is designed for use with the Firefly III data import tool, allowing for the automatic importation of financial transactions from the Royal Bank of Canada (RBC) account statements into Firefly III.

## Configuration File Structure

- **Version and Source:** This file is based on version 3 of the configuration file format and is designed to work with version `ff3-importer-1.4.1` of the Firefly III data importer.
- **Date Format:** The date of transactions is expected in the `n/j/Y` format (month/day/year).
- **Delimiter:** The columns in the CSV file are separated by commas.
- **Headers and Rules:** The import file contains headers, and import rules are enabled.

## CSV File Format

Your CSV file from RBC must contain the following columns:

1. _Type de compte (ce champ est ignoré dans cette configuration)_
2. Numéro du compte
3. Date de l'opération
4. Numéro du chèque
5. Description 1
6. Description 2
7. CAD (montant de la transaction en dollars canadiens)
8. _USD (ce champ est ignoré dans cette configuration)_

## Duplicate Detection

The `classic` duplicate detection method is used to avoid importing duplicate transactions.

## Currency Conversion

Currency conversion is enabled, allowing for the automatic conversion of transaction amounts to the primary currency of your Firefly III account if necessary.
