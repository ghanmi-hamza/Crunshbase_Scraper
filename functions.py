from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Profile:

    def __init__(self,name='',driver=''):
        self.name = name
        self.driver = driver
        pass

    def get_browser(self):
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hamza\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe", options=options)
        #self.driver.get('https://www.crunchbase.com/organization/'+str(self.name))
    def summary(self):
        self.driver.get('https://www.crunchbase.com/organization/'+str(self.name))
        elem0 = self.driver.find_element_by_xpath(".//*[@id= 'company_overview_about']")
        About = elem0.find_element_by_xpath('..').text

        try: 
            elem1 = self.driver.find_element_by_xpath(".//*[@id= 'company_overview_highlights']")
            Highlights = elem1.find_element_by_xpath('..').text
        except :
            Highlights = ''

        elem2 = self.driver.find_element_by_xpath(".//*[@id= 'overview_default_view']")
        Details = elem2.find_element_by_xpath('..').text
        dic = {
            'About' : ' '.join(About.split()[1:]),
            'Highlights' : ' '.join(Highlights.split()[1:]),
            'Details' : ' '.join(Details.split()[1:])
        }
        return(dic)

    def financial(self):
        try:
            self.driver.get('https://www.crunchbase.com/organization/'+str(self.name)+"/company_financials")
            try: 
                elem1 = self.driver.find_element_by_xpath(".//*[@id= 'company_financials_about']")
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
            try: 
                elem1 = self.driver.find_element_by_xpath(".//*[@id= 'current_employees']")
                team = elem1.find_element_by_xpath('..').text
            except :
                team = ''
        except:
            team = ''
        dic = {
            'Team' : ' '.join(team.split()[2:]),
        }
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
            elem0 = self.driver.find_element_by_xpath(".//*[@id= 'timeline']")
            Activity = elem0.find_element_by_xpath('..').text
        except :
            Activity = ''

        try : 
            elem2 = self.driver.find_element_by_xpath(".//*[@id= 'events']")
            Events = elem2.find_element_by_xpath('..').text
        except : 
            Events = ''
        dic = {
            'Activity' : ' '.join(Activity.split()[4:]),
            'Events' : ' '.join(Events.split()[1:])
        }
        return(dic)
    def close_browser(self):
        self.driver.close()
        return()
