from typing import Any, Sequence

from factory import Faker, post_generation
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = User
        django_get_or_create = ("username",)
