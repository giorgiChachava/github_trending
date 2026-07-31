import sys
import json
import time
import requests
from .visuals import typeout, typeout2, typeout3
from datetime import datetime

TODAY = datetime.today().strftime('%Y-%m-%d')

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
    typeout2("----- Now we can explore what's hot on GitHub without opening our browser. HOOORAYYY")


def main():
    args = sys.argv[1:]
    if len(args)==0:
        show_greetings()
    elif len(args)!=4:
        typeout("----- Nuhuh. To use me, run: github_trending --duration <day> --limit <n>")
    else:
        day = args[1]
        limit = args[3]
        
        
    
if __name__ == "__main__":
    main()