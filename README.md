# Extract Entities (URLs, Mentions, Hashtags)

## Description

The method extracts useful entities from social media posts such as URLs, hashtags, cashtags ($ and €), mentions (including Mastodon mentions), quoted texts, punctuations, punctuation emphasis (e.g., !!!), all caps words, negations, time expressions (e.g., today, next week), and emojis. It's a very simple method using only regular expressions to determine the mentioned entities. The method reads data from a CSV file with posts per row and writes output to a CSV file having post text and the extracted entities as respective columns.

## Use Cases

- Social listening and brand monitoring: detect mentions and hashtags to track when a brand, product, or individual is discussed across platforms (Twitter, Mastodon, etc.).
- Trend detection: collect and aggregate hashtags, cashtags and URLs to identify emerging topics, viral posts, or breaking news quickly.
- Market and investor signals: extract cashtags (e.g., $AAPL, €ETH) together with sentiment cues (all-caps, emojis) to feed lightweight trading or research pipelines.
- Community network analysis: use mention pairs to build interaction graphs that reveal influencers, community structure, and reply networks.
- Misinformation / source tracing: extract URLs and quoted text to support fact-check workflows and provenance tracing of shared claims.
- Dataset preparation for ML: produce structured features (mentions, hashtags, emojis) to accelerate annotation, classification, and supervised model training.
- Archival and compliance: persist mentions, URLs and quoted content when collecting datasets for legal, compliance, or historical archiving purposes.
- Linguistic and cultural research: analyze emoji usage, punctuation emphasis and mention patterns to study communication norms across communities.

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

1. **Prepare the environment**
   
- Recommended Python: 3.10 (the pinned dependencies were tested with 3.10). Create and activate a virtual environment:
```    
  python3 -m venv .venv
  source .venv/bin/activate
```

- **Install dependencies:**

  ```pip install -r requirements.txt```

2. **Run the notebook (interactive)**

- Start Jupyter and open the notebook >  jupyter lab or jupyter notebook
- Open `index.ipynb` and run the cells in order. The notebook:
  - imports `extract_entities` from `entity_extractor.py`
  - reads `data/input_social_posts.csv`
  - runs the extractor and shows `df_extracted_entities.head()`
  - writes output to `data/output_posts_with_entities.csv` (UTF-8)


## How to Use

Follow these steps to run the extractor and produce the CSV output. Commands assumed to run in shell/terminal.

- Input format: ensure a `Posts` column exists in `data/input_social_posts.csv` and that text encoding is UTF-8 to preserve emojis.
- Large files: process in batches (e.g., read CSV in chunks) to avoid high memory usage.
- Debugging: inspect intermediate DataFrames with `.head()` and check regex edge cases by crafting unit tests.
- Extending extraction: consider integrating `emoji` helpers, URL normalization, or an NLP library (spaCy) for more robust entity recognition.

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

index.ipynb (cell-by-cell overview)

- Cell 1 (markdown): Notebook title.
- Cell 2 (markdown): Short method description.
- Cell 3 (python): Imports: `from entity_extractor import extract_entities` and `import pandas as pd`.
- Cell 4 (python): Read input CSV (`data/input_social_posts.csv`) into `df_posts`.
- Cell 5 (python): `df_posts.head()` to inspect the data.
- Cell 6 (python): Convert posts to list and call `extract_entities(ls_posts)` producing `df_extracted_entities`.
- Cell 7 (python): `df_extracted_entities.head()` to inspect output.
- Cell 8 (python): Save output to `data/output_posts_with_entities.csv` with `to_csv` (UTF-8 recommended).

Implementation tips

- Run cells in order, ensure Python 3.10 (or update pinned deps), and `pip install -r requirements.txt` (or use Pipfile/pipenv).

## Contact

For queries, please contact, <taimoor.khan@gesis.org>
