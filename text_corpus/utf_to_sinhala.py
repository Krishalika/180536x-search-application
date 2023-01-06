import csv
import json
import codecs

# Read the JSON file
with open('songs.json', 'r') as f:
    data = json.load(f)

# Convert the elements of the array to Sinhala
sinhala_array = []
for element in data:
    print(element['songName'])
#     sinhala_element = codecs.decode(element, 'utf-8')
#     sinhala_array.append(sinhala_element)

# # Write the array to a CSV file
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for element in sinhala_array:
#         writer.writerow([element])
