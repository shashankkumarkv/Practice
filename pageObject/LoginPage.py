from selenium import webdriver

class LoginPage:
        ##credentials##
        usename = "admin@yourstore.com"
        password = "admin"
        loginButton = ""


    def __init__(self, driver):
        self.driver = driver


