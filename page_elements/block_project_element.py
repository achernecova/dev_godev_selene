from selene import browser


class BlockProjectElement:
    # локатор блока с карточками
    cards = browser.all(".projects-item")

    @staticmethod
    def button_project():
        return browser.all(".projects-item")
