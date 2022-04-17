This is a homework exercise where I was tasked to build a web scraper to fetch information from 3 Airbnb pages (links in the airbnb scraper file) (scraper works on Airbnb website on 17th of April 2022, might not work if Airbnb redesigns the website)
The project to run needs the following dependencies:
    * Python ( use pip install to get libraries selenium)
    * Google Chrome version 100 (to be compatible with the chromedriver.exe)
Asessment of the task:
    * Script is able to extract information for two pages, but the third page returns 403 error ( it could be due to the item being innaccessible or removed)
    * amenimities are only partially retrieved as a few are hidden behind a button. Potentially the web driver could press the button and retireve the rendered elements after that. (due to lack of time this isn't implemented)

Further possible improvements:
    * Looking into deprication warning message to ensure that running the scraper is safe (as it didn't effect functionality I decided not to look into them further to save time)
    * Input and output channels could be added to have a file of url's as input and a json file of data as output
    * To be scalable the scraper needs to use a proxy to hide the machine's IP from Airbnb, as scrapping numerous pages would blacklist the IP.
    * Scraper relies on reading data from very unique custom class elements that if changed could make retrieval of data fail (for example modifing the unique class codes for elements, when reworking page layout)
