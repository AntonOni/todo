import pytest
import time



@pytest.mark.usefixtures("test_setup")
class TestSuite():

    @pytest.mark.usefixtures("test_begin")
    def test_login(self, test_setup):
        chrome = test_setup
        time.sleep(2)
        chrome.find_element_by_class_name("btn").click()
        time.sleep(2)
        chrome.find_element_by_id("taskName").send_keys("AntonUser111")
        time.sleep(2)
        chrome.find_element_by_id("taskDescription").send_keys("UserAnton111")
        time.sleep(2)
        chrome.find_element_by_class_name("btn").click()
        time.sleep(2)

        alert = chrome.switch_to.alert
        assert alert.text == "Tarefa enviada com sucesso!"
        alert.accept()

        time.sleep(2)
        list_of_pages = chrome.find_elements_by_class_name("paginate_button ")
        print(len(list_of_pages))
        list_of_pages[-2].click()
        time.sleep(2)
        table_rows = chrome.find_elements_by_tag_name("tr")
        last_row = table_rows[-1]
        td_el_last_row = last_row.find_elements_by_tag_name("td")
        tag_name = td_el_last_row[1].text
        tag_last = td_el_last_row[2].text
        assert tag_name == "AntonUser111"
        assert tag_last == "UserAnton111"


    @pytest.mark.usefixtures("test_begin")
    def test_some(self):
        print("Some Test 111")
