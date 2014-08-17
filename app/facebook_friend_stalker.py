from selenium.webdriver.support.ui import WebDriverWait

def get_friend_data():
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    ask_user_to_log_in(driver)
    load_friends_page(driver)
    friend_urls = get_urls_of_friends(driver)
    return get_friend_occupations(friend_urls, driver)

def ask_user_to_log_in(driver):
    driver.get("https://www.facebook.com")
    logged_in = raw_input("Have you logged in?")
    while not logged_in:
        print "Please log in to get your friend data."
        logged_in = raw_input("You are logged in. True/False?")

def load_friends_page(driver):
    print "Getting friends..."
    driver.get("https://www.facebook.com/me/friends")

    def friends_section_finished(driver):
        try:
            for element in driver.find_elements_by_class_name("uiHeaderTitle"):
                if "More About " in element.text:
                    return True
            return False
        except:
            print "Problem getting element text."
    def is_source_changed(driver):
        try:
            return source != driver.page_source
        except WebDriverException:
            pass

    while not friends_section_finished(driver):
        source = driver.page_source
        driver.execute_script("window.scrollTo(0, document.body.offsetHeight)")
        WebDriverWait(driver, 10).until(is_source_changed)
 
def get_urls_of_friends(driver):
    print "Getting friend urls..."
    friend_urls = []
    friends = driver.find_elements_by_class_name("fcb")
    for web_element in friends:
        profile_a_tag = web_element.find_element_by_tag_name("a")
        profile_url = profile_a_tag.get_attribute("href")
        friend_urls.append(profile_url)
#    print "Friend urls retrieved: " + str(len(friend_urls))
    return friend_urls
       
def get_friend_occupations(friend_urls, driver):
    occupations = []

    def get_work(driver):
        work_tags = driver.find_elements_by_class_name("_4_ug")
        return work_tags[0].text

    for url in friend_urls:
        name = None
        work = None
        tries = 0
        while (work is None or name is None) and tries < 5:
            tries += 1
            driver.get(url) 
            name = driver.find_elements_by_class_name("_8_2")[0].text
            try:
                work = get_work(driver)
                employer = work.split(" at ", 1)[1]
                occupation = work.split(" at ", 1)[0]
            except:
                pass
        user_data = {'name': name, 'employer': employer, 'title': occupation} 
        occupations.append(user_data)
    return occupations

def main():
    get_friend_data()

if __name__ == "__main__":
    main()
