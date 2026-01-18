# [Tomorrow](https://www.tomorrow.one)

| ff3-rule           | Tomorrow csv-identifier | for example                                                              |
| ------------------ | ----------------------- | ------------------------------------------------------------------------ |
| `account-name`     | `account_type`          | `Personal Account`, `Savings account` or `Pocket account`                |
| `date_book`        | `booking_date`          | `2026-01-18`                                                             |
| `date_transaction` | `valuta_date`           | (usually the same as the booking date)                                   |
| `opposing-name`    | `sender_or_recipient`   | `Tomorrow GmbH`                                                          |
| `opposing-iban`    | `iban`                  | `DE00000000000000000000`                                                 |
| `tags-comma`       | `booking_type`          | `Direct Debit`                                                           |
| `description`      | `description`           | `Thank you for a great month with Change from 18/01/2026 to 18/02/2026.` |
| `category-name`    | `category`              | `Finances`                                                               |
| `amount`           | `amount`                | `"-8,00"`                                                                |
| `currency-code`    | `currency`              | `EUR`                                                                    |

## pocket handling

When using a pocket, `tomorrow` handles the transfer between the "Personal Account" 
and a pocket as a "payment". Because of that two transactions are created. One payment 
to the pocket and one withdraw from the "Personal Account". Because a pocket doesn't 
has an IBAN, but a transaction seem to require one, an internal IBAN (E.g. `DEXXXXXXXXXXXXXXXX0310`)
is used for the withdraw transaction. Usually the payment to the pocket is correctly mapped as a 
transfer from the "Personal Account". But then the withdraw from the "Personal Account" is incorrectly 
mapped because of the invalid IBAN that is given in the csv data.

To avoid this, the IBAN needs to be mapped manually to the "Personal Account". This will result in error 
from the Import, but thats to be expected as the withdraw is a duplicate of the transfer.

Alternatively you could just remove the entries with the invalid IBAN before importing the csv.
