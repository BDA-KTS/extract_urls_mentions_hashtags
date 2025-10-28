# Extract Entities (URLs, Mentions, Hashtags)

## Description

The method extracts useful entities from social media posts such as URLs, hashtags, cashtags ($ and €), mentions (including Mastodon mentions), quoted texts, punctuations, punctuation emphasis (e.g., !!!), all caps words, negations, time expressions (e.g., today, next week), and emojis. It is a very simple method using only regular expressions to determine the mentioned entities. The method reads data from a CSV file with posts per row and writes output to a CSV file having the post text followed by the respective columns of the extracted entities.

## Use Cases

- The study the impact of users reaction and increase in their engagement with posts having URLs, hashtags, and mentioned compared to the posts without the mentioned entities on the same topic.
- Comparing the use of puntuation emphasis, all caps, and emojis between the social media posts on different topics indicate how formal or informal the general language is.
- Identifying collective activites and coordination patterns leading to real-time mobilization at the time of protests and political unrest.

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

| Posts | Mentions | Hashtags | Cashtags | URLs | Quoted_text | Punctuations | Punctuation_emphasis | All_caps | Negations | Time_expressions | Emojis |
|:-----:|:--------:|:--------:|:--------:|:----:|:-----------:|:------------:|:--------------------:|:--------:|:---------:|:----------------:|:------:|
|"@bob@infosec.exchange #Crypto €BMW ""Let’s go!"" https://t.co/xyz123 😀"|	['@bob@infosec.exchange']|	['#Crypto']	|['€BMW']	|['https://t.co/xyz123']	|"['""Let’s go!""']"|	[@, @, ., #, €, ", ’, !, ", :, /, /, ., /, 😀] | []	|['BMW']|	[]|	[]|	['😀']|
|"#Startups 💡 \$GOOG https://t.co/xyz123 @dave@mastodon.social 'Not sure about this'"|['@dave@mastodon.social']	|['#Startups']	|['\$GOOG']	|['https://t.co/xyz123']	|"[""'Not sure about this'""]"	| [#, 💡, \$, :, /, /, ., /, @, @, ., ', '] | []	|['GOOG']|	['not']	|[]	|['💡']|
|@bob@mastodon.social \$AAPL 'This is amazing' 😀 #Crypto https://news.site/article|	['@bob@mastodon.social']|	['#Crypto']|	['\$AAPL']|	['https://news.site/article']|	"[""'This is amazing'""]"| [@, @, ., $, ', ', 😀, #, :, /, /, ., /] |	[]|	['AAPL']|	[]|	[]|	['😀']|
|"@dave@infosec.exchange ""Exciting times ahead!"" https://t.co/xyz123 €BMW #AI 😀"	|['@dave@infosec.exchange']|	['#AI']|	['€BMW']|	['https://t.co/xyz123']|	"['""Exciting times ahead!""']"|	[@, @, ., ", !, ", :, /, /, ., /, €, #, 😀]	 | []|	['BMW', 'AI']|	[]|	['times']|	['😀']|
|#AI @bob@mastodon.social €ETH 🚀 'Not sure about this' https://news.site/article |	['@bob@mastodon.social']|	['#AI']|	['€ETH']|	['https://news.site/article']|	"[""'Not sure about this'""]"|	[#, @, @, ., €, 🚀, ', ', :, /, /, ., /]	| []|	['AI', 'ETH']|	['not']|	[]|	['🚀']|

## Hardware Requirements

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU cores, 4 GB RAM, 40 GB HDD).
  
## Environment Setup

The method is tested with Python 3.10 and should work with other Python versions as well. Use the following command to setup the virtual working environment by installing all dependencies;

  ```pip install -r requirements.txt```

## How to Use

- Open `index.ipynb` and execute the cells to use the method. It imports and uses the entity extraction function defined in `entity_extractor.py`.
- Populate the input file `data/input_social_posts.csv` with social media posts on the topic of interest, keeping one per row (Optional: the file already has sample posts). 

## Technical Details

Mentions are user-references in social posts (for example `@alice` on Twitter or `@alice@instance.social` on Mastodon). In this project mentions are detected by a single regular expression defined in `entity_extractor.py`: `(?<!\w)@[\w.\-]+(?:@[\w\.\-]+\.\w+)?`. This pattern matches an `at-sign(@)` not preceded by a word character, followed by a username (letters, digits, underscore, dot, hyphen) and optionally a second `@` plus an instance/domain to capture Fediverse/Mastodon handles. The negative lookbehind helps avoid matching mentions that are embedded inside other words, but edge cases (trailing punctuation, emails, or unusual unicode characters) may still require post-processing or normalization. See `entity_extractor.py` for the canonical regex and its usage.

This section briefly explains the implementation of `entity_extractor.py` and the `index.ipynb` workflow in clear, semi-formal points so you can understand, maintain, or extend the code.

entity_extractor.py

- Purpose: Implements a single public function `extract_entities(ls_posts)` that accepts a list of post strings and returns a pandas DataFrame where each column is an entity type and each row corresponds to a post.
- Patterns: A `patterns` dict defines named regular expressions for: Mentions (including Mastodon-style `@user@instance`), Hashtags (`#word`), Cashtags (`$` and `€` + ticker), URLs (`http(s)://...` and `www.`), Quoted text, Punctuations, Punctuation emphasis (repeated `!`, `?`, `.`), All-caps words, Negations (`not, no, never, none, n't`), Time expressions (today, tomorrow, times, etc.), and a basic Unicode emoji range.
- Extraction flow: Builds `dict_entities` with empty lists for each column, copies `ls_posts` to the `Posts` key, then iterates each post and each pattern. For `Negations` and `Time_expressions` the post is lowercased before regex matching to improve detection. Matches from `re.findall` are appended as lists so the resulting DataFrame column values are lists of matches.
- Output: Returns a pandas DataFrame. Typical usage writes this DataFrame to CSV (`to_csv`) which serializes lists to strings for storage.
- Dependencies & notes: Uses `re`, `pandas`, and imports `emoji` though emoji handling is currently implemented via a Unicode range and could be improved. Limitations include regex edge-cases, incomplete emoji coverage, and punctuation tokenization.

Suggestions: consider using the `emoji` library utilities, URL normalization, or an NLP library (spaCy) for more robust entity extraction and unit tests for edge cases.

Extending extraction: consider integrating `emoji` helpers, URL normalization, or an NLP library (spaCy) for more robust entity recognition.


## Contact

For queries, please contact, <taimoor.khan@gesis.org>
