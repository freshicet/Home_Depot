#!/usr/bin/python
# -*- coding: utf-8 -*-
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

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87")
# change path as needed
path_to_phantomjs = 'C:\Python35\Scripts\Home_dGUI\phantomjs-2.1.1-windows/bin/phantomjs'

# A randomizer for the delay
seconds = 5 + (random.random() * 5)


def show_entry_fields():
    # create a new PhantomJS session
    driver = webdriver.PhantomJS(
        executable_path=path_to_phantomjs, desired_capabilities=dcap)
    driver.implicitly_wait(30)
    ID = e1.get()
    password_forHD = e2.get()
    # Open's a Home Depot Survey.
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
        # Open's the next page and ask, how would you describe this particular
        # shopping experience at The Home Depot compared to other
        # home improvement stores?
        # About the same is clicked.
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div[1]/div/table/tbody/tr/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,Why did you say that this shopping
        # experience was about the same compared to other home improvement
        # stores? Next is click.
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div[1]/div/table/tbody/tr/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask, How satisfied were you with each of these
        # areas during this visit to The Home Depot? Please use the full scale
        # below.
        # The time it took to check-out, from the time you got in line to the
        # time you finished paying.
        # Somewhat satisfied was click.
        # Store employees and the customer service they provided.
        # Somewhat satisfied was click.
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[4]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,
        # Thinking about this visit,how much do you agree or disagree that each of the following
        # statements describe your experience at The Home Depot? Please use the full scale below.
        # The store was generally neat and clean
        # Neither agree nor disagree was click.
        # Had sufficient quantities of product in-stock on the shelves.
        # Neither agree nor disagree was click.
        # The cashier was friendly.
        # Neither agree nor disagree was click.
        # Employees were consistently friendly throughout the store.
        # Neither agree nor disagree was click.
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
        # Open's the next page and ask,
        # Still thinking about this visit.
        # Did you require assistance from a store employee?
        # No was click.
        # Did you receive assistance from a store employee?
        # No was click.
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]/input')
        element.click()
        element = driver.find_element_by_xpath(
            '//*[@id="surveyform"]/div[1]/div/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[3]/input')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,
        # You indicated that there were not sufficient quantities of products on the shelves. 
        # In what area(s) were you looking for product(s) that were not available in sufficient quantities?
        # Tool Rental was click.
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_outofstock_tool_rental_yn_1"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,
        # Is there anything else you would like to tell us about your visit or is 
        # there anything we could do to improve your shopping experience?
        # I do not have anything else to share was click.
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_catchall_oe_optout_yn_1"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,
        # You indicated you were not satisfied with store employees and the customer service they provided.
        # No, please do not contact me was click.
        element = driver.find_element_by_xpath(
            '//*[@id="i_onf_q_thd_contact_radio_3"]')
        element.click()
        driver.find_element_by_id("nextButton").click()
        time.sleep(seconds)
        # Open's the next page and ask,
        # Input Name and Email
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
    finally:
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
