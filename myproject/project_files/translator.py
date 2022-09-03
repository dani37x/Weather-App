from translate import Translator



def lang_changer(language, content):
    change = Translator(to_lang=language)
    translate_result = change.translate(content)
    return translate_result