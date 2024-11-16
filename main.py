from views.splash import Splash
from views.signup import Signup
from views.categorie import Cate


import flet as ft


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = page.width
    page.window.height = page.height
    page.title = "Food App"
    #page.bgcolor = ft.colors.WHITE
    #page.window.expand = True
    page.padding = 0

    page.fonts = {
        "SF PRO": "/fonts/SFPRODISPLAYBOLD.OTF"
    }

    def router(_) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(Splash(page=page))
            case "/signup":
                page.views.append(Signup(page=page))
            case "/cate":
                page.views.append(Cate(page=page))
        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets")
