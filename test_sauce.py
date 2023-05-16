from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
  def test_invalid_login(self):
        #
        WebDriverWait(self.driver,timeout=4).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))   
        usernameInput = self.driver.find_element(By.ID , "user-name")
        WebDriverWait(self.driver,timeout=4).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID , "Password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element,(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3" )
        testResult = errorMessage.text == "Kullanıcı adı ve şifre bu hizmetteki hiçbir kullanıcıyla eşleşmiyor"
        print(f"TEST SONUCU:{testResult}")
def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,timeout=4).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))   
        usernameInput = self.driver.find_element(By.ID , "user-name")
        WebDriverWait(self.driver,timeout=4).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID , "Password")
        self.driver.execute_script("window.scrollTo(0,500)")
        #eylem zinciri
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(usernameInput, "secret_sauce")
        actions.perform()
        #perform ilgili aksiyonları çalıştır demek.
        loginBtn = self.driver.find_element(By.ID , "login-button")
        loginBtn.click()
        


testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_invalid_login()


while True:
    continue


 #unital (şu alana kadar bekle demek)
#14. satırın açıklaması : web drivırımı 5 satiye beklet , ne zamana kadar ? loketırla bir elementin görünür olmasını bekle.Görünmez olmasa bile 5 saniye geçmiş ise onu görünür yap.
#çift parantezin sebebi tek bir alanda tanımalamam lazım onun için locator açtık yukarı.tek parametrede gönderiyoruz
#send_keys kısmı çalışmıyor ve githubdan kontrolü yapılmadı 
#parolla kısımlarıda çalışmıyor