class UrlHelper:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    LOGIN_URL = BASE_URL + "login"
    FEED_URL = BASE_URL + "feed"
    PROFILE_URL = BASE_URL + "account/profile"
    
    @classmethod
    def get_url(cls, page_name):
        urls = {
            "main": cls.BASE_URL,
            "login": cls.LOGIN_URL,
            "feed": cls.FEED_URL,
            "profile": cls.PROFILE_URL
        }
        return urls.get(page_name, cls.BASE_URL)