from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


#binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
#browser = webdriver.Firefox(firefox_binary=binary)


driver = webdriver.Chrome('C:/chromedriver.exe')

#driver.get("https://www.python.org/")

# Pass the URL of the file
nexturl = "https://apps-secure.phoenix.gov/PDD/Search/IssuedPermit"

# Derive the output files
filestr = "Phoenix_data.txt"
#picklestr = "crime_data_pull.pkl"

# Identify the column names of the dataset, pipe delimited
row = 'Type|Number|Issue Date|	Final Date|Struct|Census|Use|Subdivision|Lot|Address|	Parcel|Floor Area|Total Fees|Zoning|Valuation|Owner|Owner Address|Contractor|Contr. Phone|Plan Number\n'
       
df = pd.DataFrame()

#try:
#   go to the initial page with data
driver.get(nexturl)

# Access the MainContent_rblArea_0 (City Wide Crome) controller in the HTML of the webpage
permitType = driver.find_element_by_id('ddlPermitType')
permitType.click()


structureClass = driver.find_element_by_id('ddlStructureClass')
structureClass.click()

sortResultBy = driver.find_element_by_id('option1')
sortResultBy.click()

html_source = driver.page_source
  
# Convert html source to BS analyzed object
soup = BeautifulSoup(html_source, 'html.parser')

# Get table on page by div class
table = soup.find('table', {'class': 'k-link'})
#body = table.find_all('tbody')[0]

# Get number of rows in the table on the page
rows = list()#body.find_all('tr')

# Loop through each row in the table and collect the data into a dataframe and append to the final dataframe
for row in rows[1:]:
    col = row.find_all('td')
    dfrow = pd.DataFrame({'Type': [col[0].text.encode('utf-8', 'ignore')], 'Number': [col[1].text.encode('utf-8', 'ignore')],\
                          'Issue Date': [col[2].text.encode('utf-8', 'ignore')], 'Final Date': [col[3].text.encode('utf-8', 'ignore')],\
                          'Struct': [col[4].text.encode('utf-8', 'ignore')], 'Census': [col[5].text.encode('utf-8', 'ignore')],\
                          'Use': [col[6].text.encode('utf-8', 'ignore')],'Subdivision': [col[7].text.encode('utf-8', 'ignore')],\
                          'Lot': [col[8].text.encode('utf-8', 'ignore')],'Address': [col[9].text.encode('utf-8', 'ignore')],\
                          'Parcel': [col[10].text.encode('utf-8', 'ignore')],'Floor Area': [col[11].text.encode('utf-8', 'ignore')],\
                          'Total Fees': [col[12].text.encode('utf-8', 'ignore')],'Zoning': [col[13].text.encode('utf-8', 'ignore')],\
                          'Valuation': [col[14].text.encode('utf-8', 'ignore')],'Owner': [col[15].text.encode('utf-8', 'ignore')],\
                          'Owner Address': [col[16].text.encode('utf-8', 'ignore')],'Contractor': [col[17].text.encode('utf-8', 'ignore')],\
                          'Contr. Phone': [col[18].text.encode('utf-8', 'ignore')],'Plan Number': [col[19].text.encode('utf-8', 'ignore')]})
    df = df.append(dfrow, ignore_index=True)

print "Current Page Completed"



start = driver.find_element_by_id('txtStartDate')
start.clear()
start.send_keys("11/17/2010")
start.send_keys(Keys.RETURN)
start.click()

end = driver.find_element_by_id('txtEndDate')
end.clear()
end.send_keys("12/16/2010")
end.send_keys(Keys.RETURN)
end.click()

sortby = driver.find_element_by_id('option1')
sortby.click()
CreateFile = driver.find_element_by_id('btnCreateFile')
CreateFile.click() 

html_source = driver.page_source

# convert html source to BS analyzed object 
soup = BeautifulSoup(html_source, 'html.parser')

# get all reviews on page by div class
table = soup.find('table', {'class': 'k-link'})
# body = table.find_all('tbody')[-1]


# Get number of rows in the table on the page
rows = list()# body.find_all('tr')



# Output final dataframe to current directory
df.to_csv(filestr, index=False, sep = '|')
