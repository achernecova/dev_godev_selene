from pages.b2b_page_selene import B2BPageSelene
from pages.codeigniter_page_selene import CodeigniterPageSelene
from pages.custom_software_dev_page_selene import CustomSoftwarePageSelene
from pages.d2c_page_selene import D2CPageSelene
from pages.e_com_page_selene import EComPageSelene
from pages.framework_page_selene import FrameworkPageSelene
from pages.landing_page_selene import LandingPageSelene
from pages.main_page_selene import MainPageSelene
from pages.mobile_page_selene import MobilePageSelene
from pages.outstaff_page_selene import OutstaffPageSelene
from pages.project_euro_vpn_selene import ProjectEuroVPNSelene
from pages.project_find_a_builder_selene import ProjectFindABuilderSelene
from pages.project_mint_link_selene import ProjectMintLinkSelene
from pages.project_sls_selene import ProjectSLSSelene
from pages.project_trading_platform_selene import ProjectTradingPlatformSelene
from pages.project_vegan_hotel_selene import ProjectVeganHotelSelene
from pages.python_page_selene import PythonPageSelene
from pages.react_page_selene import ReactPageSelene
from pages.saas_page_selene import SAASPageSelene
from pages.services_page_selene import ServicesPageSelene
from pages.support_page_selene import TechSupportPageSelene
from pages.symfony_page_selene import SymfonyPageSelene
from pages.web_development_page_selene import WebDevelopmentPageSelene


def get_page_instance_selene(page_name):
    page_classes = {
        "base_page": MainPageSelene,
        "services_page": ServicesPageSelene,
        "mobile_page": MobilePageSelene,
        "custom_software_dev_page": CustomSoftwarePageSelene,
        "outstaff_page": OutstaffPageSelene,
        "python": PythonPageSelene,
        #
        # "c_sharp_page": JavaPage,
        # "java": JavaPage,
        # "unity_page": JavaPage,
        # "golang_page": JavaPage,
        #
        "web_development_page": WebDevelopmentPageSelene,
        "e_com_page": EComPageSelene,
        # "cms": CMSPage,
        "landing": LandingPageSelene,
        "framework_page": FrameworkPageSelene,
        "b2b_page": B2BPageSelene,
        "d2c": D2CPageSelene,
        "saas": SAASPageSelene,
        "website_design_page": WebDevelopmentPageSelene,
        "tech_support_page": TechSupportPageSelene,
        # "wordpress": WordpressPage,
        # "joomla": JoomlaPage,
        # "opencart": OpencartPage,
        "reactjs": ReactPageSelene,
        # "laravel": LaravelPage,
        "symfony": SymfonyPageSelene,
        "codeigniter": CodeigniterPageSelene,
        # "project_page": ProjectPage,
        # "reviews": ReviewsPage,
        # "contacts": ContactPage,
        # "about": AboutPage,
        # # "blog": BlogPage,
        "project_euro_vpn": ProjectEuroVPNSelene,
        "project_find_a_builder": ProjectFindABuilderSelene,
        "project_mint_link": ProjectMintLinkSelene,
        "project_sls": ProjectSLSSelene,
        "project_vegan_hotel": ProjectVeganHotelSelene,
        "project_trading_platform": ProjectTradingPlatformSelene,
    }
    try:
        return page_classes[page_name]()
    except KeyError:
        raise ValueError(f"Неизвестная страница: {page_name}")
