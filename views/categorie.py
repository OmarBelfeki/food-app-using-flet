import flet as ft


class Cate(ft.View):
    def __init__(self, page: ft.Page) -> None:
        self.__width = page.width
        super().__init__()
        self.route = "/cate"
        self.padding = ft.padding.only(top=33, left=0, right=0, bottom=0)
        self.bgcolor = ft.colors.TRANSPARENT
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER



        self.decoration = ft.BoxDecoration(
            bgcolor=ft.colors.WHITE,
            image=ft.DecorationImage(
                src="categories.png",
                fit=ft.ImageFit.FILL
            )
        )


        self.controls = [
            ft.Container(
                width=self.__width, height=52,
                border_radius=ft.border_radius.all(value=20),
                border=ft.border.all(width=1, color="#C8C6C6"),
                margin=ft.margin.only(left=15, right=15),
                bgcolor="#C6BEDE",
                content=ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.SEARCH, color="#6B6969", size=25),
                        ft.TextField(
                            width=self.__width - 120,
                            hint_text="Search",
                            hint_style=ft.TextStyle(color="#6B6969"),
                            border=ft.InputBorder.NONE,
                            on_change=self.__changed
                        ),
                        ft.Icon(name=ft.icons.MIC, color="#6B6969", size=25),
                    ]
                )
            ),
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            ft.Container(
                alignment=ft.alignment.center_left,
                padding=ft.padding.only(left=15),
                content=ft.Text(
                    value="Categories",
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.W_700,
                    size=34,
                    text_align=ft.TextAlign.CENTER,
                    font_family="SF PRO",
                    style=ft.TextStyle(
                        letter_spacing=0.3,
                        decoration=ft.TextDecoration.NONE,
                        height=1.194
                    )
                ),
                on_click=lambda e: e.page.go("/")
            ),
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Row(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="Pasta.png",
                                data="pasta",
                                width=150, height=150
                            ),
                            ft.Image(
                                src="Healthy.png",
                                data="healthy",
                                width=150, height=150

                            )
                        ]
                    ),
                    ft.Row(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="Hamnurger.png",
                                data="hamburger",
                                width=150, height=150
                            ),
                            ft.Image(
                                src="Meat.png",
                                data="meat",
                                width=150, height=150
                            )
                        ]
                    ),
                    ft.Row(
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="Rectangle-154.png",
                                data="dessert",
                                width=150, height=150
                            ),
                            ft.Image(
                                src="Ramen.png",
                                data="pasta",
                                width=150, height=150
                            )
                        ]
                    )
                ]
            )

        ]

    @staticmethod
    def __changed(e: ft.ControlEvent) -> None:
        pass