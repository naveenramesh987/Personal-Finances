from flet import *
from pages.home import Home
from pages.forgotpassword import ForgotPassword
from pages.dashboard import Dashboard
from pages.login import Login
from pages.signup import Signup


class Main(UserControl):
    def __init__(
        self,
        page: Page,
    ):
        super().__init__()
        self.page = page

    def init_helper(
        self,
    ):
        self.page.on_route_change = self.on_route_change

    def on_route_change(self, route):
        new_page = {
            "/": Home,
            "/login": Login,
            "/signup": Signup,
            "/me": Dashboard,
            "/forgotpassword": ForgotPassword,
        }
        self.page.views.clear()
        self.page.views.append()


app(target=Main, assets_dir="assets", view=WEB_BROWSER)
