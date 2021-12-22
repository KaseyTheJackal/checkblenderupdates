import unittest
from selenium import webdriver

driver = webdriver.driver

driver.get("https://builder.blender.org/download/daily")
driver.title("Architecture")

