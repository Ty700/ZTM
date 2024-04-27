from translate import Translator
import sys

def main(lang_abv, lang):
    translator = Translator(to_lang=lang_abv, from_lang='en')
    
    translation = None

    __INFILE_NAME = 'file_to_translate.txt'
    __OUTFILE_NAME = 'translated_file.txt'

    try:
        with open(__INFILE_NAME) as infile:
            translation = translator.translate(infile.read())
            print(translation)

        with open(__OUTFILE_NAME, mode='w') as outfile:
            outfile.write(f'{__INFILE_NAME} in {lang}:\n')
            outfile.write(translation)

    except FileNotFoundError:
        print('Check your file path')
    

if __name__ == '__main__':
    lang_map = {
        'Arabic':       'ar',
        'Bengali':      'bi',
        'Chinese':      'zh',
        'English':      'en',
        'French':       'fr',
        'German':       'de',
        'Hindi':        'hi',
        'Japanese':     'ja',
        'Korean':       'ko',
        'Portuguese':   'pt',
        'Russian':      'ru',
    }
    
    # If lang to translate to isn't def in CLI
    if len(sys.argv) < 2:
        print("What language would you like to translate to: ")

        for lang in lang_map.keys():
            print(lang)
        print()

        trans_lang = input().capitalize()

        while(trans_lang not in lang_map.keys()):
            print("Non-supported language.")
            trans_lang = input().capitalize()
        
        else:
            main(lang_map[trans_lang], trans_lang)

    else:
        trans_lang = sys.argv[1].capitalize()

        while(trans_lang not in lang_map.keys()):
            print("Non-supported language.")
            trans_lang = input().capitalize()
        
        else:
            main(lang_map[trans_lang], trans_lang)
