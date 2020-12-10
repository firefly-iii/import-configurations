# Erste Bank

There are a few things you have to be aware of while working with Erste Bank's George and Firefly III.

1. Make sure you configure the csv export like my example in the folder called `example.png`
2. Because George let's you download the csv just UTF-16LB encoded, you have to convert it to UTF-8 before importing in Firefly III.

## Converting via macOS / Linux
```
FILE=source.csv; iconv -f UTF-16LE -t utf-8 $FILE > import.csv
```