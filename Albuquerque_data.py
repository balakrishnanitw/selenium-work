# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome('C:/chromedriver.exe')
#driver.set_preference("browser.helperApps.neverAsk.saveToDisk","application/csv")
# Pass the URL of the file
nexturl = "http://cognospublic.cabq.gov/cabqcognos/cgi-bin/cognos.cgi?b_action=cognosViewer&ui.action=run&ui.object=/content/folder[%40name=%27Permitting%27]/folder[%40name=%27Building%20Permits%27]/report[%40name=%27KIVA_ALL_BLDG_permits%27]&ui.name=KIVA_ALL_BLDG_permits&run.outputFormat=&run.prompt=true&nh=1 "

# Derive the output files
filestr = "Albuquerque_data.txt"
#picklestr = "crime_data_pull.pkl"

# Identify the column names of the dataset, pipe delimited
row = 'Permit#|Bldg Use|Action|Land Use|Ownership|House#|Street|St|QD|Zip|Zone Map|Lot Acreage|Lot|Block|Tract|Subdivision|SqFt|Value|Owner|Contractor|Contractor Ph|Entry Date|Issue Date\n'
       
df = pd.DataFrame()

#try:
#   go to the initial page with data
driver.get(nexturl);

# Access the MainContent_rblArea_0 (City Wide Crome) controller in the HTML of the webpage
startdate = driver.find_element_by_id('PRMT_TB_N13AC6540x227FA718_NS_')
#startdate.click()


enddate = driver.find_element_by_id('PRMT_TB_N13AC6540x227FA8A4_NS_')
enddate.click()
finish = driver.find_element_by_id('finishN13AC6540x227FAA30_NS_')
finish.click() #sortResultBy = driver.find_element_by_id('option1')

html_source = driver.page_source
  
# Convert html source to BS analyzed object
soup = BeautifulSoup(html_source, 'html.parser')

# Get table on page by div class
table = soup.find('table', {'class': 'mainHeader1'})
#body = table.find_all('tbody')[-1]
#
## Get number of rows in the table on the page
rows = list()#body.find_all('tr')#list()

# Loop through each row in the table and collect the data into a dataframe and append to the final dataframe
for row in rows[1:]:
    col = row.find_all('td')
    dfrow = pd.DataFrame({'Permit#': [col[0].text.encode('utf-8', 'ignore')], 'Bldg Use': [col[1].text.encode('utf-8', 'ignore')],\
                          'Action': [col[2].text.encode('utf-8', 'ignore')], 'Land Use': [col[3].text.encode('utf-8', 'ignore')],\
                          'Ownership': [col[4].text.encode('utf-8', 'ignore')], 'House#': [col[5].text.encode('utf-8', 'ignore')],\
                          'Street': [col[6].text.encode('utf-8', 'ignore')],'St': [col[7].text.encode('utf-8', 'ignore')],\
                          'QD': [col[8].text.encode('utf-8', 'ignore')],'Zip': [col[9].text.encode('utf-8', 'ignore')],\
                          'Zone Map': [col[10].text.encode('utf-8', 'ignore')],'Lot Acreage': [col[11].text.encode('utf-8', 'ignore')],\
                          'Lot': [col[12].text.encode('utf-8', 'ignore')],'Block': [col[13].text.encode('utf-8', 'ignore')],\
                          'Tract': [col[14].text.encode('utf-8', 'ignore')],'Subdivision': [col[15].text.encode('utf-8', 'ignore')],\
                          'SqFt': [col[16].text.encode('utf-8', 'ignore')],'Value': [col[17].text.encode('utf-8', 'ignore')],\
                          'Owner': [col[18].text.encode('utf-8', 'ignore')],'Contractor': [col[19].text.encode('utf-8', 'ignore')],\
                          'Contractor Ph': [col[18].text.encode('utf-8', 'ignore')],'Entry Date': [col[19].text.encode('utf-8', 'ignore')],\
                          'Issue Date': [col[18].text.encode('utf-8', 'ignore')]})
    df = df.append(dfrow, ignore_index=True)
    #z=df.to_csv(filestr, index=False, sep = '|')


#for j in end_date:
#    for i in start_date:
start= driver.find_element_by_id('PRMT_TB_N13AC6540x227FA718_NS_')
start.send_keys("20101112")
start.send_keys(Keys.RETURN)
#start.click()
end = driver.find_element_by_id('PRMT_TB_N13AC6540x227FA8A4_NS_')
end.send_keys("20111112")
end.send_keys(Keys.RETURN)
#end.click()

    #        sortby = driver.find_element_by_id('option1')
    #        sortby.click()
finish = driver.find_element_by_id('finishN13AC6540x227FAA30_NS_')
#finish.click() 
    
html_source = driver.page_source
    
            # convert html source to BS analyzed object
soup = BeautifulSoup(html_source, 'html.parser')
    
            # get all reviews on page by div class
table = soup.find('table', {'class': 'mainHeader1'})
body = table.find_all('tbody')[-1]
        
            
            # Get number of rows in the table on the page
rows =  body.find_all('tr') #list()#

df.to_csv(filestr, index=False, sep = '|')
print "csv file downloaded"
driver.close()# -*- coding: utf-8 -*-
