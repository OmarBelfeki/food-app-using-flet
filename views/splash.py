import flet as ft


class Splash(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.route = "/"
        self.padding = ft.padding.only(top=33, left=0, right=0, bottom=0)
        self.bgcolor = ft.colors.TRANSPARENT
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.decoration = ft.BoxDecoration(
            bgcolor=ft.colors.WHITE,
            image=ft.DecorationImage(
                src="splash.png",
                fit=ft.ImageFit.FILL
            )
        )

        self.controls = [
            ft.Text(
                value="The fastest food\ndelivery service",
                color=ft.colors.BLACK,
                weight=ft.FontWeight.W_700,
                size=34,
                text_align=ft.TextAlign.CENTER,
                font_family="SF PRO",
                style=ft.TextStyle(
                    letter_spacing=-0.3,
                    decoration=ft.TextDecoration.NONE,
                    height=1.194
                )
            ),
            #ft.Divider(height=-5, color=ft.colors.TRANSPARENT),
            ft.Container(
                margin=ft.margin.only(top=-50),
                width=508, height=508,
                image=ft.DecorationImage(src="Saly-1.png"),
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                on_click=lambda e: e.page.go("/signup")
            )
        ]
