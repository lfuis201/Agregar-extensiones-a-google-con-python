from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_extension('D:\programacion\python\extensions\Python-Shell.crx')    #añadir directorio de la extension
driver = webdriver.Chrome(options=chrome_options, executable_path='D:\programacion\python\extensions\chromedriver')    #añadir directorio de chromedriver
driver.get('https://www.google.co.in')