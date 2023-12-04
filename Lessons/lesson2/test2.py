
def test_step1(site):
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    # print(err_label.text) должен показать ошибку 401
    assert err_label.text == "401"

# test_step1()


# высота элемента
# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# # цвет элемента копируем по клику на код элемента копи икспас
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))


# driver_path: chromedriver.exe в ямл если используем скаченный драйвер
