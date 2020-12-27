import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TwitterBot():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome("./chromedriver")
        self.username = username
        self.password = password
        
    def sign_in(self):
        self.browser.get("https://www.twitter.com/login")
        time.sleep(0.3)
        usernameInput = self.browser.find_element_by_name("session[username_or_email]")
        passwordInput = self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(0.1)
    
    def tweet_something(self):
        tweet = self.browser.find_element_by_xpath(
            '''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                  /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                  /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                  /div/div/div'''
            )
        tweet.send_keys("""HELLOWWW.""")
        tweet.send_keys(Keys.COMMAND, Keys.ENTER)
        
        
        
        
if __name__ == "__main__":
    usr = input("Please enter username: ")
    passw = input("Please enter password: ")
    t_bot = TwitterBot(usr, passw)
    t_bot.sign_in()
    t_bot.tweet_something()
        
        
        
