import pandas #pandasをインポート
import pprint

import requests
from bs4 import BeautifulSoup

#国見
url_kunimi = 'https://weather.yahoo.co.jp/weather/jp/44/8320/44214.html'

#urlを読み取る
kunimi = pandas.io.html.read_html(url_kunimi)

#jsonで保存
kunimi[0].to_json('KunimiForcast.json',force_ascii=False)

######################################################################################

#中津
url_nakatu = 'https://weather.yahoo.co.jp/weather/44/8320/44203.html'

#urlを読み取る
nakatu = pandas.io.html.read_html(url_nakatu)

#jsonで保存
nakatu[0].to_json('NakatuForcast.json',force_ascii=False)

######################################################################################

#豊後高田
url_bungotakada = 'https://weather.yahoo.co.jp/weather/44/8320/44209.html'

#urlを読み取る
bungotakada = pandas.io.html.read_html(url_bungotakada)

#jsonで保存
bungotakada[0].to_json('BungotakadaForcast.json',force_ascii=False)

######################################################################################

#杵築
url_kituki = 'https://weather.yahoo.co.jp/weather/44/8310/44210.html'

#urlを読み取る
kituki = pandas.io.html.read_html(url_kituki)

#jsonで保存
kituki[0].to_json('KitukiForcast.json',force_ascii=False)

######################################################################################

#院内
url_innai = 'https://weather.yahoo.co.jp/weather/44/8320/44211.html'

#urlを読み取る
innai = pandas.io.html.read_html(url_innai)

#jsonで保存
innai[0].to_json('InnaiForcast.json',force_ascii=False)

######################################################################################

#玖珠
url_kusu = 'https://weather.yahoo.co.jp/weather/44/8330/44462.html'

#urlを読み取る
kusu = pandas.io.html.read_html(url_kusu)

#jsonで保存
kusu[0].to_json('KusuForcast.json',force_ascii=False)

######################################################################################

#湯布院
url_yuhuin = 'https://weather.yahoo.co.jp/weather/44/8310/44213.html'

#urlを読み取る
yuhuin = pandas.io.html.read_html(url_yuhuin)

#jsonで保存
yuhuin[0].to_json('YuhuinForcast.json',force_ascii=False)

######################################################################################

#竹田
url_taketa = 'https://weather.yahoo.co.jp/weather/44/8330/44208.html'

#urlを読み取る
taketa = pandas.io.html.read_html(url_taketa)

#jsonで保存
taketa[0].to_json('TaketaForcast.json',force_ascii=False)

######################################################################################

#犬飼
url_inukai = 'https://weather.yahoo.co.jp/weather/44/8340/44212.html'

#urlを読み取る
inukai = pandas.io.html.read_html(url_inukai)

#jsonで保存
inukai[0].to_json('InukaiForcast.json',force_ascii=False)

######################################################################################

#宇目
url_ume = 'https://weather.yahoo.co.jp/weather/44/8340/44205.html'

#urlを読み取る
ume = pandas.io.html.read_html(url_ume)

#jsonで保存
ume[0].to_json('UmeForcast.json',force_ascii=False)

######################################################################################

#佐伯
url_saiki = 'https://weather.yahoo.co.jp/weather/44/8340/44205.html'

#urlを読み取る
saiki = pandas.io.html.read_html(url_saiki)

#jsonで保存
saiki[0].to_json('SaikiForcast.json',force_ascii=False)

######################################################################################

#蒲江
url_kamae = 'https://weather.yahoo.co.jp/weather/44/8340/44205.html'

#urlを読み取る
kamae = pandas.io.html.read_html(url_kamae)

#jsonで保存
kamae[0].to_json('kamaeForcast.json',force_ascii=False)
