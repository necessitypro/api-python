from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.test import APIClient

from authentication.models import Account


def SuperuserClient():
    """return superuser authenticated client"""
    account = Account.objects.create_superuser(
        email="superuser@necessity.pro", password="password"
    )

    client = APIClient()
    client.force_authenticate(account)
    return client


def UserClient():
    """return user authenticated client"""
    modules = ["geography-country"]

    user_group = Group.objects.create(name="user")

    for module in modules:
        mod = module.split("-")
        content_type = ContentType.objects.get(app_label=mod[0], model=mod[1])
        permissions = Permission.objects.filter(content_type=content_type)
        for permission in permissions:
            if permission.codename == f"view_{mod[1]}":
                user_group.permissions.add(permission)

    account = Account.objects.create_user(
        email="info@necessity.pro", password="password"
    )

    account.groups.add(user_group)

    client = APIClient()
    client.force_authenticate(account)
    return client
