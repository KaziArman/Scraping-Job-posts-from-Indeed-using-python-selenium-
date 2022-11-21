#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install selenium')


# In[ ]:


get_ipython().system('pip install pandas')


# In[ ]:


get_ipython().system('pip install win-unicode-console')


# In[ ]:


get_ipython().system('pip install webdriver-manager')


# In[ ]:


import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from IPython.core.display import display,HTML
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import os
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
print('Done')


# In[ ]:


url = 'https://www.indeed.co.in/?from=gnav-jobsearch--jasx'
driver.get(url)
print('Done')


# In[ ]:


keyword = 'plumber'
k = driver.find_element_by_xpath('//*[@id="text-input-what"]')
k.send_keys(keyword)
time.sleep(2)
print('Done')


# In[ ]:


search = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
webdriver.ActionChains(driver).move_to_element(search).click(search).perform()
driver.implicitly_wait(10)
time.sleep(2)
print('Done')


# In[ ]:


Dic = {}
gc=pd.DataFrame(data=Dic,index=[0], columns=['Post','Company Name','Location','Salary','Qualification','Experience','Apply Link','Job Info'])
print('Done')


# In[ ]:


q = 0
u = 0
for url in range(50):
    url = 'https://www.indeed.co.in/jobs?q='+ str(keyword) +'&sort=date&fromage=last&start='+ str(q) +''
    driver.get(url)
    q = q + 10
    time.sleep(5)
    i = 0
    for p in range(15):
        try:
            try:
                cmpny = driver.find_elements_by_css_selector('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading6.company_location.tapItem-gutter > pre > span.companyName') 
                cmpny = cmpny[i].text
                driver.implicitly_wait(10)
                time.sleep(4)
            except:
                cmpny = 'NOT AVAILABLE'
            try:
                
                loc = driver.find_elements_by_css_selector('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading6.company_location.tapItem-gutter > pre > div')
                loc = loc[i].text
                driver.implicitly_wait(10)
                time.sleep(4)
                print(loc)
            except:
                loc = 'NOT AVAILABLE'
            try:
                post = driver.find_elements_by_css_selector('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading4.color-text-primary.singleLineTitle.tapItem-gutter > h2 > span')
                post = post[i].text
                print(post)
                driver.implicitly_wait(10)
                #print(i)
                time.sleep(4)
            except:
                post = 'NOT AVAILABLE'
            
            clks= driver.find_elements_by_css_selector('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading4.color-text-primary.singleLineTitle.tapItem-gutter > h2 > span')[i]
            driver.execute_script("arguments[0].click();", clks)
            time.sleep(5)
            
            
            try:
                sal = driver.find_elements_by_css_selector('div.slider_container > div > div.slider_item > div > table.jobCard_mainContent > tbody > tr > td > div.heading6.tapItem-gutter.metadataContainer > div > span')
                sal = sal[i].text
                print(sal)
                driver.implicitly_wait(10)
                time.sleep(4)
            except:
                sal = 'Negotiable'
                print(sal)
            
            try:
                link = driver.current_url
                print(link)
                driver.implicitly_wait(20)
                time.sleep(3)
                
            except:
                try:
                    
                    li = driver.find_elements_by_css_selector('a.tapItem.fs-unmask.result.job_31cef8b84f3a88f0.resultWithShelf.sponTapItem.desktop')
                    link = li[i].get_attribute('href')
                    print(link)
                    driver.implicitly_wait(10)
                    time.sleep(4)
                except IndexError:
                    link = "Not Collectable"
            
            try:
                #jd2 = driver.find_element_by_css_selector('div#vjs-desc') #vjs-desc > div:nth-child(2)
                jd = driver.find_elements_by_css_selector('div.job-snippet > ul > li')
                jd = jd[i].text
                #jd2 = jd2.text
                #print(jd2)
                print(jd)
                time.sleep(4)
                driver.implicitly_wait(10)
            except:
                jd = "NOT AVAILABLE"
            
            with open('lets_welder.txt','w',encoding='cp1252', errors='ignore') as g:
                p= str(jd)
                g.write(p)
                
            with open('lets_welder.txt',encoding='cp850', errors='replace') as fo:
                f = fo.readlines()
                l = len(f)
                find = 'Qualification'
                find2 = 'Experience'
                k=[]
                h=[]
                n=[]
                k.clear()
                h.clear()
                n.clear()
                a = ''
                b = ''
                c = ''

                for w in range(l):
                    if find in f[w]:
                        h.append(f[w])
                        a = "".join(h)
                        a = a.replace("\n","")
                        a = a.replace("''","")
                        print(a)
                    elif find2 in f[w]: 
                        n.append(f[w])
                        b = "".join(n)
                        b = b.replace("\n","")
                        b = b.replace("''","")
                        print(b)
                    else:
                        k.append(f[w])
                        c = "".join(k)
                        c = c.replace("\n",'*')
                        c = c.replace('*','\n')
                        c = c.replace("''","")
                        w = "<pre>"
                        v = "</pre>"
                        c = w + c + v
                        time.sleep(4)

            Dic = {'Post':post,'Company Name':cmpny,'Location':loc,'Salary':sal,'Job Info':c,'Qualification':a,'Experience':b,'Apply Link':link}
            

            gc = gc.append(Dic, ignore_index=True)
            
            i = i + 1
            print(gc)
            gc.to_excel('jobs_'+str(keyword)+'.xlsx')
            time.sleep(2)
            os.remove('lets_welder.txt')
               
        except NoSuchElementException as e:
            continue 
            
        except IndexError as x:
            driver.get(url)
            i = 0
            time.sleep(2)
            continue
            
        except TimeoutException as t:
            time.sleep(900)
            continue 


# In[ ]:




