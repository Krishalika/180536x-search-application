import csv
import json
import codecs
from mtranslate import translate
# Read the JSON file
# with open('songs.json', 'r') as f:
#     data = json.load(f)

# # Convert the elements of the array to Sinhala
# sinhala_array = []
# for element in data:
#     print(element['songName'])
#     sinhala_element = codecs.decode(element, 'utf-8')
#     sinhala_array.append(sinhala_element)

# # Write the array to a CSV file
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for element in sinhala_array:
#         writer.writerow([element])

# def translation_array(stringArray):
#     translated_array = []
#     for string in stringArray:
#         translated_array.append(translate(string, 'si', 'en'))
#     return translated_array

import pandas as pd
import googletrans

# Read the Excel file
df = pd.read_excel('text_corpus.xls')

# Translate the Sinhala columns into English
translator = googletrans.Translator()
for column in df.columns:
    if df[column].dtype == object:  # Only translate columns with object dtype (i.e. strings)
        df[column] = df[column].apply(lambda x: translator.translate(x, src='si', dest='en').text)

# Write the translated dataframe to a new CSV file
df.to_csv('translated_filename.csv', index=False)


