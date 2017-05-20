# The main app for doing Home Depot survey.
# It Has a GUI interface that you are able to put in ID and Password from
# Home Depot receipts.
# The GUI Front-End is using Tkinter.
# The Back end is using selenium.

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tkinter import *
from Info_HD import First_name, Last_name, Email, zip_code
import random
import time

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
#     "(KHTML, like Gecko) Chrome/15.0.87")

# path_to_phantomjs = 'C:\Python35\Scripts\Home_dGUI\phantomjs-2.1.1-windows/bin/phantomjs'  # change path as needed
# driver = webdriver.PhantomJS(
#     executable_path=path_to_phantomjs, desired_capabilities=dcap)
path_to_Chrome = 'C:\Python35\Scripts\Home_dGUI\chromedriver.exe'
# A randomizer for the delay
seconds = 5 + (random.random() * 5)


def show_entry_fields():
    # create a new Chrome session
    driver = webdriver.Chrome(path_to_Chrome)
    driver.implicitly_wait(30)
    ID = e1.get()
    password_forHD = e2.get()
    # Open a Home Depot Survey.
    driver.get("https://survey.medallia.com/?thehomedepot")
    driver.find_element_by_id("beginButton").click()
    time.sleep(seconds)
    zipcode = driver.find_element_by_xpath(
        '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div[1]/div/input')
    # Zipcode input
    zipcode.send_keys(zip_code)
    driver.find_element_by_id("nextButton").click()
    time.sleep(seconds)
    driver.find_element_by_id("nextButton").click()
    time.sleep(seconds)
    id = driver.find_element_by_name('spl_q_thd_receiptcode_id_entry_text')
    # ID input
    id.send_keys(ID)
    password = driver.find_element_by_name(
        'spl_q_thd_receiptcode_password_entry_text')
    # Password input
    password.send_keys(password_forHD)
    driver.find_element_by_id("nextButton").click()
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="i_onf_q_thd_pro_classification_none_consumer_yn_1"]'))
        )
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open the next page which ask how would you describe this particular
        # shopping experience at The Home Depot compared to other home improvement
        # stores?
        # About the same is clicked.
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div[1]/div/table/tbody/tr/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton")
        time.sleep(seconds)
        element.click()
        # Open the next page ask
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div[1]/div/table/tbody/tr/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[3]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[4]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[3]/td[4]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[4]/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[3]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_outofstock_tool_rental_yn_1"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_catchall_oe_optout_yn_1"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_contact_radio_3"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        first_name = driver.find_element_by_name(
            'spl_q_thd_contact_first_name_text')
        # Frist name input
        first_name.send_keys(First_name)
        last_name = driver.find_element_by_name(
            'spl_q_thd_contact_last_name_text')
        # Last name input
        last_name.send_keys(Last_name)
        e_mail = driver.find_element_by_name(
            'spl_q_thd_contact_email_sweeps_text')
        # Email input
        e_mail.send_keys(Email)
        driver.find_element_by_id("finishButton").click()
        driver.quit()

master = Tk()

Label(master, text="ID").grid(row=0)
Label(master, text="password").grid(row=1)


e1 = Entry(master)
e2 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(
    row=7, column=0, sticky=W, pady=4)
Button(master, text='Enter', command=show_entry_fields).grid(
    row=8, column=1, sticky=W, pady=4)


mainloop()
