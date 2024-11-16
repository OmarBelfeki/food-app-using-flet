import flet as ft


class Signup(ft.View):
    def __init__(self, page: ft.Page) -> None:
        self.__width = page.width
        super().__init__()
        self.route = "/signup"
        self.padding = ft.padding.only(top=33, left=0, right=0, bottom=0)
        self.bgcolor = ft.colors.TRANSPARENT
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER



        self.decoration = ft.BoxDecoration(
            bgcolor=ft.colors.WHITE,
            image=ft.DecorationImage(
                src="signup.png",
                fit=ft.ImageFit.FILL
            )
        )

        self.controls = [
            ft.Stack(
                width=self.__width,
                height=250,
                controls=[
                    ft.Text(
                        value="Order food\nto your door",
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.W_700,
                        size=34,
                        text_align=ft.TextAlign.CENTER,
                        font_family="SF PRO",
                        style=ft.TextStyle(
                            letter_spacing=0.3,
                            decoration=ft.TextDecoration.NONE,
                            height=1.194
                        ),
                        left=85
                    ),
                    ft.Image(
                        src="Burger Front.png",
                        error_content=ft.Icon(name=ft.icons.IMAGE),
                        width=75, height=50,
                        top=75, left=10
                    ),
                    ft.Image(
                        src="o_donut.png",
                        error_content=ft.Icon(name=ft.icons.IMAGE),
                        width=121, height=116.75,
                        top=90, left=123

                    ),
                    ft.Image(
                        src="Hot Dog Isometric.png",
                        error_content=ft.Icon(name=ft.icons.IMAGE),
                        width=100, height=100,
                        top=30, left=255
                    ),
                ]
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                width=330, height=346,
                border_radius=ft.border_radius.all(value=20),
                padding=ft.padding.only(left=15, right=15),
                content=ft.Column(
                    controls=[
                        ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                        ft.Text(
                            value="Sign up",
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
                        ft.Divider(height=15, color=ft.colors.TRANSPARENT),
                        ft.TextField(
                            hint_text="Email address",
                            height=42,
                            text_vertical_align=ft.VerticalAlignment.END,
                            hint_style=ft.TextStyle(
                                color="#4A4A4A",
                                size=17,
                                font_family="SF PRO",
                            ),
                            bgcolor="#F5F5F5",
                            border_radius=30,
                        ),
                        ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                        ft.TextField(
                            hint_text="*****",
                            height=42,
                            text_vertical_align=ft.VerticalAlignment.END,
                            hint_style=ft.TextStyle(
                                color="#4A4A4A",
                                size=17,
                                font_family="SF PRO",
                            ),
                            bgcolor="#F5F5F5",
                            border_radius=30,
                        ),
                        ft.Divider(height=8, color=ft.colors.TRANSPARENT),
                        ft.ElevatedButton(
                            bgcolor="#8359E3",
                            width=318, height=42,
                            content=ft.Text(
                                value="Create account",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.W_600,
                                size=17,
                                text_align=ft.TextAlign.CENTER,
                                font_family="SF PRO",
                                style=ft.TextStyle(
                                    letter_spacing=-0.3,
                                    decoration=ft.TextDecoration.NONE,
                                    height=1.194
                                )
                            ),
                            on_click=lambda e: e.page.go("/cate")
                        ),
                        ft.Divider(height=3, color=ft.colors.TRANSPARENT),
                        ft.Divider(height=1, color="#F5F5F5", thickness=3),
                        ft.Row(
                            spacing=-2,
                            controls=[
                                ft.Text(
                                    value="Already have an account? ",
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.W_400,
                                    size=13,
                                    text_align=ft.TextAlign.CENTER,
                                    font_family="SF PRO",
                                    style=ft.TextStyle(
                                        letter_spacing=-0.08,
                                        decoration=ft.TextDecoration.NONE,
                                        height=1.194
                                    )
                                ),
                                ft.TextButton(
                                    style=ft.ButtonStyle(overlay_color=ft.colors.TRANSPARENT),
                                    content=ft.Text(
                                        value="Sign in",
                                        color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_800,
                                        size=13,
                                        text_align=ft.TextAlign.CENTER,
                                        font_family="SF PRO",
                                        style=ft.TextStyle(
                                            letter_spacing=-0.08,
                                            decoration=ft.TextDecoration.NONE,
                                            height=1.194
                                        )
                                    ),
                                    on_click=lambda e: e.page.go("/")
                                )
                            ]
                        )
                    ]
                )
            )
        ]


