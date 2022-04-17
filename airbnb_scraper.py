# Airbnb web-scrapper solution, made by Bence Mogyorodi
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AirbnbScraper:

    def __init__(self):
        # Needs a chromedriver.exe file in folder to work, make sure the version of the driver matches the installed chrome version on the device
        self.PATH = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH) # Will open up a chrome browser to convince Airbnb that a real user is accessing their website
        self.hotel_list = []
    
    def try_fetch_element(self,class_code):
        counter=0
        name_element=self.driver.find_elements(by=By.CLASS_NAME,value=class_code)
        if(len(name_element)>0):
            return name_element[0].text
        return "Element was not found!"
    def try_fetch_more_elements(self,class_code):
        name_element=self.driver.find_elements(by=By.CLASS_NAME,value=class_code)
        if(len(name_element)>0):
            return name_element
        return []
    def get_hotel_info(self, url):
        self.driver.get(url)
        self.driver.maximize_window() # making sure page rendered consistently by js scripts by making it full screen
        
        hotel_info={}
        
        
        time.sleep(5) # waiting for page to render

        hotel_info["url"]=url 
        hotel_info["name"]=self.try_fetch_element("_fecoyn4")
        property_type=self.try_fetch_element("_cv5qq4")
        if property_type!="Element was not found!":
            prop_type=property_type.split(' hosted')[0] # Property type is in longer text can be cut of by splitting before the word 'hosted'
            hotel_info["property_type"]=prop_type
        else:
            hotel_info["property_type"]=property_type

        hotel_info["bathroom_number"]="NA"
        hotel_info["bedroom_number"]="NA"
        hotel_data=self.try_fetch_more_elements("len26si")
        for data in hotel_data:
            # Multiple messages with variable split lenght, however the number of rooms is consistently split with one space from the room type
            # thus the number of rooms can be changed by looking at the last element in the text for the room type and the element before for the number
            data_split=data.text.split(' ')
            data_length=len(data_split)
            if data_split[data_length-1]=='bathrooms' or data_split[data_length-1]=='bathroom':
                hotel_info["bathroom_number"]=int(data_split[data_length-2])
            if data_split[data_length-1]=='bedrooms' or data_split[data_length-1]=='bedroom':
                hotel_info["bedroom_number"]=int(data_split[data_length-2])


        amenities=self.try_fetch_more_elements("iikjzje")
        #Some amenities are locked behind clicking a button on the UI which would open a list of amenities
        hotel_info["amenities"]=[]
        for element in amenities:
            hotel_info["amenities"].append(element.text)
        
        #add hotel info to hotel list
        self.hotel_list.append(hotel_info)
        print(hotel_info)

urls = ["https://www.airbnb.co.uk/rooms/33571268","https://www.airbnb.co.uk/rooms/33090114","https://www.airbnb.co.uk/rooms/50633275"]
AirbnbScraper = AirbnbScraper()
hotel_list=[]
for url in urls:
    AirbnbScraper.get_hotel_info(url)
print('\nFinal hotel list here:')
print(AirbnbScraper.hotel_list)
AirbnbScraper.driver.close()
