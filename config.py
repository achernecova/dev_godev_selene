import os

# Определяем текущее окружение
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
BASE_URL = (
    os.getenv("MAIN_PAGE", "https://dev.godev.agency/")
    if ENVIRONMENT == "development"
    else os.getenv("PROD_PAGE", "https://godev.agency/")
)


class PageConfig:

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.pages = {
            "base_page": {
                "name": "base_page",
                "title": "Web Development Company in USA | Web Design, App & Web Development Services – Godev",
                "description": "Godev is a leading web development company in the USA. "
                "We specialize in custom web design, web applications, app and web development services",
                "url_page": self.base_url,
            },
            "services_page": {
                "name": "services_page",
                "title": "IT services for you and your business",
                "description": "In godev studio you can order the creation of a website, "
                "portal or application of any complexity. We use a wide technology stack",
                "url_page": self.base_url + "services/",
            },
            "outstaff_page": {
                "name": "outstaff_page",
                "title": "IT staff augmentation company in USA, cost of outsorce tech teams and software developers",
                "description": "IT staff augmentation – hire tech teams and software developers for your "
                "projects with lower cost in USA. Software, databases, websites, applications, "
                "microservices, mobile applications",
                "url_page": self.base_url
                + "services/outstaffing-and-outsourcing-of-it-specialists/",
            },
            "mobile_page": {
                "name": "mobile_page",
                "title": "Mobile App Development Services in USA, Leading Mobile Application "
                "Development Company Godev",
                "description": "Transform your ideas into reality with our mobile app development services. "
                "As a leading mobile app development company, we specialize in custom solutions "
                "for iOS and Android, including cross-platform apps",
                "url_page": self.base_url + "services/mobile-development/",
            },
            "custom_software_dev_page": {
                "name": "custom_software_dev_page",
                "title": "Software Development Services in USA, Company for Custom Software Development",
                "description": "Discover top-notch custom software development services in the USA. "
                "Our professional team Godev provides scalable software solutions tailored to your "
                "business needs",
                "url_page": self.base_url + "services/software-development/",
            },
            "python_page": {
                "name": "python_page",
                "title": "Hire Top Python Developer: Find Your Python Programmer with Godev",
                "description": "Hire top Python developer in Godev and scale your development team! "
                "Find your dedicated Python programmer for expert coding and scalable "
                "solutions now.",
                "url_page": self.base_url + "services/python/",
            },
            "c_sharp_page": {
                "name": "c_sharp",
                "title": "Hire C# Developers in the USA, C Sharp Programmers in Godev",
                "description": "Hire C# developers in the USA. Find top C# programmers for high-quality development. "
                "Collaborate with skilled C Sharp developers in your time zone.",
                "url_page": self.base_url + "services/c-sharp/",
            },
            "java_page": {
                "name": "java",
                "title": "Java Software Development Services, Hire Our Expert Company | Godev",
                "description": "Unlock your project's potential with Godev's custom Java software development "
                "services. Hire our expert team to build robust applications tailored to your needs!",
                "url_page": self.base_url + "services/java-development-services/",
            },
            "unity_page": {
                "name": "unity",
                "title": "Hire Developers: Unity Development Company in USA",
                "description": "Hire top Unity developers from our USA-based Unity development company Godev. "
                "Find the best Unity engineer for your project. Hire remote Unity developers now ",
                "url_page": self.base_url + "services/unity/",
            },
            "golang_page": {
                "name": "golang",
                "title": "Hire Golang Developers: Go Development Company in USA",
                "description": "Hire top Golang developers from our USA-based Go development company Godev. "
                "Find the best Golang engineer for your project. Hire remote Golang developers now",
                "url_page": self.base_url + "services/golang/",
            },
            "website_dev_page": {
                "name": "website_dev_page",
                "title": "Website Development Company in USA, Leading Web Design and Development Services Godev",
                "description": "Discover Godev, a leading web development company in the USA, offering top-notch "
                "web design and development services to elevate your online business. "
                "Professional web developers with 10+ years of experience.",
                "url_page": self.base_url + "services/website-development/",
            },
            "e_com_page": {
                "name": "e_com_page",
                "title": "Ecommerce Website Development Company in USA: Expert Web Design & Solutions",
                "description": "Transform your online business with our ecommerce website development company "
                "in the USA. Godev offer expert web design and solutions for high-converting sites",
                "url_page": self.base_url + "services/website-development/e-commerce/",
            },
            "cms_page": {
                "name": "cms_page",
                "title": "Custom CMS Development Services in USA: Company for Your Website Needs",
                "description": "Unlock your website's potential with our custom CMS development services in "
                "the USA. Tailored solutions to meet your business needs, "
                "backed by years of Godev's experience",
                "url_page": self.base_url + "services/website-development/cms/",
            },
            "landing_page": {
                "name": "landing_page",
                "title": "Mastering Landing Page Design in USA, Top Development Services in Godev",
                "description": "Unlock the secrets to effective landing page design in the USA with Godev's top "
                "development services. Generate more leads and enhance conversions today!",
                "url_page": self.base_url + "services/development-of-a-landing-page/",
            },
            "framework_page": {
                "name": "framework_page",
                "title": "Web Development on Frameworks in the USA: website development in Godev",
                "description": "Explore top web development frameworks in the USA with Godev. Save time and "
                "enhance coding efficiency for your projects by leveraging "
                "powerful software infrastructure!",
                "url_page": self.base_url + "services/website-development/framework/",
            },
            "b2b_page": {
                "name": "b2b_page",
                "title": "B2B Ecommerce Website Development Services in USA: Design Strategies for "
                "Success with Godev",
                "description": "Transform your B2B ecommerce website with Godev's expert design strategies. "
                "Our web development services create high-converting platforms for success",
                "url_page": self.base_url + "services/website-development/b2b/",
            },
            "d2c_page": {
                "name": "d2c_page",
                "title": "D2C Ecommerce Web Development in USA | direct to consumer website from Godev",
                "description": "Transform your brand with Godev's D2C eCommerce web development in the USA. "
                "Sell directly to consumers, enhance your online presence, and boost "
                "your ecommerce strategy today!",
                "url_page": self.base_url + "services/website-development/d2c/",
            },
            "web_development_page": {
                "name": "web_development_page",
                "title": "Web Development Services in USA, Custom Website and "
                "Web App Development Solutions | Godev",
                "description": "Looking for expert web development services in the USA? Godev offers high-quality, "
                "custom website development and responsive web design solutions tailored "
                "to your needs.",
                "url_page": self.base_url + "services/web-development/",
            },
            "saas_page": {
                "name": "saas_page",
                "title": "SaaS Development Services in USA: Hire Expert Developers for Application Development "
                "in Godev",
                "description": "Unlock your business potential with our SaaS development services in the USA. "
                "Hire expert developers to create scalable, user-friendly applications "
                "tailored for your clients",
                "url_page": self.base_url + "services/saas/",
            },
            "website_design_page": {
                "name": "website_design_page",
                "title": "Leading Web Design & Development Company in USA | Digital Marketing Agency Godev",
                "description": "Godev is a leading web design and development company offering expert website "
                "design and development services in USA. Elevate your brand with our digital "
                "marketing agency",
                "url_page": self.base_url
                + "services/website-design-and-development-services/",
            },
            "tech_support_page": {
                "name": "tech_support_page",
                "title": "IT maintenance and support services in USA",
                "description": "Discover top-notch IT maintenance and support services in the USA, "
                "ensuring your software and applications run smoothly with timely updates "
                "and expert assistance Godev",
                "url_page": self.base_url + "services/tech-support/",
            },
            "wordpress_page": {
                "name": "wordpress_page",
                "title": "WordPress Website Development & Designe Services in USA | Development Agency Godev",
                "description": "Godev is a leading WordPress website design and development agency in the USA, "
                "offering tailored WordPress development services to elevate your brand online",
                "url_page": self.base_url + "services/wordpress/",
            },
            "joomla_page": {
                "name": "joomla_page",
                "title": "Joomla Development Company in USA | Joomla Web Development Services & CMS Solutions "
                "from Godev",
                "description": "Godev is a leading Joomla development company in the USA, providing top-notch "
                "Joomla web development services. Design & Development agency with 19+ years "
                "of experience!",
                "url_page": self.base_url + "services/joomla/",
            },
            "opencart_page": {
                "name": "opencart_page",
                "title": "OpenCart Development Services Company for eCommerce, hire OpenCart developers in USA",
                "description": "Elevate your online store with our leading OpenCart development company in the "
                "USA. Hire expert OpenCart developers for eCommerce solutions and "
                "mobile apps in Godev",
                "url_page": self.base_url + "services/opencart/",
            },
            "reactjs_page": {
                "name": "reactjs_page",
                "title": "Top ReactJS Development Services Company Godev | Hire Expert React Developers",
                "description": "Unlock the potential of your project with Godev, a top ReactJS development company."
                " Hire expert React developers for scalable web and mobile app solutions today!",
                "url_page": self.base_url + "services/web-development/reactjs/",
            },
            "laravel_page": {
                "name": "laravel_page",
                "title": "Premier Laravel Development Company Godev | Expert Laravel Services",
                "description": "Discover Godev, a premier Laravel development company offering custom "
                "Laravel development services. Hire expert developers to elevate your web "
                "app projects today! ",
                "url_page": self.base_url + "services/laravel-development-company/",
            },
            "symfony_page": {
                "name": "symfony_page",
                "title": "Hire Expert Symfony Developers | Leading Symfony Development Company Godev",
                "description": "Hire expert Symfony developers at Godev for scalable web applications. "
                "Our Symfony development services ensure efficient and secure solutions "
                "tailored to your needs.",
                "url_page": self.base_url + "services/symfony/",
            },
            "codeigniter_page": {
                "name": "codeigniter_page",
                "title": "CodeIgniter Development Company Godev | Expert CodeIgniter Development Services",
                "description": "Elevate your web projects with Godev, a leading CodeIgniter development company. "
                "Hire expert CodeIgniter developers for top-notch development services today!",
                "url_page": self.base_url
                + "services/website-development/framework/codeigniter/",
            },
            "project_page": {
                "name": "project_page",
                "title": "Web Development and Designs Portfolio - Godev",
                "description": "Godev's portfolio consist of completed projects in Design and Web Development. "
                "We help clients grow and prosper for over 10 years",
                "url_page": self.base_url + "projects/",
            },
            "reviews_page": {
                "name": "reviews_page",
                "title": "Godev Reviews | Web development in USA",
                "description": "Reviews from our clients about web development with Godev",
                "url_page": self.base_url + "reviews/",
            },
            "contacts_page": {
                "name": "contacts_page",
                "title": "Contact information: godev office address",
                "description": "You can contact the godev agency for development, design, "
                "technical support of websites or applications of any complexity",
                "url_page": self.base_url + "contacts/",
            },
            "about_page": {
                "name": "about_page",
                "title": "Godev Agency - Web Development Company in USA",
                "description": "Discover Godev Agency, a premier web development firm dedicated to delivering "
                "innovative and customized digital solutions. Meet the talented team that helps "
                "businesses succeed online",
                "url_page": self.base_url + "about-us/",
            },
            # "blog_page":
            # {
            #     "name": "blog_page",
            #     "title": "Blog",
            #     "description": "",
            #     "url_page": self.base_url + "blog/"
            # },
            "project_euro_vpn": {
                "name": "project_euro_vpn",
                "title": "Website development for EuroHoster Ltd (design, bootstrap) | Godev",
                "description": "Godev's case: website development for EuroHoster Ltd. Website design, bootstrap",
                "url_page": self.base_url + "projects/information-security-service/",
            },
            "project_find_a_builder": {
                "name": "project_find_a_builder",
                "title": "Website development for construction company from London (front-end development, "
                "programming, Symfony) | Godev",
                "description": "Godev's case: website development for construction company. front-end development, "
                "programming, Symfony",
                "url_page": self.base_url + "projects/find-a-builder/",
            },
            "project_mint_link": {
                "name": "project_mint_link",
                "title": "Website development for Mint Links (PHP,Yii2) | Godev",
                "description": "Godev's case: website development for Mint Links. PHP,Yii2",
                "url_page": self.base_url + "projects/mint-links/",
            },
            "project_sls": {
                "name": "project_sls",
                "title": "MVP for Swift Logistic Solutions (SLS) Serbian logistics company (Symfony, React) | Godev",
                "description": "Godev's case: website development (MVP) for Serbian logistics company. Symfony, React",
                "url_page": self.base_url + "projects/swift-logistic-solutions/",
            },
            "project_vegan_hotel": {
                "name": "project_vegan_hotel",
                "title": "Website development for Vegan Hotel (PHP, JQUERY) | Godev",
                "description": "Godev's case: website development for vegan hotel in the Dolomites. Php, Jquery",
                "url_page": self.base_url + "projects/vegan-hotel/",
            },
            # "project_trading_platform":
            #     {
            #         "name": "project_trading_platform",
            #         "title": "Major National Asset Trading Platform",
            #         "description": "",
            #         "url_page": self.base_url + "projects/major-national-asset-trading-platform/"
            #     },
        }

    def get_page_data(self, page_name: str) -> dict:
        """Возвращает данные страницы по ее имени."""
        if page_name in self.pages:
            return self.pages[page_name]
        else:
            raise ValueError(f"Страница '{page_name}' не найдена в PageConfig.")


config = PageConfig()
