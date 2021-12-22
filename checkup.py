import unittest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari

driver.get("https://builder.blender.org/download/daily")
driver.title("Architecture")

