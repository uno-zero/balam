import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
print("")
banner = "\033[1;32m	  ▄▄▄▄    ▄▄▄       ██▓    ▄▄▄       ███▄ ▄███▓                   \033[0m\n" \
		 "\033[1;32m	▓█████▄ ▒████▄    ▓██▒   ▒████▄    ▓██▒▀█▀ ██▒                    \033[0m\n" \
		 "\033[1;32m	▒██▒ ▄██▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██    ▓██░                    \033[0m\n" \
		 "\033[1;32m	▒██░█▀  ░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██    ▒██                     \033[0m\n" \
		 "\033[1;32m	░▓█  ▀█▓ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒   ░██▒                    \033[0m\n" \
		 "\033[1;32m	░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ░  ░                    \033[0m\n" \
		 "\033[1;32m	▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░  ░      ░                    \033[0m\n" \
		 "\033[1;32m	 ░    ░   ░   ▒     ░ ░    ░   ▒   ░      ░                       \033[0m\n" \
		 "\033[1;32m	░            ░  ░    ░  ░     ░  ░       ░                        \033[0m\n" \
		 "\033[1;32m      ░                                                   By:unozero  \033[0m"
		 
print(banner)
query= input("º		Search balam: ")

def search(query):
  url = f"https://google.com/search?q={query}"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'html.parser')
  results = soup.find_all('div', class_='g')
  return results

dorks = [
  f"site:medium.com {query}",
  f"inurl:gitbook.io {query}",
  f"inurl:github.io {query}"
]

for dork in dorks:
  results = search(dork)
  print(f"Results for dork '{dork}':")
  for result in results:
    link = result.find('a')
    print(Fore.GREEN + link.get('href') + Style.RESET_ALL)
