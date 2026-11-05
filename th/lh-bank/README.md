# LH Bank — Thailand

`default.json` imports the seven-column normalized CSV produced by the
[Thai bank companion tools](https://github.com/Nolang9100/firefly-thailand-imports/tree/540e9c91917ca1049dca2f2cbb170763130e7c7e/th/lh-bank).
It does **not** parse the original PDF or an arbitrary bank CSV directly.

Supported source: native THB account e-Statements; standard output requires externally attested controls.

## Prepare the CSV

Follow the [converter guide](https://github.com/Nolang9100/firefly-thailand-imports/blob/540e9c91917ca1049dca2f2cbb170763130e7c7e/th/lh-bank/README.md).
The converter and its requirements are hosted separately; no converter code,
credentials, or real bank records are included here.

For LH Bank, run `converter/statement_to_csv.py` from the companion bank directory.
Encrypted PDFs use a hidden password prompt with `--ask-password`.

**Use only standard `transactions.csv` output produced with a complete, matching
external control attestation bundle.** `review-candidates.csv` is review-only and
must not be treated as a completed source verification. LH Bank's supported
layout lacks printed independent opening and summary controls. Supporting values
are human-attested; the converter checks scope, provenance hashes, and values,
not the meaning or authenticity of supporting documents.

## Importer settings

Target: Firefly III Data Importer **2.3.5**, JSON configuration format **v3**.
Upload `transactions.csv` together with `default.json` using File import, then
select your own THB asset account. The default account is `0`, the mapping array
is empty, and automatic user-rule execution is disabled.

| CSV column | Role |
| --- | --- |
| `date` | Transaction date, `YYYY-MM-DD` |
| `description` | Description |
| `amount` | Negative withdrawal / positive deposit |
| `currency` | `THB` |
| `external_id` | Statement-text fingerprint plus row sequence |
| `balance` | Ignored; retained for inspection only |
| `note` | Note |

The configuration does not create an opening-balance transaction, category,
counterparty account, or internal-transfer interpretation.

Identical extracted statement text produces stable external IDs. Changed exports
or overlapping statement periods require a separate duplicate review; these are
not bank-issued transaction IDs.

## Validation and limits

The configuration passes the official v3 JSON Schema. Companion converter tests
use fictional fixtures; selected local real-source checks remain private.
Actual Firefly import/re-import acceptance has **not** been performed. See the
[validation record](https://github.com/Nolang9100/firefly-thailand-imports/blob/540e9c91917ca1049dca2f2cbb170763130e7c7e/VALIDATION.md)
for the supported scope and evidence limitations.
