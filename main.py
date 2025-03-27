import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import allure
import time

#Definicion de funciones de espera y búsqueda, para simplificar escritura

driver = webdriver.Firefox()

def webWaitXPATH(path):
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{path}')]"))
    )
def webWaitCLASS(path):
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, f'{path}'))
    )
def webWaitID(path):
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.ID, f'{path}'))
    )

def findXPATH(path):
    return driver.find_element(By.XPATH,f"//a[contains(@href, '{path}')]")
def findCLASS(path):
    return driver.find_element(By.CLASS_NAME, f"{path}")
def findID(path):
    return driver.find_element(By.ID, f"{path}")

#Startup del programa
@pytest.fixture(scope="module")
def drive():
    driver.get("https://the-internet.herokuapp.com/")
    yield driver
    driver.quit()

#Prueba de Login en un form
@allure.feature("Prueba de Login")
@allure.story("Login Funcional")
@allure.severity(allure.severity_level.CRITICAL)
def test_Login(drive):
    driver.get("https://the-internet.herokuapp.com")
    webWaitXPATH("/login")
    with allure.step("Entrar a Login"):
        mouse = findXPATH("/login")
        mouse.click()
    with allure.step("Escribir Username"):
        webWaitID("username")
        mouse = findID("username")
        mouse.send_keys("tomsmith")

    with allure.step("Escribir Clave"):
        mouse = findID("password")
        mouse.send_keys("SuperSecretPassword!")
    with allure.step("Presionar Boton"):
        mouse = findCLASS("radius")
        mouse.click()
    with allure.step("Verificar Login"):
        assert driver.current_url == "https://the-internet.herokuapp.com/secure"
        print(" Prueba de Login exitosa!")

#Prueba de seleccionar un checkbox

@allure.feature("Prueba de Checkbox")
@allure.story("Checkbox Funcional")
@allure.severity(allure.severity_level.CRITICAL)
def test2():
    driver.get("https://the-internet.herokuapp.com")
    webWaitXPATH("/checkboxes")
    with allure.step("Entrar a Checkboxes"):
        mouse = findXPATH("/checkboxes")
        mouse.click()
    with allure.step("Seleccionar Checkbox"):
        webWaitID("checkboxes")
        mouse = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/form/input[2]')
        mouse.click()
    with allure.step("Verificar Checkbox"):
        assert mouse.is_selected() == False
        print(" Prueba de checkboxes exitosa!")

#Prueba de Dropdown

@allure.feature("Prueba de Dropdown")
@allure.story("Dropdown Funcional")
@allure.severity(allure.severity_level.CRITICAL)
def test3():
    driver.get("https://the-internet.herokuapp.com")
    webWaitXPATH("/dropdown")
    with allure.step("Entrar a Dropdown"):
        mouse = findXPATH("/dropdown")
        mouse.click()
    with allure.step("Seleccionar Dropdown"):
        webWaitID("dropdown")
        dropdown = Select(findID("dropdown"))
        dropdown.select_by_visible_text("Option 1")
    with allure.step("Verificar Dropdown"):
        assert dropdown.first_selected_option.text == "Option 1"
        print(" Prueba de Dropdown Exitosa")

