import time
from selenium import webdriver
from word_cloud import WordCloud
import matplotlib.pyplot as plt



driver = webdriver.Chrome("./chromedriver")

driver.get('https://coinmarketcap.com/ko/'); 

last_height = driver.execute_script("return document.body.scrollHeight")   

start = -100
end = 0
for i in range(last_height//100):
    start += 100
    end += 100
    driver.execute_script("window.scrollTo(" + str(start) + "," + str(end)+");")   
    time.sleep(0.1)   


quar = driver.find_elements_by_css_selector("p.sc-1eb5slv-0.gGIpIK.coin-item-symbol")
coinInfo = []


count = 0
printC = 0
mindT=[]

for j in quar:
    printC += 1
    count += 1
    mindT.append(j.text)


time.sleep(1)         
  
btcCloud=(" ").join(mindT)
wordcloud = WordCloud(background_color='black',width = 2000, height = 800).generate(btcCloud)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("project.png",bbox_inches='tight')
plt.show()
plt.close()

driver.quit()