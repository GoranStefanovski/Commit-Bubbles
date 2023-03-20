import os
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class StoppableHTTPServer(HTTPServer):
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean-up server (close socket, etc.)
            self.server_close()


# Make sure the server is created at current directory
os.chdir('.')
# Create server object listening the port 80
httpServer = StoppableHTTPServer(server_address=('', 8000), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
# Start processing requests
thread = threading.Thread(None, httpServer.run)
thread.start()

print("Start tests")

from autotest_lib.client.common_lib.cros import chromedriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# Shutdown server
httpServer.shutdown()
thread.join()