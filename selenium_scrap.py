from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("http://www.in.gov.br/leiturajornal?data=12-04-2019&secao=dou2")
p_element = driver.find_elements_by_xpath(xpath=".//*[text()='instituto federal de educação, ciência e tecnologia de pernambuco']/following::ul[1]/li/a")

for x in p_element:
    driver2 = webdriver.PhantomJS()
    driver2.get(x.get_attribute('href'))
    time.sleep(5)
    identifica = driver2.find_elements_by_class_name("identifica")
    dou_paragraph = driver2.find_elements_by_class_name("dou-paragraph")

    print("Texto: " + identifica[1].text)
    for dou in dou_paragraph:
        if dou.text:
            print("Paragrafo: " + dou.text)
    driver2.quit()
