THIS SCRIPT WAS ONLY TESTED WITH THE KREISSPARKASSE ESSLINGEN/NÜRTINGEN, USE AT
YOUR OWN RISK

Why?
---

KSK ES is doing some nasty stuff in their csv files.

How?
---

So pretty much everything you have to do is to go to your online banking
account and download the csv files. Put them in a folder next to the scripts.
Make sure they have a '.CSV' extension in allcaps or change the script.

Run `bash clean_csv_files.sh` and you should have clean csv files, ready for
being imported.

What is the script doing exactly?
---

Cmon, its not that much to read...

The script removes lines with an amount of 0 Euros. This is happening on
`ABSCHLUSS, Abrechnung DD.MM.YYYY siehe Anlage` lines.

It also corrects the BIC code, IBAN and Name of `ABSCHLUSS` and
`ENTGELTABSCHLUSS`.
