from selenium import webdriver
import time 


browser= webdriver.Chrome()

url="https://accounts.google.com/o/oauth2/auth/identifier?response_type=code&access_type=offline&client_id=451050238842-stelcbipu0o33seaasv3sd3gt8ktilti.apps.googleusercontent.com&redirect_uri=https%3A%2F%2F10fastfingers.com%2Faccount%2Fgoogle_oauth2callback&state&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&approval_prompt=auto&flowName=GeneralOAuthFlow"

browser.get(url)

input_alani=browser.find_element_by_xpath("//*[@id='identifierId']")

input_alani.send_keys("mehmetyasinyeles@gmail.com")

buton=browser.find_element_by_xpath("//*[@id='identifierNext']/div/button")

buton.click()

time.sleep(1)

sifre=browser.find_element_by_name("password")

sifre.send_keys("evxpyj11")

buton2=browser.find_element_by_xpath("//*[@id='passwordNext']/div/button")

buton2.click()

time.sleep(3)

browser.get("https://10fastfingers.com/typing-test/turkish")

time.sleep(3)

i=1

input_alani2=browser.find_elements_by_xpath("//*[@id='inputfield']")

while i<200:
    
    kelime= browser.find_elements_by_xpath("//*[@id='row1']/span["+str(i)+"]")
    
    input_alani2.send_keys(kelime.text +" ")
    i+=1
    time.sleep(0.1)