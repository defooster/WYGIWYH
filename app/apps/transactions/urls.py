from django.urls import path
import apps.transactions.views as views

urlpatterns = [
    path(
        "transactions/actions/pay",
        views.bulk_pay_transactions,
        name="transactions_bulk_pay",
    ),
    path(
        "transactions/actions/unpay/",
        views.bulk_unpay_transactions,
        name="transactions_bulk_unpay",
    ),
    path(
        "transactions/actions/delete/",
        views.bulk_delete_transactions,
        name="transactions_bulk_delete",
    ),
    path(
        "transaction/<int:transaction_id>/pay",
        views.transaction_pay,
        name="transaction_pay",
    ),
    path(
        "transaction/<int:transaction_id>/delete",
        views.transaction_delete,
        name="transaction_delete",
    ),
    path(
        "transaction/<int:transaction_id>/edit",
        views.transaction_edit,
        name="transaction_edit",
    ),
    path(
        "transaction/add",
        views.transaction_add,
        name="transaction_add",
    ),
    path(
        "transactions/transfer",
        views.transactions_transfer,
        name="transactions_transfer",
    ),
    path("tags/", views.tags_index, name="tags_index"),
    path("tags/list/", views.tags_list, name="tags_list"),
    path("tags/add/", views.tag_add, name="tag_add"),
    path(
        "tags/<int:tag_id>/edit/",
        views.tag_edit,
        name="tag_edit",
    ),
    path(
        "tags/<int:tag_id>/delete/",
        views.tag_delete,
        name="tag_delete",
    ),
    path("categories/", views.categories_index, name="categories_index"),
    path("categories/list/", views.categories_list, name="categories_list"),
    path("categories/add/", views.category_add, name="category_add"),
    path(
        "categories/<int:category_id>/edit/",
        views.category_edit,
        name="category_edit",
    ),
    path(
        "categories/<int:category_id>/delete/",
        views.category_delete,
        name="category_delete",
    ),
    path(
        "installment-plans/",
        views.installment_plans_index,
        name="installment_plans_index",
    ),
    path(
        "installment-plans/list/",
        views.installment_plans_list,
        name="installment_plans_list",
    ),
    path(
        "installment-plans/add/",
        views.installment_plan_add,
        name="installment_plan_add",
    ),
    path(
        "installment-plans/<int:installment_plan_id>/transactions/",
        views.installment_plan_transactions,
        name="installment_plan_transactions",
    ),
    path(
        "installment-plans/<int:installment_plan_id>/edit/",
        views.installment_plan_edit,
        name="installment_plan_edit",
    ),
    path(
        "installment-plans/<int:installment_plan_id>/delete/",
        views.installment_plan_delete,
        name="installment_plan_delete",
    ),
    path(
        "installment-plans/<int:installment_plan_id>/refresh/",
        views.installment_plan_refresh,
        name="installment_plan_refresh",
    ),
]
