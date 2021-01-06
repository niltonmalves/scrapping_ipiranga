# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import time

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.support.select import Select, By

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

#pedido de combustivel
dataEntrega='08/01/2021'
et=''
ga=''
gc='20000'
s10=''
s500=''

ano=time.localtime().tm_year
mes=time.localtime().tm_mon
dia=time.localtime().tm_mday

diaEnt=dataEntrega[0:2]
mesEnt=dataEntrega[3:5]
anoEnt=dataEntrega[6:10]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
chrome_options.add_argument('--ignore-certificate-errors')
#wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
wd = webdriver.Chrome('chromedriver')

wd.delete_all_cookies()

wd.get("https://www.redeipiranga.com.br/wps/portal/redeipiranga/login/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOKNAiwtDI1NDL0sgk1MDBzdw5zMg3y8DA1CTIAKIoEKDHAARwNC-sP1o_AqCTSHKsBjRUFuhEGmo6IiALSd4v0!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/")

#wd.set_window_size(1680,1680)
#wd.execute_script("document.body.style.zoom='50%'")
wd.fullscreen_window()

username=wd.find_element_by_id("viewns_Z7_2P981341J8S440AGVB7RLJ1034_:ns_Z7_2P981341J8S440AGVB7RLJ1034_j_id1359681328_510b177e:login")
username.clear()
username.send_keys('xxxxxx')
password = wd.find_element_by_name("viewns_Z7_2P981341J8S440AGVB7RLJ1034_:ns_Z7_2P981341J8S440AGVB7RLJ1034_j_id1359681328_510b177e:senha")
password.clear()
password.send_keys('xxxxxx')

#clicar no Enter, para confirmar o login e senha
wd.find_element_by_name("viewns_Z7_2P981341J8S440AGVB7RLJ1034_:ns_Z7_2P981341J8S440AGVB7RLJ1034_j_id1359681328_510b177e:ns_Z7_2P981341J8S440AGVB7RLJ1034_j_id1359681328_510b17ac").click()

wd.get('https://www.redeipiranga.com.br/wps/myportal/redeipiranga/meuposto/medidasespeciaisetransitorias')

#central de compras
wd.get('https://www.redeipiranga.com.br/wps/myportal/redeipiranga/compraseservicos/centraldecompras/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOItjDw8DSycDbwNPAzdDAJdQ518Hb0CvSzCDIEKIoEKjAIsLQyNTQy9LIJNTAwc3cOczIN8vAwNXE0o0x9oTpx-AxzA0YCQ_nD9KLASfD7AqwDkRLACPG4oyA0NjTDI9AQAgr9Ldw!!/dl5/d5/L2dJQSEvUUt3QS80SmlFL1o2XzJQOTgxMzQxSjhTNDQwQUdWQjdSTEoxMDM1/')

#clicar em combustivel
wd.get('https://www.redeipiranga.com.br/wps/myportal/redeipiranga/compraseservicos/centraldecompras/combustivel/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOKNAiwtDI1NDL0sgk1MDBzdw5zMg3y8DA28DIEKIvEocDUB67cw8vA0sHA28DbwMHQzCHQNdfJ19Ar0sggjpD_QHK_9xqZQ_QY4gKMBcfbjUUCU_XgUEAi_cP0ovEpAIYhXASiIwArwhQFeE8zM9AtyQ4EgwiDTM10RAOLIjlY!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/?uri=nm%3Aoid%3AZ6_2P981341J8S440AGVB7RLJ10J1')
wd.find_element_by_class_name('floatClose')
wd.find_element_by_class_name('floatClose').click()

wd.switch_to.frame(wd.find_element_by_name("ns_Z7_2P981341J0TD30A8I8QDFA2006_content-frame"))
#wd.find_element_by_class_name('floatClose').click()
#wd.switch_to.frame(wd.find_element_by_name("ns_Z7_2P981341J0TD30A8I8QDFA2006_content-frame"))

