import scrapy
from scrapy.http import FormRequest
import base64

'''После установки scrapy используем комнды в терминале 
scrapy startproject ppc100
scrapy genspider ppc100spider hackyou-captcha.ctf.su'''

class Ppc100spiderSpider(scrapy.Spider):#Это будет в файле после комнад
    name = 'ppc100spider'#Это будет в файле после комнад
    allowed_domains = ['hackyou-captcha.ctf.su'] #Это будет в файле после комнад
    start_urls = ['http://hackyou-captcha.ctf.su/']#Это будет в файле после комнад

    def parse(self, response):#Это будет в файле после комнад
        b64 = response.css('code::text').extract_first() #Достаем саму капчу
        data = base64.b64decode(b64)
        frmdata = {'answer': data} #Учитываем состав отправляемых данных
        yield FormRequest(response.url, callback=self.parse_frm, formdata=frmdata) #Отправляем нашу капчу

    def parse_frm(self, response):
        yield {
            'body': response.body #Достаем флаг
        }

'''
Чтоб запустить паука пишем команду в терминале 
и указываем сохранить ответ в json файле для большего удобства
scrapy runspider ppc100spider.py -o ppc100.json
'''

'''Kill_4ll_hum4ns_like_in_f1rst_hack_y0u_h2LExNo'''