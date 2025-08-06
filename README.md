# Extract Entities (URLs, Mentions, Hashtags)

## Description

The method extracts useful entities from social media posts such as URLs, hashtags, cashtags ($ and €), mentions (including Mastodon mentions), quoted texts, punctuations, punctuation emphasis (e.g., !!!), all caps words, negations, time expressions (e.g., today, next week), and emojis. It's a very simple method using only regular expressions to determine the mentioned entities. The method reads data from a CSV file with posts per row and writes output to a CSV file having post text and the extracted entities as respective columns.

## Use Cases

This method can be used to extract entities mentioned in social media posts, e.g., URLs, hashtags, emojis, etc., contributing to the analysis of social behavior among user groups.

## Input Data

The input data consists of social media posts (one per line) as a CSV file, i.e., `data/input_social_posts.csv`. The following are a few examples:

|Posts|
|---------|
|"@bob@infosec.exchange #Crypto €BMW ""Let’s go!"" https://t.co/xyz123 😀"|
|#Startups 💡 $GOOG https://t.co/xyz123 @dave@mastodon.social 'Not sure about this'|
|@bob@mastodon.social $AAPL 'This is amazing' 😀 #Crypto https://news.site/article|
|"@dave@infosec.exchange ""Exciting times ahead!"" https://t.co/xyz123 €BMW #AI 😀"|
|#AI @bob@mastodon.social €ETH 🚀 'Not sure about this' https://news.site/article|
|...|

## Output Data

The method writes output to a CSV file, i.e., `data/output_posts_with_entities.csv`. It has the first column as the original post's text, followed by columns representing entities extracted from the text. Each column value is a list of one or more entities extracted from a post.

| Posts | Mentions | Hashtags | Cashtags | URLs | Quoted_text | Punctuation_emphasis | All_caps | Negations | Time_expressions | Emojis |
| --------- | -------- | -------- | ---- | ----------- | ------------ | -------------------- | -------- | --------- | ---------------- | ------ |
|"@bob@infosec.exchange #Crypto €BMW ""Let’s go!"" https://t.co/xyz123 😀"|	['@bob@infosec.exchange']|	['#Crypto']	|['€BMW']	|['https://t.co/xyz123']	|"['""Let’s go!""']"|	[]	|['BMW']|	[]|	[]|	['😀']|
|"#Startups 💡 \$GOOG https://t.co/xyz123 @dave@mastodon.social 'Not sure about this'"|['@dave@mastodon.social']	|['#Startups']	|['\$GOOG']	|['https://t.co/xyz123']	|"[""'Not sure about this'""]"	|[]	|['GOOG']|	['not']	|[]	|['💡']|
|@bob@mastodon.social \$AAPL 'This is amazing' 😀 #Crypto https://news.site/article|	['@bob@mastodon.social']|	['#Crypto']|	['\$AAPL']|	['https://news.site/article']|	"[""'This is amazing'""]"|	[]|	['AAPL']|	[]|	[]|	['😀']|
|"@dave@infosec.exchange ""Exciting times ahead!"" https://t.co/xyz123 €BMW #AI 😀"	|['@dave@infosec.exchange']|	['#AI']|	['€BMW']|	['https://t.co/xyz123']|	"['""Exciting times ahead!""']"|	[]|	['BMW', 'AI']|	[]|	['times']|	['😀']|
|#AI @bob@mastodon.social €ETH 🚀 'Not sure about this' https://news.site/article |	['@bob@mastodon.social']|	['#AI']|	['€ETH']|	['https://news.site/article']|	"[""'Not sure about this'""]"|	[]|	['AI', 'ETH']|	['not']|	[]|	['🚀']|

## Hardware Requirements

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU cores, 4 GB RAM, 40 GB HDD).
  
## Environment Setup

Executing the `requirements.txt` file using the command `pip install -r requirements.txt` will deploy the working environment.

Please note that the requirements.txt contains fixed versions that require Python 3.10. If you want to use it with newer versions of Python, update the requirements.txt accordingly (or unpin the versions).

Alternatively, there's a Pipfile to install the method with [pipenv](https://pipenv.pypa.io/en/stable/)

## How to Use

Run code cells of the `index.ipynb` notebook 

*It imports functions from entity_extractor.py*

## Contact

For queries, please contact, <taimoor.khan@gesis.org>
