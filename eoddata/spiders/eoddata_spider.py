
import scrapy
import xml.etree.ElementTree as ET 

from eoddata.items import EoddataItem

class EoddataSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ["eoddata.com"]

    def __init__(self, exchange='NYSE', letter='A'):
        self.start_urls = [
        "http://eoddata.com/stocklist/%s/%s.htm"%(exchange, letter)
        ]

    def parse(self, response):
        colNames = ['Code', 'Name', 'High', 'Low', 'Close', 'Volume', 'ChangeAbs', 'dnImg', 'ChangePct', 'dlImg']
        colLen = len(colNames)
        rowDataRo = response.xpath('//tr[@class="ro"]/td').extract()
        rowDataRe = response.xpath('//tr[@class="re"]/td').extract()
        assert (len(rowDataRo) % colLen == 0)
        assert (len(rowDataRe) % colLen == 0)
        rowDataRo.extend(rowDataRe)
        for i in range(len(rowDataRo) / colLen):
            item = EoddataItem()
            item['Code'] = "".join(ET.fromstring(rowDataRo[i*colLen]).itertext())
            item['Name'] = "".join(ET.fromstring(rowDataRo[i*colLen+1]).itertext())
            item['High'] = float("".join(ET.fromstring(rowDataRo[i*colLen+2]).itertext()).replace(',',''))
            item['Low'] = float("".join(ET.fromstring(rowDataRo[i*colLen+3]).itertext()).replace(',',''))
            item['Close'] = float("".join(ET.fromstring(rowDataRo[i*colLen+4]).itertext()).replace(',',''))
            item['Volume'] = int("".join(ET.fromstring(rowDataRo[i*colLen+5]).itertext()).replace(',',''))
            item['ChangeAbs'] = float("".join(ET.fromstring(rowDataRo[i*colLen+6]).itertext()))
            item['ChangePct'] = float("".join(ET.fromstring(rowDataRo[i*colLen+8]).itertext()))
            yield item

            



