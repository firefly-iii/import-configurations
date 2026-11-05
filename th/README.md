# Thailand

These four configurations consume normalized CSV produced by the separately
hosted [Thai bank companion tools](https://github.com/Nolang9100/firefly-thailand-imports/tree/540e9c91917ca1049dca2f2cbb170763130e7c7e).
They are not direct PDF parsers, native-bank CSV mappings, or online connections.

| Bank | Configuration | Format and usage |
| --- | --- | --- |
| Bangkok Bank | [default.json](bangkok-bank/default.json) | [README](bangkok-bank/README.md) |
| Kasikornbank (KBank) | [default.json](kbank/default.json) | [README](kbank/README.md) |
| Siam Commercial Bank (SCB) | [default.json](scb/default.json) | [README](scb/README.md) |
| LH Bank | [default.json](lh-bank/default.json) | [README](lh-bank/README.md) |

All configurations use THB, `YYYY-MM-DD`, `default_account: 0`, and empty private
mappings. Each bank guide explains preprocessing, duplicate limitations, and the
remaining actual-import validation gap. LH Bank review candidates are explicitly
excluded from standard output.
