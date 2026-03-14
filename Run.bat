pytest -v -s -n=2 --html=Html_Reports\OrangeHRM_Login_chrome.html --alluredir=Allure_Reports --browser chrome
pytest -v -s -n=2 --html=Html_Reports\OrangeHRM_Login_firefox.html --alluredir=Allure_Reports --browser firefox
pytest -v -s -n=2 --html=Html_Reports\OrangeHRM_Login_edge.html --alluredir=Allure_Reports --browser edge
pytest -v -s -n=2 --html=Html_Reports\OrangeHRM_Login_headless.html --alluredir=Allure_Reports --browser headless
