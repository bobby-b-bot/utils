""" Bobby B Bot common functions """

# Standard library imports
import re
import random
import json
import os
from os.path import join, dirname

# Third party imports
from dotenv import load_dotenv

def get_env(env_key, filepath):
    """ Get environment variables """
    
    # Create .env file path
    dotenv_path = join(dirname(filepath), '.env')
    # Load file from the path
    load_dotenv(dotenv_path)
    
    # Accessing variables
    try: 
        return os.getenv(env_key)
    except Exception as e:
        return e
    
def get_random_quote():
    """ Returns random quote from quotes file"""

    with open('../utils/quotes.json', 'r') as quotes:
        bobbyb_quotes = json.load(quotes)
    
    return random.choice(bobbyb_quotes)
    
def is_keyword_mentioned(text):
    """ Checks if the trigger words to call the bot are present in the string """
     
    with open('../utils/triggers.json', 'r') as triggers:
        keywords = json.load(triggers)

    for keyword in keywords:
    
        # Do a case insensitive search
        if re.search(keyword, text, re.IGNORECASE):
            return True
    
    return False

def get_username(author):
    """ Handles author names when comment was deleted before the bot could reply """

    if not author:
        name = '[deleted]'
    else:
    	name = author.name

    return name