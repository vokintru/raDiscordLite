import selenium.webdriver
import cfg
from selenium.webdriver.common.by import By
import time

WAIT_TIME = 2


class WebDriver:
    def __init__(self):
        driver = selenium.webdriver.Firefox()
        driver.get("https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications%2F")
        driver.implicitly_wait(5)

        # login
        login, password = cfg.LOGIN_PASSWORD
        driver.find_element(By.NAME, "email").send_keys(login)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div/div['
                            '1]/div[2]/button[2]').click()
        driver.implicitly_wait(5)

        # # creating new app
        # driver.find_element(By.CSS_SELECTOR,
        #                     "html.theme-dark body div#app-mount div.wrapper-2dJhXi div.shakeShake-1CacCa "
        #                     "div.content-1VQSdr div.contentWrapper-3RqEiS "
        #                     "div.page-content-scrolling-container.scroller-31PUfV.auto-2Csyba.scrollerBase-znEu6g "
        #                     "div.contentWrapperInner-1826hB div.marginBottomMedium-1Z1lwQ h2.heading-3LwKGe "
        #                     "div.contentSecondary-3MwfB_ "
        #                     "button.button-f2h6uQ.filledBrand-3fai8P.filledDefault-25rIra.buttonHeightMedium-2UpIaI"
        #                     ".unpaired-GdFe-D").click()
        # driver.find_element(By.CSS_SELECTOR,
        #                     "html.theme-dark body div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyCenter-3VdGrQ"
        #                     ".flexAlignCenter-8FgVwZ.flexWrap-A0-NZQ.modal-3Ezlpn "
        #                     "div.modalContent-31OOYM.overflowOverride-3QlLNG form div.modalInner-AkIGqy "
        #                     "div.grid-2a45cj "
        #                     "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
        #                     ".flexWrap-A0-NZQ div.flexChild-3PzYmX.child-GVttEz.columnSpread12-38DH5j "
        #                     "div.inputWrapper-1YNMmM.undefined input.inputDefault-3FGxgL.input-2g-os5").send_keys(
        #     "TestBot")
        # driver.find_element(By.CSS_SELECTOR,
        #                     "html.theme-dark body div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyCenter-3VdGrQ"
        #                     ".flexAlignCenter-8FgVwZ.flexWrap-A0-NZQ.modal-3Ezlpn "
        #                     "div.modalContent-31OOYM.overflowOverride-3QlLNG form div.modalInner-AkIGqy "
        #                     "div.grid-2a45cj "
        #                     "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
        #                     ".flexWrap-A0-NZQ "
        #                     "div.flexChild-3PzYmX.legalLinksSection-PIFvHC.child-GVttEz.columnSpread12-38DH5j "
        #                     "label.checkboxWrapper-2fDzaA input.inputDefault-2F39XG.input-3xr72x").click()
        # driver.find_element(By.CSS_SELECTOR,
        #                     "html.theme-dark body div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyCenter-3VdGrQ"
        #                     ".flexAlignCenter-8FgVwZ.flexWrap-A0-NZQ.modal-3Ezlpn "
        #                     "div.modalContent-31OOYM.overflowOverride-3QlLNG form footer.modalFooter-3193QM "
        #                     "button.button-f2h6uQ.filledBrand-3fai8P.filledDefault-25rIra.buttonHeightTall-Yz4Cm8"
        #                     ".unpaired-GdFe-D.createButton-3UAgy2").click()
        # time.sleep(WAIT_TIME)
        # driver.implicitly_wait(5)
        #
        # # save app_id
        # self.APP_ID = int(driver.current_url.split("/")[-2])

        self.APP_ID = 1241105403048362075
        # get bot token
        driver.get(f"https://discord.com/developers/applications/{self.APP_ID}/bot")
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR,
                            "html.theme-dark body div#app-mount div.wrapper-2dJhXi div.shakeShake-1CacCa "
                            "div.content-1VQSdr div.contentWrapper-3RqEiS "
                            "div.page-content-scrolling-container.scroller-31PUfV.auto-2Csyba.scrollerBase-znEu6g "
                            "div.contentWrapperInner-1826hB div.marginBottomMedium-1Z1lwQ form div.grid-2a45cj "
                            "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
                            ".flexWrap-A0-NZQ "
                            "div.flexChild-3PzYmX.child-GVttEz.columnSpread8-1Vhmre.columnSpreadExtraSmall12-1lxCVe"
                            ".columnSpreadSmall12-3hQlq4 div.grid-2a45cj "
                            "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
                            ".flexWrap-A0-NZQ div.flexChild-3PzYmX.child-GVttEz.columnSpread12-38DH5j "
                            "div.buttonWrap-2vdVmn "
                            "button.button-f2h6uQ.filledBrand-3fai8P.filledDefault-25rIra.buttonHeightShort-5JiyOY"
                            ".unpaired-GdFe-D").click()
        driver.find_element(By.CSS_SELECTOR,
                            "html.theme-dark body div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyCenter-3VdGrQ"
                            ".flexAlignCenter-8FgVwZ.flexWrap-A0-NZQ.modal-3Ezlpn div.modalContent-31OOYM "
                            "footer.modalFooter-3193QM "
                            "button.button-f2h6uQ.filledPrimary-3zeYrF.filledDefault-25rIra.buttonHeightTall-Yz4Cm8"
                            ".unpaired-GdFe-D.modalFooterButton-2Kh0NI").click()
        driver.find_element(By.CSS_SELECTOR, "html.theme-dark body div.flex-2S1XBF.flexHorizontal-humxgD"
                                             ".flexJustifyCenter-3VdGrQ.flexAlignCenter-8FgVwZ.flexWrap-A0-NZQ.modal"
                                             "-3Ezlpn div.modalContent-31OOYM form div.modalInner-AkIGqy "
                                             "div.grid-2a45cj "
                                             "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq"
                                             ".flexAlignStretch-1BJbuT.flexWrap-A0-NZQ "
                                             "div.flexChild-3PzYmX.child-GVttEz.columnSpread12-38DH5j "
                                             "div.inputWrapper-1YNMmM.undefined "
                                             "input.inputDefault-3FGxgL.input-2g-os5").send_keys(password)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,
                            "html.theme-dark body div#app-mount div.wrapper-2dJhXi div.shakeShake-1CacCa "
                            "div.content-1VQSdr div.contentWrapper-3RqEiS "
                            "div.page-content-scrolling-container.scroller-31PUfV.auto-2Csyba.scrollerBase-znEu6g "
                            "div.contentWrapperInner-1826hB div.marginBottomMedium-1Z1lwQ form div.grid-2a45cj "
                            "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
                            ".flexWrap-A0-NZQ "
                            "div.flexChild-3PzYmX.child-GVttEz.columnSpread8-1Vhmre.columnSpreadExtraSmall12-1lxCVe"
                            ".columnSpreadSmall12-3hQlq4 div.grid-2a45cj "
                            "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq.flexAlignStretch-1BJbuT"
                            ".flexWrap-A0-NZQ div.flexChild-3PzYmX.child-GVttEz.columnSpread12-38DH5j "
                            "div.buttonWrap-2vdVmn "
                            "button.button-f2h6uQ.filledBrand-3fai8P.filledDefault-25rIra.buttonHeightShort-5JiyOY"
                            ".unpaired-GdFe-D").click()

        self.TOKEN = driver.find_element(By.CSS_SELECTOR,
                                         "html.theme-dark body div#app-mount div.wrapper-2dJhXi div.shakeShake-1CacCa "
                                         "div.content-1VQSdr div.contentWrapper-3RqEiS "
                                         "div.page-content-scrolling-container.scroller-31PUfV.auto-2Csyba"
                                         ".scrollerBase-znEu6g "
                                         "div.contentWrapperInner-1826hB div.marginBottomMedium-1Z1lwQ form "
                                         "div.grid-2a45cj "
                                         "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq"
                                         ".flexAlignStretch-1BJbuT "
                                         ".flexWrap-A0-NZQ "
                                         "div.flexChild-3PzYmX.child-GVttEz.columnSpread8-1Vhmre"
                                         ".columnSpreadExtraSmall12-1lxCVe "
                                         ".columnSpreadSmall12-3hQlq4 div.grid-2a45cj "
                                         "div.flex-2S1XBF.flexHorizontal-humxgD.flexJustifyStart-3aWekq"
                                         ".flexAlignStretch-1BJbuT "
                                         ".flexWrap-A0-NZQ "
                                         "div.flexChild-3PzYmX.child-GVttEz"
                                         ".columnSpread12-38DH5j").get_attribute("text")


if __name__ == '__main__':
    test = WebDriver()
    print(f"APP ID: {test.APP_ID}\n"
          f"TOKEN: {test.TOKEN}")
