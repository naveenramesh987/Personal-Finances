from flet import *
from utils.colors import *
from utils.validation import Validator


class Signup(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.validator = Validator()
        self.bgcolor = blue
        self.error_border = border.all(width=1, color="red")

        self.name_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(size=12, color="#858796"),
                hint_text="Full Name",
                cursor_color="#858796",
                text_style=TextStyle(
                    size=14,
                    color="black",
                ),
            ),
            border=border.all(width=1, color="#bdcbf4"),
            border_radius=30,
        )

        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(size=12, color="#858796"),
                hint_text="Enter email address...",
                cursor_color="#858796",
                text_style=TextStyle(
                    size=14,
                    color="black",
                ),
            ),
            border=border.all(width=1, color="#bdcbf4"),
            border_radius=30,
        )

        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(top=0, bottom=0, right=20, left=20),
                hint_style=TextStyle(size=12, color="#858796"),
                text_style=TextStyle(
                    size=14,
                    color="black",
                ),
                hint_text="Password",
                cursor_color="#858796",
                password=True,
            ),
            border=border.all(width=1, color="#bdcbf4"),
            border_radius=30,
        )

        self.content = Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                Container(
                    width=500,
                    padding=40,
                    bgcolor="white",
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            Text(
                                value="Create an Account!",
                                size=16,
                                color="black",
                                text_align="center",
                            ),
                            Container(height=0),
                            self.name_box,
                            self.email_box,
                            self.password_box,
                            Container(height=10),
                            Container(
                                alignment=alignment.center,
                                bgcolor="#4e73df",
                                height=40,
                                border_radius=30,
                                content=Text(value="Create an Account"),
                                on_click=self.signup,
                            ),
                            Container(
                                content=Text(
                                    value="Forgot Password?", color="#4e73df", size=12
                                ),
                                on_click=lambda _: self.page.go("/forgotpassword"),
                            ),
                            Container(
                                content=Text(
                                    value="Already have an account? Login!",
                                    color="#4e73df",
                                    size=12,
                                ),
                                on_click=lambda _: self.page.go("/login"),
                            ),
                        ],
                    ),
                )
            ],
        )

    def signup(self, e):
        if not self.validator.is_correct_name(self.name_box.content.value):
            self.name_box.border = self.error_border
            self.name_box.update()

        if not self.validator.is_valid_email(self.email_box.content.value):
            self.email_box.border = self.error_border
            self.email_box.update()

        if not self.validator.is_valid_password(self.password_box.content.value):
            self.password_box.border = self.error_border
            self.password_box.update()