# Extract Entities (URLs, Mentions, Hashtags)

## Description
The method extracts useful entities from social media posts such as URLs, hashtags, cashtags ($ and €), mentions (including Mustodon mentions), quoted texts, punctuations, punctuation emphasis (e.g., !!!), all caps words, negations, time expressions (e.g., today, next week), and emojis. It's a very simple method using only regular expressions to determine the mentioned entities. The method reads data from a CSV file with posts per row and writes output to a CSV file having post text and the extracted entities as respective columns.

## Use Cases
To extract entities mentioned in social media posts, e.g., URLs, hashtags, emojis, etc., contributing to analyzing social behavior among user groups

## Input data
The input data consists of consists of social media posts (one per line) as a CSV file, i.e., `data/input_social_posts.csv`. The following are a few examples; 

|post_text|
|---------|
|Check out my new blog post on #MachineLearning here: https://mlblog.example.com 🔥 @techguru|
|Had an amazing workout today! 💪 #FitnessGoals #StayHealthy @fitness_pro|
|Visit https://travel.example.com for the best vacation deals! 🏖️ #TravelMore @explore_worldwide|
|Can't stop laughing at this meme 😂 #Comedy #LOL https://funny.example.com @memelord|
|Cooking made easy with these recipes! 🍳 #HomeChef #YummyFood @recipe_magic https://cookwithus.example.com|
|Feeling inspired after today's meditation session 🧘‍♂️ #Mindfulness #Relaxation @wellnessguru|
|The new game update is out! 🎮 Check details here: https://gameupdate.example.com #GamingLife @gamezone|
|Happy weekend, everyone! 🎉 #GoodVibesOnly https://weekendfun.example.com @weekender_vibes|
|Protect the planet 🌍 #ClimateChange #GoGreen @environment_care https://saveearth.example.com|
|Just finished reading this amazing book 📚 #BookLovers #MustRead @bookclub https://readmore.example.com|


## Output Data
The method writes output back to a CSV file, i.e., `data/output_posts_with_entities.csv`. It has the first column as the original post's text, followed by columns representing entities extracted from the text. In case there are multiple entities mentioned, the entities are presented as a list.

```
,post_text,mentions,hashtags,cashtags,urls,quoted_text,punctuations,punctuation_emphasis,all_caps,negations,time_expressions,emojis
0,"@bob@infosec.exchange #Crypto €BMW ""Let’s go!"" https://t.co/xyz123 😀",['@bob@infosec.exchange'],['#Crypto'],['€BMW'],['https://t.co/xyz123'],"[('Let’s go!', '')]","['@', '@', '.', '#', '€', '""', '’', '!', '""', ':', '/', '/', '.', '/', '😀']",[],['BMW'],[],[],['😀']
1,#Startups 💡 $GOOG https://t.co/xyz123 @dave@mastodon.social 'Not sure about this',['@dave@mastodon.social'],['#Startups'],['$GOOG'],['https://t.co/xyz123'],"[('', 'Not sure about this')]","['#', '💡', '$', ':', '/', '/', '.', '/', '@', '@', '.', ""'"", ""'""]",[],['GOOG'],['not'],[],['💡']
2,@bob@mastodon.social $AAPL 'This is amazing' 😀 #Crypto https://news.site/article,['@bob@mastodon.social'],['#Crypto'],['$AAPL'],['https://news.site/article'],"[('', 'This is amazing')]","['@', '@', '.', '$', ""'"", ""'"", '😀', '#', ':', '/', '/', '.', '/']",[],['AAPL'],[],[],['😀']
3,"@dave@infosec.exchange ""Exciting times ahead!"" https://t.co/xyz123 €BMW #AI 😀",['@dave@infosec.exchange'],['#AI'],['€BMW'],['https://t.co/xyz123'],"[('Exciting times ahead!', '')]","['@', '@', '.', '""', '!', '""', ':', '/', '/', '.', '/', '€', '#', '😀']",[],"['BMW', 'AI']",[],['times'],['😀']
4,#AI @bob@mastodon.social €ETH 🚀 'Not sure about this' https://news.site/article,['@bob@mastodon.social'],['#AI'],['€ETH'],['https://news.site/article'],"[('', 'Not sure about this')]","['#', '@', '@', '.', '€', '🚀', ""'"", ""'"", ':', '/', '/', '.', '/']",[],"['AI', 'ETH']",['not'],[],['🚀']
5,'This is amazing' €BMW https://t.co/xyz123 💡 #AI @dave,['@dave'],['#AI'],['€BMW'],['https://t.co/xyz123'],"[('', 'This is amazing')]","[""'"", ""'"", '€', ':', '/', '/', '.', '/', '💡', '#', '@']",[],"['BMW', 'AI']",[],[],['💡']
6,'These days are amazing' #TechNews https://t.co/xyz123 €ETH 💡 @dave@techhub.org,['@dave@techhub.org'],['#TechNews'],['€ETH'],['https://t.co/xyz123'],"[('', 'These days are amazing')]","[""'"", ""'"", '#', ':', '/', '/', '.', '/', '€', '💡', '@', '@', '.']",[],['ETH'],[],['days'],['💡']
7,"What a day today #AI $GOOG @bob@techhub.org 🚀 https://news.site/article""",['@bob@techhub.org'],['#AI'],['$GOOG'],"['https://news.site/article""']",[],"['#', '$', '@', '@', '.', '🚀', ':', '/', '/', '.', '/', '""']",[],"['AI', 'GOOG']",[],"['day', 'today']",['🚀']
8,"https://news.site/article #TechNews ""Exciting times ahead!"" @eve@mastodon.social 😀 $GOOG",['@eve@mastodon.social'],['#TechNews'],['$GOOG'],['https://news.site/article'],"[('Exciting times ahead!', '')]","[':', '/', '/', '.', '/', '#', '""', '!', '""', '@', '@', '.', '😀', '$']",[],['GOOG'],[],['times'],['😀']
9,"Let’s go! https://t.co/xyz123 @alice@mastodon.social $TSLA #AI 🔥""",['@alice@mastodon.social'],['#AI'],['$TSLA'],['https://t.co/xyz123'],[],"['’', '!', ':', '/', '/', '.', '/', '@', '@', '.', '$', '#', '🔥', '""']",[],"['TSLA', 'AI']",[],[],['🔥']
10,"$TSLA 🔥 @bob@infosec.exchange ""Exciting times ahead!"" #AI https://t.co/xyz123",['@bob@infosec.exchange'],['#AI'],['$TSLA'],['https://t.co/xyz123'],"[('Exciting times ahead!', '')]","['$', '🔥', '@', '@', '.', '""', '!', '""', '#', ':', '/', '/', '.', '/']",[],"['TSLA', 'AI']",[],['times'],['🔥']
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


