#Translate a mass amount of text via google translate.
#Author Aaron Beckley
#Jan 12 2024
#Python 3.10.8
from googletrans import Translator #https://py-googletrans.readthedocs.io/en/latest/
import os
import argparse


def main():
    try:
        argParse = argparse.ArgumentParser(description='A simple tool for mass converting text from google translate', prog='mass text language translation')
        argParse.add_argument('-v', '--version', action='version', version='%(prog)s version 1.0')
        argParse.add_argument('-f', '--inputfile', action='store', type=str, help='Input file')
        argParse.add_argument('-o', '--output', action='store', type=str, help='Output file')
        #argParse.add_argument('-t', '--inputtext', action='store', type=str, help='Input text as a string')
        argParse.add_argument('-d', '--languagedest', action='store', type=str, help='Language destination, use language code')
        #argParse.add_argument('-s', '--languagesrc', action='store', type=str, help='Language Source, use language code')
        argParse.add_argument('-l', '--listlanguagecode', action='store', help=str(LANGUAGES))
        args = argParse.parse_args()
        if args.inputfile == None:
            print("Please provide an input text")
            exit()
        if args.inputfile:
            if args.output == None:
               translate_from_file(args.inputfile, args.languagedest)
            else:
               translate_from_file(args.inputfile, args.languagedest, args.output)
               


    
    except KeyboardInterrupt:
        print(' is caught, exiting...')
        exit()




def translate_from_file(input="", des='en', output="false",):
    translator = Translator()
    if output!="false":
        data = ""
        with open(str(input), 'r') as file:
            data = file.read()
        if (data.count('')-1) > 1000:
            count = 0
            start = 0
            end = 1000
            while count < (data.count('')-1): #uses common ways sentences are ended in english in order to try and maintain cohesion
                if data[end:end+1] == '.' or data[end:end+1] == '!' or data[end:end+1] == '?' or data[end:end+1] == '\n':
                    #print(data[start:end])
                    with open(output, "a") as text_file:
                        text_file.write(translator.translate(data[start:end], dest=des).text)
                    count = count + (data[start:end].count('')-1)
                    start = end
                    end = end + 1000
                else:
                    end+=1
                    if end > data.count('')-1:
                        with open(output, "a") as text_file: #When finished just does one last request then breaks
                            text_file.write(translator.translate(data[start:end], dest=des).text)
                        break
        else:
            with open(output, "a") as text_file:
                text_file.write(translator.translate(input, dest=des).text)    
    else:
        data = ""
        with open(str(input), 'r') as file:
            data = file.read()
        if (data.count('')-1) > 1000:
            count = 0
            start = 0
            end = 1000
            while count < (data.count('')-1): #uses common ways sentences are ended in english in order to try and maintain cohesion
                if data[end:end+1] == '.' or data[end:end+1] == '!' or data[end:end+1] == '?' or data[end:end+1] == '\n':
                    #print(data[start:end])
                    print(translator.translate(data[start:end], dest=des).text)
                    count = count + (data[start:end].count('')-1)
                    start = end
                    end = end + 1000
                else:
                    end+=1
                    if end > data.count('')-1: #When finished just does one last request then breaks
                        print(translator.translate(data[start:end], dest=des).text)
                        break
        else:
            print(translator.translate(input, dest=des).text)





#List of languages
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

if __name__ == "__main__":
    main()




