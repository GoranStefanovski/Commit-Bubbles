import os
import time
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

driver.find_element(by=By.XPATH, value="//input[@value='Hector']").click()

assert driver.current_url.endswith("authors=Hector")

circle = driver.find_element(by=By.CSS_SELECTOR, value="circle[shown=true]")
assert float(circle.get_attribute("cx")) == 522
assert float(circle.get_attribute("cy")) == 406
assert float(circle.get_attribute("r")) == 18

circle.click()

driver.find_element(by=By.XPATH, value="//a[text()='the test pyramid is best']")

time.sleep(1)

driver.close()

# Shutdown web server
httpServer.shutdown()
thread.join()