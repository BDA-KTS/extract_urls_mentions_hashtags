# extract_urls_mentions_hashtags

The method extracts useful entities from social media posts such as URLs, hashtags, mentions and emojis. The method reads social media posts from the file, extract useful entities and stores the output as json file with lists of entitites extracted from each document.

## Keywords
url extraction, mentions extraction, hashtags extraction, emoji extraction

## Use case
Social scientists interested in analyzing the mention of entities e.g., URLs, hashtags etc. the compare the entity sharing behavior of two groups of social media posts

## Repo Structure
- `extract_entities.ipynb` contains the entity extraction script. It also reads and write data from/to the files
- `data/input-data.txt` has the input data, each document in a separate line
- `data/extracted_entities.json` has extracted entities structured for each document as list in a json file

## Environmental Setup
Executing the `requirements.txt` file using command `pip install -r requirements.txt` will deploy the working environment

## Input data
The method works on extracting entities from DBD data e.g., TweetsKB

## Sample input and output data
- The sample input data is in the file `data/input-data.txt`
- The sample output data is in the file `data/extracted_entities.json`

## Contact
taimoor.khan@gesis.org


