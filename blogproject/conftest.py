import pytest
from blog.models import Post
from blog.tests.factories import PostFactory
from courses.tests.factories import CourseFactory, MaterialFactory
from django.contrib.sites.models import Site
from django_dynamic_fixture import G
from users.models import User
from users.tests.factories import UserFactory


@pytest.fixture
def user():
    return User.objects.create_user(
        username="user", password="password", email="user@zmrenwu.com"
    )


@pytest.fixture
def post(user):
    return PostFactory(author=user, body="正文")


@pytest.fixture
def course():
    return CourseFactory(description="**教程**")


@pytest.fixture
def material():
    return MaterialFactory()


@pytest.fixture
def site():
    return Site.objects.get(name="example.com")
