for file in *.CSV; do
    cp $file conv_$file
    iconv -f LATIN1 -t UTF-8 conv_$file > $file
    rm conv_$file
    python3 cleaner.py $file
done
