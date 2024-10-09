# urls.py
from django.urls import path
from apps.accounts import views

urlpatterns = [
    path(
        "account-reconciliation/",
        views.account_reconciliation,
        name="account_reconciliation",
    ),
    path("accounts/", views.accounts_list, name="accounts_list"),
    path("account/add/", views.account_add, name="account_add"),
    path(
        "account/<int:pk>/edit/",
        views.account_edit,
        name="account_edit",
    ),
    path(
        "account/<int:pk>/delete/",
        views.account_delete,
        name="account_delete",
    ),
    path("account-groups/", views.account_groups_list, name="account_groups_list"),
    path("account-groups/add/", views.account_group_add, name="account_group_add"),
    path(
        "account-groups/<int:pk>/edit/",
        views.account_group_edit,
        name="account_group_edit",
    ),
    path(
        "account-groups/<int:pk>/delete/",
        views.account_group_delete,
        name="account_group_delete",
    ),
]
