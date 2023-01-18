import pandas as pd

# Read the CSV file and specify the encoding as 'utf-8'
df = pd.read_csv("180536X_text_corpus.csv", encoding='utf-8')

# Convert the DataFrame to JSON and write to a file
df.to_json("sample.json", orient='records', force_ascii=False)

# Open the JSON file and read the data
with open("sample.json", "r", encoding='utf-8') as f:
    json_data = f.readlines()

# Write the modified JSON data to a file
with open("data_raw.json", "w", encoding='utf-8') as f:
    f.write("".join(json_data))

