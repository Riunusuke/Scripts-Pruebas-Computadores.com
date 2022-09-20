from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Proyecto Computadores.com
    Package: TestProject.Generated.Tests.ProyectoComputadorescom
    Test: CP-02.2
    Generated by: Andres Diaz (diazandresfelipe91@gmail.com)
    Generated on 09/20/2022, 19:52:16
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="6vg3AYBdNyUgmB8Dn2JI8usHfm5RJkaE6bkMe7kVMXI",
                              project_name="Proyecto Computadores.com",
                              job_name="CP-02.2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Se busca comprobar que el usuario no sea capaz de ingresar a su cuenta si la contraseña no es correcta."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost/wordpress/"
    Correo = ""
    Password = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Cuenta'
    cuenta = driver.find_element(By.XPATH,
                                 "//li[3]/a[. = 'Cuenta']")
    cuenta.click()

    # 3. Type '{Correo}' in 'username-13'
    username_13 = driver.find_element(By.CSS_SELECTOR,
                                      "#username-13")
    username_13.send_keys(f'{Correo}')

    # 4. Type '{Password}' in 'user_password-13'
    user_password_13 = driver.find_element(By.CSS_SELECTOR,
                                           "#user_password-13")
    user_password_13.send_keys(f'{Password}')

    # 5. Click 'um-submit-btn'
    um_submit_btn = driver.find_element(By.CSS_SELECTOR,
                                        "#um-submit-btn")
    um_submit_btn.click()

    # 6. Click 'La contraseña es incorrecta. Por favo...1'
    la_contrase_a_es_incorrecta_por_favo_1 = driver.find_element(By.XPATH,
                                                                 "//p[. = 'La contraseña es incorrecta. Por favor, inténtalo de nuevo.']")
    la_contrase_a_es_incorrecta_por_favo_1.click()
