# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

#import pickle

#binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#browser = webdriver.Firefox(firefox_binary=binary)


driver = webdriver.Chrome('C:/chromedriver.exe')

#driver.get("https://www.python.org/")

# Pass the URL of the file
nexturl = "http://www.stltoday.com/news/local/stl-info/search-city-of-st-louis-building-permits/html_8e7f4aa3-f366-5e66-aa8d-c96f51d917ce.html"

# Derive the output files
filestr = "stloius_data.txt"
#picklestr = "crime_data_pull.pkl"
# Identify the column names of the dataset, pipe delimited
row = 'Address|Project Type|Description|EstimatedCost|Owner|Date Issued\n'
       
df = pd.DataFrame()

#try:
#   go to the initial page with data
driver.get(nexturl);

# Access the MainContent_rblArea_0 (City Wide Crome) controller in the HTML of the webpage
permitType = driver.find_element_by_id('ddlPermitType')
permitType.click()


structureClass = driver.find_element_by_id('ddlStructureClass')
structureClass.click()
address = driver.find_element_by_name('Value1_1')
#address.click()

zipcode = driver.find_element_by_name('Value2_1')
zipcode.send_keys("63101")
zipcode.send_keys(Keys.RETURN)

ProjectType = driver.find_element_by_name('Value3_1')
#ProjectType.send_keys(Keys.RETURN)

EstimatedCost = driver.find_element_by_name('Value4_1')
EstimatedCost.send_keys(Keys.RETURN)

Search = driver.find_element_by_id('searchID')
Search.click() 

html_source = driver.page_source
  
# Convert html source to BS analyzed object
soup = BeautifulSoup(html_source, 'html.parser')

# Get table on page by div class
table = soup.find('table', {'class': 'cbFormTableCellspacing_4fda49b7143cf4'})
#body = table.find_all('tbody')[0]
df.to_csv(filestr, index=False, sep = '|')
# Get number of rows in the table on the page
rows = list()#body.find_all('tr')

# Loop through each row in the table and collect the data into a dataframe and append to the final dataframe
for row in rows[1:]:
    col = row.find_all('td')#Address|Project Type|Description|EstimatedCost|Owner|Date Issued\n
    dfrow = pd.DataFrame({'Address': [col[0].text.encode('utf-8', 'ignore')], 'Project Type': [col[1].text.encode('utf-8', 'ignore')],\
                          'Description': [col[2].text.encode('utf-8', 'ignore')], 'EstimatedCost': [col[3].text.encode('utf-8', 'ignore')],\
                          'Owner': [col[4].text.encode('utf-8', 'ignore')], 'Date Issued': [col[5].text.encode('utf-8', 'ignore')]})                          
                         
    df = df.append(dfrow, ignore_index=True)

print "Current Page Completed"

# Go through the rest of the pages available in the search options based on month and year












