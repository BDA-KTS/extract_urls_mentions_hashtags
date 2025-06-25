# Extract Entities (URLs, Mentions, Hashtags)

## Description
The method extracts useful entities from social media posts such as URLs, hashtags, mentions and emojis. The method reads social media posts from the file, extract useful entities and stores the output as json file with lists of entitites extracted from each document.

## Use Case
Social scientists interested in analyzing the mention of entities e.g., URLs, hashtags etc. the compare the entity sharing behavior of two groups of social media posts

## Input data
The method uses regular expressions to identify different entities in text and therefore can be used for any type of text. For demonstration, we use auto-generated social media posts.

|Social Media Posts|
|--------|
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
The entities extracted are writen into a file using JSON format.

```
{"docs": 10, "entities": [{"doc-0": {"urls": ["https://mlblog.example.com"], "mentions": ["@techguru"], "hashtags": ["#MachineLearning"], "emojis": ["\ud83d\udd25"]}}, {"doc-1": {"urls": [], "mentions": ["@fitness_pro"], "hashtags": ["#FitnessGoals", "#StayHealthy"], "emojis": ["\ud83d\udcaa"]}}, {"doc-2": {"urls": ["https://travel.example.com"], "mentions": ["@explore_worldwide"], "hashtags": ["#TravelMore"], "emojis": ["\ud83c\udfd6"]}}, {"doc-3": {"urls": ["https://funny.example.com"], "mentions": ["@memelord"], "hashtags": ["#Comedy", "#LOL"], "emojis": ["\ud83d\ude02"]}}, {"doc-4": {"urls": ["https://cookwithus.example.com\""], "mentions": ["@recipe_magic"], "hashtags": ["#HomeChef", "#YummyFood"], "emojis": ["\ud83c\udf73"]}}, {"doc-5": {"urls": [], "mentions": ["@wellnessguru"], "hashtags": ["#Mindfulness", "#Relaxation"], "emojis": ["\ud83e\uddd8\u200d\u2642\ufe0f"]}}, {"doc-6": {"urls": ["https://gameupdate.example.com"], "mentions": ["@gamezone"], "hashtags": ["#GamingLife"], "emojis": ["\ud83c\udfae"]}}, {"doc-7": {"urls": ["https://weekendfun.example.com"], "mentions": ["@weekender_vibes"], "hashtags": ["#GoodVibesOnly"], "emojis": ["\ud83c\udf89"]}}, {"doc-8": {"urls": ["https://saveearth.example.com\""], "mentions": ["@environment_care"], "hashtags": ["#ClimateChange", "#GoGreen"], "emojis": ["\ud83c\udf0d"]}}, {"doc-9": {"urls": ["https://readmore.example.com\""], "mentions": ["@bookclub"], "hashtags": ["#BookLovers", "#MustRead"], "emojis": ["\ud83d\udcda"]}}]}
```

## Hardware Requirements
The method runs on a cheap virtual machine provided by cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD). 
  
## Environmental Setup
Executing the `requirements.txt` file using command `pip install -r requirements.txt` will deploy the working environment

## How to Use
Open the notebook `extract_entities.ipynb` and call the method `extract_entities(text)` for each text item in a loop. The method itself is defined in the notebook as well.

## Contact
[taimoor.khan@gesis.org](mailto:taimoor.khan@gesis.org)


