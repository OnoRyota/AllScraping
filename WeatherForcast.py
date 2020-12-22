import pandas #pandasをインポート
import pprint

import requests
from bs4 import BeautifulSoup

#国見
url_kunimi = 'https://tenki.jp/forecast/9/47/8320/44214/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_kunimi)

#jsonで保存
fetched_daraframes[0].to_json('KunimiForcast.json',force_ascii=True)

######################################################################################

#中津
url_nakatu = 'https://tenki.jp/forecast/9/47/8320/44214/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_nakatu)

#jsonで保存
fetched_daraframes[0].to_json('NakatuForcast.json',force_ascii=True)

######################################################################################

#豊後高田
url_bunngotakada = 'https://tenki.jp/forecast/9/47/8320/44209/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_bungotakada)

#jsonで保存
fetched_daraframes[0].to_json('BungotakadaForcast.json',force_ascii=True)

######################################################################################

#杵築
url_kituki = 'https://tenki.jp/forecast/9/47/8310/44210/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_kituki)

#jsonで保存
fetched_daraframes[0].to_json('KitukiForcast.json',force_ascii=True)

######################################################################################

#院内
url_innai = 'https://tenki.jp/forecast/9/47/8320/44211/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_innaii)

#jsonで保存
fetched_daraframes[0].to_json('InnaiForcast.json',force_ascii=True)

######################################################################################

#玖珠
url_kusu = 'https://tenki.jp/forecast/9/47/8330/44462/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_kusu)

#jsonで保存
fetched_daraframes[0].to_json('KusuForcast.json',force_ascii=True)

######################################################################################

#湯布院
url_yuhuin = 'https://tenki.jp/forecast/9/47/8310/44213/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_yuhuin)

#jsonで保存
fetched_daraframes[0].to_json('YuhuinForcast.json',force_ascii=True)

######################################################################################

#竹田
url_taketa = 'https://tenki.jp/forecast/9/47/8330/44208/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_taketa)

#jsonで保存
fetched_daraframes[0].to_json('TaketaForcast.json',force_ascii=True)

######################################################################################

#犬飼
url_inukai = 'https://tenki.jp/forecast/9/47/8340/44212/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_inukai)

#jsonで保存
fetched_daraframes[0].to_json('InukaiForcast.json',force_ascii=True)

######################################################################################

#宇目
url_ume = 'https://tenki.jp/forecast/9/47/8340/44205/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_ume)

#jsonで保存
fetched_daraframes[0].to_json('UmeForcast.json',force_ascii=True)

######################################################################################

#佐伯
url_saiki = 'https://tenki.jp/forecast/9/47/8340/44205/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_saiki)

#jsonで保存
fetched_daraframes[0].to_json('SaikiForcast.json',force_ascii=True)

######################################################################################

#蒲江
url_kamae = 'https://tenki.jp/forecast/9/47/8340/44205/'

#urlを読み取る
fetched_daraframes = pandas.io.html.read_html(url_kamae)

#jsonで保存
fetched_daraframes[0].to_json('kamaeForcast.json',force_ascii=True)