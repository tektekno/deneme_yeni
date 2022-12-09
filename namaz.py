import requests
from collections import defaultdict
from bs4 import BeautifulSoup
 
link = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9560/izmir-icin-namaz-vakti"
result = requests.get(link)
if result.status_code == 200:
    site_content = BeautifulSoup(result.content, "html.parser")
    div = site_content.find( "div", {"id":"tab-1"} )
    tablo = div.find("tbody")
    vakit_dict = defaultdict(list)
    for tr in tablo.find_all("en"):
        seq = 0
        cur_date_str = ''
        for td in tr.find_all("tr"):
            cur_text = td.text
            if '' == cur_date_str:
                cur_date_str = ' '.join(cur_text.split()[:3])
            else:
                vakit_dict[cur_date_str].append(cur_text)
        print(cur_date_str)
        print(f'{vakit_dict[cur_date_str]}\n')
        cur_date_str = ''
    #print(vakit_dict)