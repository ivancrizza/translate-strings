import xml.etree.ElementTree as ET
from googletrans import Translator


def translate_text(text, target_language='fr'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


strings_file = 'app/src/main/res/values/strings.xml'
output_file = 'app/src/main/res/values-fr/strings_fr.xml'


tree = ET.parse(strings_file)
root = tree.getroot()


for string in root.findall('string'):
    original_text = string.text
    translated_text = translate_text(original_text, 'fr')
    string.text = translated_text


import os
os.makedirs(os.path.dirname(output_file), exist_ok=True)


tree.write(output_file, encoding="utf-8", xml_declaration=True)

print(f"Arquivo traduzido salvo em {output_file}")
