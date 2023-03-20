import os
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class StoppableHTTPServer(HTTPServer):
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean-up server (close socket, etc.)
            self.server_close()

# Serve the VueSFC app
os.chdir('.')
httpServer = StoppableHTTPServer(server_address=('', 8000), RequestHandlerClass=CGIHTTPRequestHandler)
thread = threading.Thread(None, httpServer.run)
thread.start()

# Start tests
driver = webdriver.Chrome()
driver.get("http://localhost:8000")
assert "Bubble" in driver.title
wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.TAG_NAME, "input")))

elem = driver.find_elements(by=By.TAG_NAME, value="input")[2].click()

assert driver.current_url.endswith("authors=Hector")

circles = driver.find_elements(by=By.TAG_NAME, value="circle")
found = 0
for circle in circles:
    if circle.get_attribute("style") is "":
        found = found +1
        radius = circle.get_attribute("r")
        assert float(radius) > 56
        assert float(radius) < 58

        circle.click()

        driver.find_element(by=By.XPATH, value="//a[text()='the test pyramid is best']")

assert found is 1

import time

driver.close()

# Shutdown web server
httpServer.shutdown()
thread.join()