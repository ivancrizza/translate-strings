import os
import xml.etree.ElementTree as ET
from googletrans import Translator


def translate_text(text, target_language='fr'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


strings_file = './android/app/src/main/res/values/strings.xml'
output_dir = './android/app/src/main/res/values-fr'
output_file = os.path.join(output_dir, 'strings_fr.xml')


os.makedirs(output_dir, exist_ok=True)


tree = ET.parse(strings_file)
root = tree.getroot()


for string in root.findall('string'):
    original_text = string.text
    translated_text = translate_text(original_text, 'fr')
    string.text = translated_text


tree.write(output_file, encoding="utf-8", xml_declaration=True)

print(f"Arquivo traduzido salvo em {output_file}")
