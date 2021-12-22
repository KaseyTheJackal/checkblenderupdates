import unittest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://builder.blender.org/download/daily")
items = driver.find_elements(By.ID, "builds-list platform-darwin active")

for item in items:
    text = item.text
    print(text)

driver.close()
