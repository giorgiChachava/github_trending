import sys
import json
import time
import requests
from .visuals import typeout, typeout2, typeout3
from datetime import datetime, timedelta

TODAY_OBJ = datetime.today()
TODAY_STR = TODAY_OBJ.strftime('%Y-%m-%d')

MAX_DURATION_DAYS = 365  
MAX_LIMIT = 100          


def show_greetings():
    typeout2("---------------------------")
    typeout3(r"""
      /$$$$$$  /$$$$$$$$
     /$$__  $$|__  $$__/
    | $$  \__/   | $$   
    | $$ /$$$$   | $$   
    | $$|_  $$   | $$   
    | $$  \ $$   | $$   
    |  $$$$$$/   | $$   
    \______/    |__/     
          """)
    time.sleep(0.3)
    typeout2("----- Hello, I am here to help you discover trending repositories on GitHub")
    typeout2("----- You can call me GT.")
    typeout2("----- To use me, run: github_trending --duration <day> --limit <n>")
    typeout2("----- Now u will have information about GitHub repos that was created from <day> to today. List will be sorted by stars.")
    typeout2("----- OFC '--duration' and '--limit' are optional. if u dont use these commands, we make them 7 and 10 respectivly.")
    typeout2("----- Now we can explore what's hot on GitHub without opening our browser. HOOORAYYY")

def fetch_data(from_data, limit):
    query = f'created:{from_data}..{TODAY_STR}&sort=stars&order=desc'
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        counter=0
        for item in data['items']:
            if counter!=limit:
                counter+=1
                typeout3(f"----- repo N{counter} name: {item['name']}")
                typeout3(f"----- repo N{counter} stars: {item['stargazers_count']}")
                typeout3(f"----- repo N{counter} url: {item['html_url']}")
                typeout3("----------------------------------")
            else:
                return 
                
                
        print(data)
        print(from_data)
        return
    elif response.status_code == 403:
        typeout3("----- Rate limit exceeded! Wait a minute before running again.")
    elif response.status_code == 304:
        typeout3("----- Sorry, Error N304")
    elif response.status_code == 422:
        typeout3("----- Sorry, Error N422")
    elif response.status_code == 503:
        typeout3("----- Sorry, Error N503") 

def error_messege():
    typeout("----- Nuhuh. To use me, run: github_trending --duration <day> --limit <n>")
    typeout("----- OFC '--duration' and '--limit' are optional. if u dont use these commands, we make them 7 and 10 respectivly.")
    return
def main():
    args = sys.argv[1:]
    if len(args)==0:
        day=7
        limit=10
    elif len(args)==1 and args[0]=="greet":
        show_greetings()
        return 
    elif len(args)==1 and args[0]!="greet":
        error_messege()
        return
    elif len(args)==2:
        day = 7
        limit = 10
        if args[0]=="--duration":
            day = int(args[1])
        elif args[0]=="--limit":
            limit = int(args[1])
        else:
            error_messege()
            return
    elif len(args)==4:
        if args[0]=="--duration" and args[2]=="--limit":
            day = int(args[1]) 
            limit = int(args[3])
        elif args[2]=="--duration" and args[0]=="--limit":
            day = int(args[3]) 
            limit = int(args[1])
        else:
            error_messege()
            return
        
    if day <= 0:
        typeout("----- Error: --duration must be greater than 0.")
        return

    if day > MAX_DURATION_DAYS:
        typeout(f"----- Warning: Maximum supported duration is {MAX_DURATION_DAYS} days.")
        typeout(f"----- Capping duration to {MAX_DURATION_DAYS} days to ensure accurate results.")
        day = MAX_DURATION_DAYS

    if limit <= 0:
        typeout("----- Error: --limit must be greater than 0.")
        return

    if limit > MAX_LIMIT:
        typeout(f"----- Warning: Maximum allowed limit is {MAX_LIMIT}.")
        limit = MAX_LIMIT
        
    from_date_obj = TODAY_OBJ - timedelta(days=day)
    from_date = from_date_obj.strftime('%Y-%m-%d')
    fetch_data(from_date, limit)
        
if __name__ == "__main__":
    main()