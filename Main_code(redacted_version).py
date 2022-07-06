from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import re
import csv
# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# Makes a list "urls" that contains the column "Company department domain"
df = pd.read_csv('Missouri_Contacts.csv')
urls = df['Company department domain']
# Urls are changed for the code to only go through a website once and get all the info at once
urls[8] = ""
urls[1] = ""
urls [18] = ""
urls[28] = ""
urls[38] = ""
urls[43] = ""
alphabet = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
stupid_blank = '\xa0'
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#Lists to store information
names_positions = []
Phone = []
Email = []
domains = []
company = []
# For loop begins
for url in urls:
# First website
   if(url == urls [1]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       table = news_soup.find('table')
       table_text = table.get_text()
       lists = table_text.split("\n")
       clean_list = []
       for item in lists:
           if(item != ""):
               clean_list.append(item)
       i = 0
       while i < len(clean_list):
           names_positions.append(clean_list[i])
           i = i+1
           Phone.append(clean_list[i])
           i = i+1
           Email.append(clean_list[i])
           i = i+1
           stripped_names_positions = names_positions
           names = []
           positions = []
           domains.append(url)
           for name in stripped_names_positions:
               both = name.split(',')
               names.append(both[0])
               positions.append(both[1])
       for name in stripped_names_positions:
           if(re.search(" – ", name)):
               company_fullname = news_soup.title.get_text()
               company_name = company_fullname.split(' – ')
               company.append(company_name[1])
           else:
               company_fullname = news_soup.title.get_text()
               company.append(company_fullname)
# Next
   elif(url == urls[8]):
       browser.visit("")
       html = browser.html
       news_soup = soup(html, 'html.parser')
       all_links = []
       websites = []
       for link in news_soup.find_all('a'):
           all_links.append(link.get('href'))
       for link in all_links:
           if re.search("/government/departments/public-utilities/water/profiles", link):
               websites.append(link)
       websites.pop(0)
       for website in websites:
           browser.visit("" + website)
           html = browser.html
           news_soup = soup(html, 'html.parser')
           name = news_soup.h1.get_text()
           position = news_soup.p.get_text()
           email_code = news_soup.find("div", {"class":"col-md-6"})
           email_and_phone = email_code.get_text()
           names.append(name)
           positions.append(position)
           email_and_phone_split = email_and_phone.split('\n')
           j = email_and_phone_split.index("Email:")
           j2 = email_and_phone_split.index("Phone:")
           Email.append(email_and_phone_split[j + 1])
           Phone.append(email_and_phone_split[j2 + 1])
           domains.append("" + website)
           code = news_soup.find("a", {"class":"logo-top-line"})
           company_fullname = code.get_text()
           company_name = company_fullname.strip()
           company.append(company_name)
  
   # Next                 
   elif(url == urls[15]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       email_and_phone = news_soup.find("div", {"id":"contactspopularlistDiv"})
       email_phone = email_and_phone.get_text()
       info_list = email_phone.split()
       first_name = info_list[0]
       last_names = info_list[1].split('Title:')
       last_name = last_names[0]
       name = first_name + " " + last_name
       title_half = info_list[3].split('Phone:')
       title = info_list[2] + " " + title_half[0]
       phone_list = info_list[4].split('opens')
       phone = phone_list[0]
       email = info_list[7]
       names.append(name)
       positions.append(title.strip())
       Phone.append(phone.strip())
       Email.append(email.strip())
       domains.append(url)
       company_fullname = news_soup.title.get_text()
       company.append(company_fullname)
  
   # Next
   elif(url == urls[16]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       name_code = news_soup.find("div", {"style": "font-size: 14.4px;"})
       phone_code = news_soup.find("span", {"style":"font-size: 14.6667px; font-family: Ubuntu;"})
       springfield_name = name_code.get_text()
       info_split = springfield_name.split(',')
       name_split = info_split[0].split('Director')
       springfield_name = name_split[0].split('\xa0')
       names.append(springfield_name[1])
       positions.append("Director, Environmental Services")
       Phone.append(" ")
       Email.append(" ")
       domains.append(url)
       company_fullname = news_soup.title.get_text()
       company.append(company_fullname)
  
   # Next
   elif(url == urls[17]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('li', {'class': 'InfoAdvanced widgetItem fr-view'})
       name = code.h3.get_text()
       link = code.find('a')
       email_split = link.get('href')
       email_two, email_three, email = email_split.partition('mailto:')
       title_list = code.get_text()
       info_list = title_list.split()
       title = info_list[3] + " " + info_list[4]
       phone = info_list[15]
       names.append(name)
       positions.append(title.strip())
       Phone.append(phone.strip())
       Email.append(email.strip())
       domains.append(url)
       company_fullname = news_soup.title.get_text()
       company.append(company_fullname)
  
   # Next
   elif(url == urls[18]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('div', {'class': 'et_pb_column et_pb_column_3_8 et_pb_column_inner et_pb_column_inner_1'})
       diverted = news_soup.find('p', {'style': 'height: 150px;'})
       text = code.get_text()
       defined = text.split('<p style="height: 150px;">')
       for str in defined:
           dif = str.split('\n')
           text_list = []
           text_list.append(dif)
      
       second_code = news_soup.find('div', {'class': 'et_pb_column et_pb_column_3_8 et_pb_column_inner et_pb_column_inner_2 et-last-child'})
       second_diverted = news_soup.find('p', {'style': 'height: 150px;'})
       second_text = second_code.get_text()
       second_defined = second_text.split('<p style="height: 150px;">')
       for second_str in second_defined:
           second_dif = second_str.split('\n')
           second_text_list = []
           second_text_list.append(second_dif)
      
       main_list = text_list[0]
       second_main_list = second_text_list[0]
      
       one_clean_list = []
       two_clean_list = []
       for item in main_list:
               if(item != ""):
                   one_clean_list.append(item)
      
       for item in second_main_list:
               if(item != ""):
                   two_clean_list.append(item)
      
       for item in two_clean_list:
           one_clean_list.append(item)
       i = 0
       while i < len(one_clean_list):
           names.append(one_clean_list[i])
           i = i+1
           positions.append(one_clean_list[i])
           i = i+1
           Email.append(" ")
           Phone.append(" ")
           domains.append(url)
           one_clean_list_length = len(one_clean_list)
          
       for i in range(0, int(one_clean_list_length/2)):
           company_fullname = news_soup.title.get_text()
           company.append(company_fullname)
  
   # Next
   elif(url == urls[26]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       phone_number_code = news_soup.p.a.next_sibling.next_sibling
       phone = phone_number_code.get_text()
       email_code = news_soup.p.a.next_sibling.next_sibling.next_sibling.next_sibling
       email = email_code.get_text()
       names.append(" ")
       positions.append("Customer Service")
       Phone.append(phone)
       Email.append(email)
       domains.append(url)
       company_code = news_soup.find('span', {'class': 'sr-only'}).get_text()
       if(re.search('Home Page', company_code)):
           company_text = company_code.strip('Home Page')
       else:
           company_text = company_code
       company.append(company_text)
  
   # Next
   elif(url == urls[27]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       code = news_soup.find('div', {'id': 'dnn_ctr640_HtmlModule_lblContent', 'class': 'Normal'})
       phone_code = code.h2.next_sibling.next_sibling.next_sibling.next_sibling
       phone_text = phone_code.get_text()
       phone_list = phone_text.split(':')
       phone_raw = phone_list[1]
       phone = phone_raw.strip()
       position_text = news_soup.title.get_text()
       if(re.search('Contact ', position_text)):
           position = position_text.strip('\n\tContact ')
       else:
           position = position_text
       positions.append(position)
       Phone.append(phone)
       names.append(" ")
       Email.append(" ")
       domains.append(url)
       company_code = news_soup.find('span', {'class': 'sr-only'}).get_text()
       if(re.search('Home Page', company_code)):
           company_text = company_code.strip('Home Page')
       else:
           company_text = company_code
       company.append(company_text)
  
   # Next
   elif(url == urls[28]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       code = news_soup.find('div', { 'class': 'content-cols-col-100 box-gray'})
       all_names = code.p.get_text()
       names_list = all_names.split('\n')
       for each_name in names_list:
           if(re.search('Director of Water Utilities ', each_name)):
               director_name_list = each_name.split('Director of Water Utilities ')
               names.append(director_name_list[1])
       positions.append('Director of Water Utilities')
       Phone.append(" ")
       Email.append(" ")
       domains.append(url)
       company_code = news_soup.find('span', {'class': 'sr-only'}).get_text()
       if(re.search('Home Page', company_code)):
           company_text = company_code.strip('Home Page')
       else:
           company_text = company_code
       company.append(company_text)
  
   # Next
   elif(url == urls[34]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('li', {'class': 'InfoAdvanced widgetItem fr-view'})
       name = code.div.h2.get_text()
       position = code.div.span.get_text()
       email_link = code.p.a.get('href')
       email_list = email_link.split('mailto:')
       email = email_list[1]
       phone_list = code.p.next_sibling.next_sibling.next_sibling.get_text().split()
       phone = phone_list[1]
       names.append(name)
       positions.append(position.strip())
       Phone.append(phone.strip())
       Email.append(email.strip())
       domains.append(url)
       company.append('St. Joseph, MO')
  
   # Next
   elif(url == urls[38]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       first_code = news_soup.find('table', {'id': 'cityDirectoryDepartmentDetails'})
       second_code = first_code.find_next('table', {'id': 'cityDirectoryDepartmentDetails'})
       third_code = second_code.find_next('table', {'id': 'cityDirectoryDepartmentDetails'})
      
       first_info = first_code.tbody.tr.get_text().split("\n")
       second_info = second_code.tbody.tr.get_text().split("\n")
       third_info = third_code.tbody.tr.get_text().split("\n") 
       info_list = [first_info, second_info, third_info]
       code_list = [first_code, second_code, third_code]
       raw_info = []
       new_info = []
       emails = []
       for info in info_list:
           for s in info:
               raw_info.append(s.strip("\t"))
       for info in raw_info:
           if info not in stupid_blank:
               if(not re.search("Email", info)):
                   new_info.append(info) 
       i = 0 
       while i < len(new_info):
           names.append(new_info[i])
           i = i+1
           positions.append(new_info[i])
           i = i+1
           Phone.append(new_info[i])
           i = i+1   
  
       for code in code_list:
           if (re.search('Email', code.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())):
               email_code = code.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.a.get('href')
               email_text = email_code
               email_list = email_code.split(':')
               emails.append(email_list[1])
               for email in emails:
                   Email.append(email)
           else:
               Email.append(' ')
      
       for i in range(0,3):
           domains.append(url)
           company.append('City of St. Charles')
  
   # Next
   elif(url == urls[40]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('table', {'id': 'cityDirectoryDepartmentDetails'})
       table_length = len(code.tbody.find_all('tr'))
       tr_list = code.find_all("tr")
       val_list = []
       for tr in tr_list:
           td_list = tr.find_all('td')
           for td in td_list:
               if td.get_text().strip() != "Email":
                    text = td.get_text().strip()
                    val_list.append(text)
               else:
                    email = td.find("a").get('href').split(":")[1]
                    val_list.append(email)
       i = 0
       while i < len(val_list):
           names.append(val_list[i])
           i = i+1
           positions.append(val_list[i])
           i = i+1
           Email.append(val_list[i])
           i = i+1
           Phone.append(val_list[i])
           i += 2
       for i in range(table_length):
           domains.append(url)
           company.append(news_soup.title.get_text())
 
   elif(url == urls[41]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('table', {'id': 'cityDirectoryDepartmentDetails'})
       table_length = len(code.tbody.find_all('tr'))
       tr_list = code.find_all("tr")
       val_list = []
       for tr in tr_list:
           td_list = tr.find_all('td')
           for td in td_list:
               if td.get_text().strip() != "Email":
                    text = td.get_text().strip()
                    val_list.append(text)
               else:
                    email = td.find("a").get('href').split(":")[1]
                    val_list.append(email)
       i = 0
       while i < len(val_list):
           names.append(val_list[i])
           i = i+1
           positions.append(val_list[i])
           i = i+1
           Email.append(val_list[i])
           i = i+1
           Phone.append(val_list[i])
           i += 2
       for i in range(table_length):
           domains.append(url)
           company.append(news_soup.title.get_text())
   
   elif(url == urls[42]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       html_text = news_soup.get_text()
       code = news_soup.find('table', {'id': 'cityDirectoryDepartmentDetails'})
       table_length = len(code.tbody.find_all('tr'))
       tr_list = code.find_all("tr")
       val_list = []
       for tr in tr_list:
           td_list = tr.find_all('td')
           for td in td_list:
               if td.get_text().strip() != "Email":
                    text = td.get_text().strip()
                    val_list.append(text)
               else:
                    email = td.find("a").get('href').split(":")[1]
                    val_list.append(email)
       i = 0
       while i < len(val_list):
           names.append(val_list[i])
           i = i+1
           positions.append(val_list[i])
           i = i+1
           Email.append(val_list[i])
           i = i+1
           Phone.append(val_list[i])
           i += 2
       for i in range(table_length):
           domains.append(url)
           company.append(news_soup.title.get_text())

   elif(url == urls[43]):
       browser.visit(url)
       html = browser.html
       news_soup = soup(html, 'html.parser')
       code = news_soup.find('table', {'class': 'eGov_listContent'})
       table_length = len(code.tbody.find_all('tr'))
       tr_list = code.find_all("tr")
       val_list = []
       for tr in tr_list:
            td_list = tr.find_all('td')
            for td in td_list:
               est = td.find("a", {'class': 'emailLink'})
               if est == None:
                   text = td.get_text().strip()
                   val_list.append(text)
               else:
                   email = td.find("a", {'class': 'emailLink'}).get('href').split(":")[1]
                   val_list.append(email)
       i = 0
       while i < len(val_list):
           names.append(val_list[i])
           i = i+1
           positions.append(val_list[i])
           i = i+1
           i = i+1
           Email.append(val_list[i])
           i = i+1
           Phone.append(val_list[i])
           i += 1
       for i in range(table_length):
           domains.append(url)
           company.append(news_soup.title.get_text())         
 
 
       
# End of For loop
# separating first names and last names
first_names = []
last_names = []
for name in names:
  if(name != " "):
      if(re.search(",", name)):
          both_names = name.split(',')
          first_names.append(both_names[-1])
          last_names.append(both_names[0])
      else:
          both_names = name.split()
          first_names.append(both_names[0])
          last_names.append(both_names[1])
  else:
      first_names.append(" ")
      last_names.append(" ")
# END
print("===================")
print(names)
print(len(names))
print("===================")
print(first_names)
print(len(first_names))
print("===================")
print(last_names)
print(len(last_names))
print("===================")
print(positions)
print(len(positions))
print("===================")
print(Email)
print(len(Email))
print("===================")
print(Phone)
print(len(Phone))
print("===================")
print(domains)
print(len(domains))
print("===================")
print(company)
print(len(company))
print("===================")