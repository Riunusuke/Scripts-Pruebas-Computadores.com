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
    Test: CP-04.2
    Generated by: Andres Diaz (diazandresfelipe91@gmail.com)
    Generated on 09/20/2022, 19:53:28
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="6vg3AYBdNyUgmB8Dn2JI8usHfm5RJkaE6bkMe7kVMXI",
                              project_name="Proyecto Computadores.com",
                              job_name="CP-04.2")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Se busca comprobar que el usuario no sea capaz de aplicar cupones que no se encuentren registrados en la base de datos."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost/wordpress/"
    Correo = ""
    Password = ""
    Codigo = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Salir'
    salir = driver.find_element(By.XPATH,
                                "//li[5]/a[. = 'Salir']")
    salir.click()

    # 3. Click 'Cuenta'
    cuenta = driver.find_element(By.XPATH,
                                 "//li[3]/a[. = 'Cuenta']")
    cuenta.click()

    # 4. Type '{Correo}' in 'username-13'
    username_13 = driver.find_element(By.CSS_SELECTOR,
                                      "#username-13")
    username_13.send_keys(f'{Correo}')

    # 5. Type '{Password}' in 'user_password-13'
    user_password_13 = driver.find_element(By.CSS_SELECTOR,
                                           "#user_password-13")
    user_password_13.send_keys(f'{Password}')

    # 6. Click 'um-submit-btn'
    um_submit_btn = driver.find_element(By.CSS_SELECTOR,
                                        "#um-submit-btn")
    um_submit_btn.click()

    # 7. Click 'Carrito'
    carrito = driver.find_element(By.XPATH,
                                  "//li[4]/a[. = 'Carrito']")
    carrito.click()

    # 8. Type '{Codigo}' in 'coupon_code'
    coupon_code = driver.find_element(By.CSS_SELECTOR,
                                      "#coupon_code")
    coupon_code.send_keys(f'{Codigo}')

    # 9. Click 'apply_coupon'
    apply_coupon = driver.find_element(By.CSS_SELECTOR,
                                       "[name='apply_coupon']")
    apply_coupon.click()

    # 10. Click '¡El cupón «descuento» no existe!2'
    _el_cup_n_descuento_no_existe_2 = driver.find_element(By.XPATH,
                                                          "//ul[. = '\n\t\t\t\n\t\t\t¡El cupón «descuento» no existe!\t\t\n\t']")
    _el_cup_n_descuento_no_existe_2.click()
