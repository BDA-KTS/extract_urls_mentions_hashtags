import re
import emoji
import sys
import pandas as pd

def extract_entities(input_filepath, output_filepath):
    
    #read input data (social media posts)
    try:
        df_posts = pd.read_csv('data/input_social_posts.csv', encoding='utf-8')
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: File could not be parsed.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading: {e}")
        sys.exit(1)
    
    
    
    # Patterns to extract
    patterns = {
        "mentions": r'(?<!\w)@[\w.\-]+(?:@[\w\.\-]+\.\w+)?',                                           # including both normal and mastodon mentions
        "hashtags": r'#\w+',                                                                           # hashtags
        "cashtags":r'[\$\€][A-Za-z]{1,10}',                                                              # cash tags (only $ and €)
        "urls": r'https?://\S+|www\.\S+',                                                              # urls
        "quoted_text": r'"(.*?)"|\'(.*?)\'',                                                           # quotations  
        "punctuations": r'[^\w\s]',                                                                   # punctuations
        "punctuation_emphasis": r'!{2,}|\?{2,}|\.{2,}',                                                # emphasis on ? and ! punctuations
        "all_caps": r'\b[A-Z]{2,}\b',                                                                  # All caps words
        "negations": r'\b(not|no|never|none|n\'t)\b',                                                  # use of negations (no, not never, none)
        "time_expressions": r'\b(?:tomorrow|yesterday|today|times|tonight|now|week|days|day|days|month|year)',     # time expressions (day, days, tomorrow, yesterday, tonight, next week, now) 
        "emojis": r'[\U00010000-\U0010ffff]',                                                          # Basic Unicode emoji range
    }

    # extract entities from each post
    dict_entities = {'post_text':[], 'mentions':[], 'hashtags':[], 'cashtags':[], 'urls':[], 'quoted_text':[], 'punctuations':[], 
    'punctuation_emphasis':[], 'all_caps':[], 'negations': [], 'time_expressions':[], 'emojis':[]}
    dict_entities['post_text'] = df_posts['post_text']
    
    dict_entities['post_text'] = df_posts['post_text'].values

    time_pattern = r'\b(?:tomorrow|yesterday|tonight|now|next week|in \d+ days?)\b'
    
    for post in df_posts['post_text'].values:
        for name, pattern in patterns.items():
            if name in ['negations', 'time_expressions']:
                found = re.findall(pattern, post.lower())
            else:
                found = re.findall(pattern, post)
            dict_entities[name].append(found)
        
    df_output = pd.DataFrame(dict_entities)
    
    try:
        df_output.to_csv(output_filepath, index = True)
    except PermissionError:
        print("Error: Permission denied while writing the file.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while writing file: {e}")
        sys.exit(1)


