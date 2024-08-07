# Extra instructions for ING imports

Make sure you have asset accounts with the correct IBANs already present in Firefly III that correspond to the ING accounts you are going to import. This includes savings accounts.

## How to

For each personal ING account you import CSV files for:

- Create an asset account.
- Use a descriptive name.
- Fill in the ING IBAN: NL\*\*INGB\*\*\*\*\*\*

If you have transfers between your ING account and your savings account, be sure to create asset accounts as well:

- Create a new asset account for each saving account.
- Give it a descriptive name.
- Select role "Savings account" (not mandatory)
- Fill in the ING IBAN<sup>1</sup>: NL\*\*INGB\*\*\*\*\*\*  
  <sup>1</sup>: *A single IBAN can only be used on 1 asset account at a time. If the savings account is connected to your ING main account it shares the IBAN. Use the account number field instead of the IBAN field: W\*\*\*-\*\*\*\*\*.*

## I'm not going to do this!

Your import will probably fail. Sorry.
