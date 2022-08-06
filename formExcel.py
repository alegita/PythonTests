# Imports
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

with open('FormTestExcel.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)