# ASN Bank

The CSV files downloaded from ASN Bank website do not contain Opposing Account
Name for contactless transactions so pratically all card transactions do not
have a destination account set when imported.

You can use the script
[here](https://gist.github.com/z3ntu/c3009c20013ce0f9a32a831d477048ac) to
preproccess the CSV so it has the data set correctly.
