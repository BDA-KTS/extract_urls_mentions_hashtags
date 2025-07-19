# Extract Entities (URLs, Mentions, Hashtags)

## Description
The method extracts useful entities from social media posts such as URLs, hashtags, cashtags ($ and €), mentions (including Mastodon mentions), quoted texts, punctuations, punctuation emphasis (e.g., !!!), all caps words, negations, time expressions (e.g., today, next week), and emojis. It's a very simple method using only regular expressions to determine the mentioned entities. The method reads data from a CSV file with posts per row and writes output to a CSV file having post text and the extracted entities as respective columns.

## Use Cases
To extract entities mentioned in social media posts, e.g., URLs, hashtags, emojis, etc., contributing to analyzing social behavior among user groups

## Input data
The input data consists of consists of social media posts (one per line) as a CSV file, i.e., `data/input_social_posts.csv`. The following are a few examples; 

|post_text|
|---------|
|"@bob@infosec.exchange #Crypto €BMW ""Let’s go!"" https://t.co/xyz123 😀"|
|#Startups 💡 $GOOG https://t.co/xyz123 @dave@mastodon.social 'Not sure about this'|
|@bob@mastodon.social $AAPL 'This is amazing' 😀 #Crypto https://news.site/article|
|"@dave@infosec.exchange ""Exciting times ahead!"" https://t.co/xyz123 €BMW #AI 😀"|
|#AI @bob@mastodon.social €ETH 🚀 'Not sure about this' https://news.site/article|


## Output Data
The method writes output back to a CSV file, i.e., `data/output_posts_with_entities.csv`. It has the first column as the original post's text, followed by columns representing entities extracted from the text. Each column value is a list of one or more entities extracted from a post.

```
| # | post_text | mentions | hashtags | cashtags | URLs | quoted_text | punctuations | punctuation_emphasis | all_caps | negations | time_expressions | emojis |
| - | --------- | -------- | -------- | -------- | ---- | ----------- | ------------ | -------------------- | -------- | --------- | ---------------- | ------ |
|0|...|['@bob@infosec.exchange']|['#Crypto']|['€BMW']|['https://t.co/xyz123']|"[('Let’s go!', '')]"|"['@', '@', '.', '#', '€', '""', '’', '!', '""', ':', '/', '/', '.', '/', '😀']"|[]|['BMW']|[]|[]|['😀']|
|1|...|['@dave@mastodon.social']|['#Startups']|['$GOOG']|['https://t.co/xyz123']|"[('', 'Not sure about this')]"|"['#', '💡', '$', ':', '/', '/', '.', '/', '@', '@', '.', ""'"", ""'""]"|[]|['GOOG']|['not']|[]|['💡']|
|2|...|['@bob@mastodon.social']|['#Crypto']|['$AAPL']|['https://news.site/article']|"[('', 'This is amazing')]"|"['@', '@', '.', '$', ""'"", ""'"", '😀', '#', ':', '/', '/', '.', '/']"|[]|['AAPL']|[]|[]|['😀']|
|3|...|['@dave@infosec.exchange']|['#AI']|['€BMW']|['https://t.co/xyz123']|"[('Exciting times ahead!', '')]"|"['@', '@', '.', '""', '!', '""', ':', '/', '/', '.', '/', '€', '#', '😀']"|[]|"['BMW', 'AI']"|[]|['times']|['😀']|
|4|...|['@bob@mastodon.social']|['#AI']|['€ETH']|['https://news.site/article']|"[('', 'Not sure about this')]"|"['#', '@', '@', '.', '€', '🚀', ""'"", ""'"", ':', '/', '/', '.', '/']"|[]|"['AI', 'ETH']"|['not']|[]|['🚀']|
```
## Hardware Requirements
The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).  
  
## Environmental Setup
Executing the `requirements.txt` file using the command `pip install -r requirements.txt` will deploy the working environment

## How to Use

- Update the input file with social media posts, one per line (optional: already has sample posts)
- Execute the `main.py` file using the command `python main.py`
- *It imports functions from entity_extractor.py*

## Contact
[taimoor.khan@gesis.org](mailto:taimoor.khan@gesis.org)


