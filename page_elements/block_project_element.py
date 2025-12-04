from selene import browser


class BlockProjectElement:
    # локатор блока с карточками
    cards = browser.all(".projects-item")

    def button_project(self):
        return browser.all(".projects-item")
