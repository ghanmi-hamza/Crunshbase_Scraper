from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread

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
            description2 = elm.find_element_by_xpath(".//*[@class= 'description']").text
        except :
            description2 = ''
         
        Details = {}
        for e in  elm.find_elements_by_xpath(".//*[@class= 'text_and_value']/li"): 
            Details[e.text.split(' \n')[0]] = ' '.join(e.text.split(' \n')[1:])
        dic = {
            'Description' : description1 + description2,
            'Description_list' : about_list
        }
        dic.update(Details)
        return(dic)

    def financial(self):
        try:
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/company_financials")
            try: 
                elem1 = self.driver.find_element_by_xpath(".//span[contains(@id, 'financials_about')]")
                Fundings = elem1.find_element_by_xpath('..').text
            except :
                Fundings = ''
        except:
            Fundings = ''
        dic = {
            'Fundings' : ' '.join(Fundings.split()[1:]),
        }
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
        dic = {'Team' : team}
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
        dic = {
            'Technology' : ' '.join(technology.split()[1:]),
        }
        return(dic)
    
    def news(self):
        self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/signals_and_news")

        try : 
            elem2 = self.driver.find_element_by_xpath(".//*[@id= 'events']")
            Events = elem2.find_element_by_xpath('..').text
        except : 
            Events = ''
        try : 
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/signals_and_news/timeline")
            elem0 = self.driver.find_element_by_xpath(".//*[@id= 'timeline']")
            a = elem0.find_element_by_xpath('..') 
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,".//*[@class= 'activity-row ng-star-inserted']")))
            xx =  a.find_elements_by_xpath(".//*[@class= 'activity-row ng-star-inserted']")
            Activity = [' '.join(e.text.split()) for e in xx]


        except :
            Activity = ''
        dic = {
            'Activity' : Activity,
            'Events' : ' '.join(Events.split()[1:])
        }
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
            self.close_browser()
            print(self.name+' : '+self.status)
        except:
            self.close_browser()
            self.status = 'failed'
            print(self.name+' : '+self.status)
        return(self.data,self.status)
    def close_browser(self):
        self.driver.close()
        return()
