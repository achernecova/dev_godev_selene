from selene import browser, have


class BlockOtherServices:

    cards = browser.all(".projects-item")

    @staticmethod
    def button_other_services_more():
        return browser.all(".services-slider__card a").by(have.exact_text("More"))
