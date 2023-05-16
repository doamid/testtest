from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(3)
input = driver.find_element(By.NAME, "q" )
input.send_keys("kodlamaiö")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_element(By.CLASS_NAME , "course-listing")
print(f"Kodlamaiö sitesinde şu anda {len(listOfCourses)}adet kurs var")
# sleep(10) bekletme süresidir 
while True:
   continue 
     
# HTML LOCALORS 
#input() chrome kapanmamasını sağlar 
#sleep(10) kodu uyku moduna alır
#input.send_keys("kodlamaiö") yazarsam googlda kodlmaiö yazar
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a
