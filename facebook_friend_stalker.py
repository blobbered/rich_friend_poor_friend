def http_not_working_version:
  import httplib
  fb_conn = httplib.HTTPConnection('www.facebook.com')
  fb_conn.request("GET", "/friends/edit")
  friends_page_response = fb_conn.getresponse()
  print friends_page_response.status, friends_page_response.reason
  page = friends_page_response.read()
  print friends_page_response.msg
  print friends_page_response.getheaders()
  print page
  fb_conn.close()



def selenium_version
    from selenium import webdriver
    
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/me/friends")
    ready_state_complete = false
    while(!ready_state_complete):
      driver.execute_script("window.scrollTo(0, document.body.offsetHeight)")
      ready_state_complete = driver.execute_script("return document.readyState")
