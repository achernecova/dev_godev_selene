from selene import browser, have


class WebSitePackagesBlockSelene:
    # локатор блока с карточками
    cards = browser.all(".team")

    def button_website_packages_more(self):
        # если кнопки More – это ссылки/кнопки внутри карточки
        return browser.all(".team-card a").by(have.exact_text("More"))
