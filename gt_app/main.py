import sys
import json
import time
import requests
from .visuals import typeout, typeout2, typeout3
from datetime import datetime, timedelta

TODAY_OBJ = datetime.today()
TODAY_STR = TODAY_OBJ.strftime('%Y-%m-%d')


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
    typeout2("----- To use me, run: github_trending --duration <day> --limit <n>" 'recommended: use <n>=10')
    typeout2("----- Now u will have information about GitHub repos that was created from <day> to today. List will be sorted by stars.")
    typeout2("----- Now we can explore what's hot on GitHub without opening our browser. HOOORAYYY")


def main():
    args = sys.argv[1:]
    if len(args)==0:
        show_greetings()
        print(int(TODAY[8:]))
    elif len(args)!=4 or args[0]!="--duration" or args[2]!="--limit":
        typeout("----- Nuhuh. To use me, run: github_trending --duration <day> --limit <n>")
    else:
        try:
            day = int(args[1])
        except ValueError:
            typeout("----- Nuhuh. To use me, run: github_trending --duration <day> --limit <n>")
            typeout("----- Hint: use integer for duration time")
            return
        try:
            limit = int(args[3])
        except ValueError:
            typeout("----- Nuhuh. To use me, run: github_trending --duration <day> --limit <n>")
            typeout("----- Hint: use integer for limit number")       
            return
        
        from_date_obj = TODAY_OBJ - timedelta(days=day)
        from_date = from_date_obj.strftime('%Y-%m-%d')
        print(from_date)
        
        
    
if __name__ == "__main__":
    main()