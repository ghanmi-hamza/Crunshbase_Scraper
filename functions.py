from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import time
import re

class Profile(Thread):

    def __init__(self,name='',driver='',status = '',data = ''):
        Thread.__init__(self)
        self.name = name
        self.driver = driver
        self.status = status
        self.data = data
        pass

    def get_browser(self):
        options = webdriver.firefox.options.Options()
        #options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hamza\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe", options=options)
    def summary(self):
        self.driver.get('https://www.crunchbase.com/organization/'+str(self.name))
        try :
            elem0 = self.driver.find_element_by_xpath(".//*[@id= 'company_overview_about']")
        except :
            elem0 = self.driver.find_element_by_xpath(".//*[@id= 'investor_overview_about']")
        #elem0 = self.driver.find_element_by_xpath(".//span[contains(@id, 'overview_about')]")
        elm = elem0.find_element_by_xpath('..')
        description1 = elm.find_element_by_xpath(".//*[@class= 'description']").text   
        about_list = [e.text for e in elm.find_elements_by_xpath(".//ul[@class= 'icon_and_value']/li")]
        

        try :
            elem2 = self.driver.find_element_by_xpath(".//span[@id= 'overview_default_view']")
        except :   
            elem2 = self.driver.find_element_by_xpath(".//span[@id= 'overview_investor_view']")
        elm = elem2.find_element_by_xpath('..')
        try :
            description2 = elm.find_element_by_xpath(".//*[contains(@class, 'description')]").text
        except :
            description2 = ''
         
        Details = {}
        for e in  elm.find_elements_by_xpath(".//*[@class= 'text_and_value']/li"): 
            key = e.text.split(' \n')[0]
            key = key.lower()
            key= re.sub(' ', '_', key)
            Details[key] = ' '.join(e.text.split(' \n')[1:])
        dic = {
            'about_description' : description1 ,
            'detail_description' : description2,
            'description_list' : about_list
        }
        dic.update(Details)
        return(dic)

    def financial(self):
        #time.sleep(2)
        try:
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/company_financials")
            data  = {}
            for e in self.driver.find_elements_by_xpath(".//anchored-values/div"):
                key = e.text.split(' \n')[0]
                key = key.lower()
                key= re.sub(' ', '_', key)
                data[key] = e.text.split('\n')[1]
            
            #dic = {
            #    'funding_rounds_info' : data}
            li = []
            elm = self.driver.find_element_by_xpath(".//span[@id= 'funding_rounds']/..")
            elm1 = elm.find_elements_by_xpath(".//div/div[@class= 'section-content']/list-card/div/table[@class= 'card-grid']/tbody/tr")
            for e in elm1:
                li.append({"announced_date":e.find_elements_by_xpath(".//td")[0].text,
                        "transaction_name":e.find_elements_by_xpath(".//td")[1].text,
                        "transaction_link":e.find_elements_by_xpath(".//td")[1].find_element_by_xpath(".//*/*/a").get_attribute('href'),
                        "investors":e.find_elements_by_xpath(".//td")[2].text,
                        "money_raised":e.find_elements_by_xpath(".//td")[3].text,
                        "lead_investor":{"name":e.find_elements_by_xpath(".//td")[4].text,
                                            "link": e.find_elements_by_xpath(".//td")[4].find_element_by_xpath(".//*").get_attribute('href')} })
            data['rounds'] = li
        except:
            dic = {}
        dic = {
                'funding_rounds_info' : data}
        return(dic)
    def people(self):
        try:
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/people")
            elem1 = self.driver.find_element_by_xpath(".//*[@id= 'current_employees']")   
            elem2 = elem1.find_element_by_xpath('..')
            li = elem2.find_elements_by_xpath(".//ul[@class= 'two-column ng-star-inserted']/li")
            team = []
            for e in li:
                team.append({"image": e.find_element_by_xpath('.//img').get_attribute("src"),
                                "name": e.find_element_by_xpath('.//a').text,
                                "profile_link": e.find_element_by_xpath('.//a').get_attribute("href"),
                                "role": e.find_element_by_xpath('.//span').text } )
        except:
            team = ''
        dic = {'team' : team}
        return(dic)
    def technology(self):
        try:
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/technology")
            try: 
                elem1 = self.driver.find_element_by_xpath(".//*[@id= 'technology_about']")
                technology = elem1.find_element_by_xpath('..').text
            except :
                technology = ''
        except:
            technology = ''
        data  = {}
        for e in self.driver.find_elements_by_xpath(".//anchored-values/div"):
            key = e.text.split(' \n')[0]
            key = key.lower()
            key= re.sub(' ', '_', key)
            data[key] = e.text.split('\n')[1]
        dic = {
            'technology_info' : {'description':' '.join(technology.split()[1:])}
        }
        dic['technology_info'].update(data)
        return(dic)
    
    def news(self):
        self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/signals_and_news")
        time.sleep(2)
        try : 
            Activity = []
            #WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,".//timeline-card/div")))
            for e in self.driver.find_elements_by_xpath(".//timeline-card/div")[:10]:
                typ = e.find_element_by_xpath(".//div[@class= 'activity-title']/span").text
                dat = e.find_element_by_xpath(".//div[@class= 'activity-title']/field-formatter").text
                source = e.find_element_by_xpath(".//div[@class= 'activity-details']/*/div/*").text
                name = e.find_element_by_xpath(".//a").text
                link = e.find_element_by_xpath(".//a").get_attribute('href')
                if typ == 'News':
                    Activity.append({'type':typ,'date':dat,'source':source,'name':name,'link':link})
                else :
                    Activity.append({'type':typ,'date':dat,'content':source+name})
        except :
            Activity = ''

        try : 
            elem2 = self.driver.find_element_by_xpath(".//*[@id= 'events']/..")
            imgs = [e.get_attribute('src') for e in elem2.find_elements_by_xpath(".//img")]
            names = [{'name':e.text.split('\n')[0],'role':e.text.split('\n')[1],'date':e.text.split('\n')[2]} for e in elem2.find_elements_by_xpath(".//div[@class= 'fields']")]
            links = [e.get_attribute('href') for e in elem2.find_elements_by_xpath(".//div[@class= 'fields']/a")]
            for i in range(len(imgs)):
               names[i]['image'] =imgs[i]
               names[i]['link'] =links[i]

        except : 
            pass
        dic = {
            'activity' : Activity,
            'events' : names}
        return(dic)
    def run(self):
        self.data={}
        self.get_browser()
        self.status = 'succeeded'
        try:
            self.data.update(self.summary())
            self.data.update(self.technology())
            self.data.update(self.news())
            self.data.update(self.people())
            self.data.update(self.financial())
            self.data.update({"status":self.status})
            self.close_browser()
            print(self.name+' : '+self.status)
        except:
            self.close_browser()
            self.status = 'failed'
            self.data = {"status":self.status}
            print(self.name+' : '+self.status)
        return(self.data,self.status)
    def close_browser(self):
        self.driver.close()
        return()
