import csv
from selenium import webdriver

with open('results_by_letter.csv', 'w') as f:
    f.write('Course Letter , Courses , Link \n')

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://m.fiu.edu/catalog/index.php")

#Courses by letters

letter = []

for j in range(65 , 93):
    letter.append(chr(j))

for i in range(26):
    url = 'https://m.fiu.edu/catalog/index.php?action=subjectList&letter=' + letter[i]

    driver.get(url)

    #class_letter = driver.find_element_by_xpath('//div[@class="listButton listButton15"]')
    #classes_per_letter = driver.find_element_by_xpath('//span[@class="faded"]')

