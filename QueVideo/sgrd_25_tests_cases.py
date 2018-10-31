__author__ = 'johanna gutierres - nestor romero'

from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Sgrd25FunctionalTest(TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome('E:\\Nestor\\OneDrive\\Documentos\\uniandes\\201820\\procesos agiles\\chromedriver.exe')
        self.browser = webdriver.Chrome('E:\\chromedriver_win32\\chromedriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_crudo_list_link_location(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        botonMenu = self.browser.find_element_by_id('sidebar-collapse-btn')
        botonMenu.click()

        span = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "produccionSpan")))
        span.click()

        span2 = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Listado de Crudos"]')))
        self.assertIn('Listado de Crudos', span2.text)

    def test_crudo_list(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        botonMenu = self.browser.find_element_by_id('sidebar-collapse-btn')
        botonMenu.click()

        span = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "produccionSpan")))
        span.click()

        span2 = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="Listado de Crudos"]')))
        span2.click()

        self.browser.implicitly_wait(3)

        description = self.browser.find_element_by_id('list_description')
        self.assertIn('Muestra los crudos registrados en el recurso:', description.text)