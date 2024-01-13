# Translate-Mass-Amounts-of-Text
Uses unofficial google translate API for python to perform translate on a large quantity of text.

Maintains coherency of text by using common english sentence endings when dividing text into chunks to be translated, such as: '!', '.', '?', '\n'

Usage:

Converts an example textfile in english to chinese

```
python translate.py -f beemovie.txt -d zh-cn -o beemovieCN.txt 

```

Helpfile

```                                  
usage: mass text language translation [-h] [-v] [-f INPUTFILE] [-o OUTPUT] [-d LANGUAGEDEST] [-l]

A simple tool for mass converting text from google translate

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -f INPUTFILE, --inputfile INPUTFILE
                        Input file
  -o OUTPUT, --output OUTPUT
                        Output file
  -d LANGUAGEDEST, --languagedest LANGUAGEDEST
                        Language destination, use language code
  -l, --listlanguagecode
                        show list of available language codes

```

