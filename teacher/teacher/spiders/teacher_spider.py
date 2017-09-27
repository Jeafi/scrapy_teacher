#coding:utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector
import re
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class DmozSpider(Spider):
    name = "info"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
         # "http://202.119.85.163/open/TutorInfo.aspx?dsbh=13155",
     # "http://202.119.85.163/open/TutorInfo.aspx?dsbh=14093"
    ]
    with codecs.open('info.csv', "w", encoding='utf-8-sig')as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'E-mail', 'degree', 'title', 'birthday', 'research'])

    def start_requests(self):
        try:
            url_head = "http://202.119.85.163/open/TutorInfo.aspx?dsbh="
            for num in range(1, 100000):
                self.start_urls.append(url_head+str(num))

            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        except:
            print('?????')
                  # years_object.close()




    def parse(self, response):
        def pin(a):
            info = "\n".join(a.extract())
            res_th = r'>(.*?)<'
            m_th = re.findall(res_th, info, re.S | re.M)
            # info.decode('gb2312')
            # m_th[0].encode('utf-8')
            # print "**********\n" +m_th[0] + "\n**********\n"
            return m_th[0]
        def  pinr(a):
            info = "\n".join(a.extract())
            res_th = r'<td style="text-align: left;width: 300px;" class="tb_line">(.*?)<'
            m_th = re.findall(res_th, info, re.S | re.M)
            # info.decode('gb2312')
            # m_th[0].encode('utf-8')
            # print "**********\n"  + m_th[0] + "\n**********\n"
            return m_th[0]

        sel = Selector(response)
        names = sel.xpath("//tr[1]/td[contains(@class,'tb_line')][2]")
        mail =sel.xpath("//tr[7]/td[4]")
        degree = sel.xpath("//tr[4]/td[2]")
        title = sel.xpath("//tr[5]/td[2]")
        birthday = sel.xpath("//tr[2]/td[2]")
        research = sel.xpath("//tr[1]/td[contains(@class,'tb_line')][2]")
        pin(names)
        pin(mail)
        pin(degree)
        pin(title)
        pin(birthday)
        pinr(research)
        with open('info.csv', 'ab') as f:
            writer = csv.writer(f)
            writer.writerow([pin(names), pin(mail), pin(degree),pin(title),pin(birthday),pinr(research)])