##<a class="floatClose" href="#">X</a>
#wd.refresh
#wd.page_source
#<input type="button" name="f1" id="f1" class="bt-busca ok" value="OK" onclick="enviarIntegracao();">
#ok=wd.find_element_by_name('f1')
#ok.click
#wd.find_element_by_class_name('bt-busca ok')
#wd.find_element_by_css_selector('.bt-busca ok')
#inserir Data de Entrega
diaEntrega= wd.find_element_by_xpath('//div[@class="centdig_selecao_consultasCompras centdig_bordar_bottom"]')
diaEntrega.find_elements_by_xpath('//br')[0].find_elements_by_xpath('//input[@name="dataEntrega"]')[0].send_keys(dataEntrega)
diaEntrega.find_elements_by_xpath('//br')[0].find_elements_by_xpath('//input[@name="dataEntrega"]')[0].send_keys(Keys.ENTER)#.send_keys(Keys.ENTER)
#wd.save_screenshot('testeInsercaodiaEntrega.png')


#Responsavel pela Entrega
#ipiranga
responsavelEntrega=wd.find_element_by_xpath('//div[@class="centdig_selecao_consultasCompras centdig_bordar_bottom"]')
responsavelEntrega.find_elements_by_xpath('//br')[0].find_elements_by_xpath('//label')[2].find_elements_by_xpath('//input[@name="responsavelEntrega"]')[1].click()  #0=> cliente 1=>ipiranga
#wd.save_screenshot('testeInsercaoRespEntrega.png')


#base supridora
#Base de Caxias
# 6515 => Base de Caxias
baseSupridora=wd.find_element_by_xpath('//div[@class="centdig_selecao_consultasCompras centdig_bordar_bottom"]')
baseSupridora.find_elements_by_xpath('//br')[0].find_elements_by_xpath('//label')[2].find_elements_by_xpath('//input[@name="nomeDependencia"]')[0].find_elements_by_xpath('//option[@value="6515"]')[0].click()  #0=> cliente 1=>ipiranga
#wd.save_screenshot('testeInsercaobaseSupridora.png')

tabela= wd.find_element_by_xpath('//div[@class="centdig_tabela_lista_produtos"]')
tabela.find_elements_by_xpath('//tr')[3].find_elements_by_xpath('//input[@name="quantidade"]')[3].send_keys(gc) #GC
#wd.save_screenshot('testeInsercaoGC.png')


tabela.find_elements_by_xpath('//tr')[3].find_elements_by_xpath('//input[@name="quantidade"]')[0].send_keys(et) #Et
#wd.save_screenshot('testeInsercaoET.png')


tabela.find_elements_by_xpath('//tr')[3].find_elements_by_xpath('//input[@name="quantidade"]')[2].send_keys(ga) #GA
#wd.save_screenshot('testeInsercaoGA.png')


tabela.find_elements_by_xpath('//tr')[3].find_elements_by_xpath('//input[@name="quantidade"]')[4].send_keys(s10) #S10
#wd.save_screenshot('testeInsercaoS10.png')


tabela.find_elements_by_xpath('//tr')[3].find_elements_by_xpath('//input[@name="quantidade"]')[5].send_keys(s500) #S500
#wd.save_screenshot('testeInsercaoS500.png')


prosseguir = tabela.find_elements_by_xpath('//tr')[3].find_element_by_xpath('//input[@alt="Prosseguir"]')#.click() #prosseguir

prosseguir.click()


wd.save_screenshot(f'{dia}{mes}{ano}testeInsercaoProsseguir{diaEnt}{mesEnt}{anoEnt}.png')

wd.find_element_by_xpath('//input[@alt="Finaliza pedido"]').click()
#wd.set_window_size(1200,1200)
#wd.set_window_size(540,540)
#wd.maximize_window()
#wd.current_window_handle.__dir__()
#wd.execute_script("document.body.style.zoom='50%'")
#wd.fullscreen_window()
#wd.set_window_position(1,1)

wd.save_screenshot(f'teste{dia}{mes}{ano}InsercaoFinalizaPedidodiaEnt{diaEnt}{mesEnt}{anoEnt}.png')
