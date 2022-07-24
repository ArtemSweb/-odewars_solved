import re


pattern = r'^(https?://)?(www\.)?([a-z-0-9]*)\..+$'

def domain_name(url):
    return re.match(pattern, url).groups()[2]

print(domain_name("http://google.com"))             # "google"
print(domain_name("http://google.co.jp"))           # "google"
print(domain_name("www.xakep.ru"))                  # "xakep"
print(domain_name("https://youtube.com"))           # "youtube"
print(domain_name("https://123.net"))               # "123"