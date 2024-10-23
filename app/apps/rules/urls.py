from django.urls import path
import apps.rules.views as views

urlpatterns = [
    path(
        "rules/",
        views.rules_index,
        name="rules_index",
    ),
    path(
        "rules/list/",
        views.rules_list,
        name="rules_list",
    ),
    path(
        "rules/transaction/<int:transaction_rule_id>/view/",
        views.transaction_rule_view,
        name="transaction_rule_view",
    ),
    path(
        "rules/transaction/add/",
        views.transaction_rule_add,
        name="transaction_rule_add",
    ),
    path(
        "rules/transaction/<int:transaction_rule_id>/edit/",
        views.transaction_rule_edit,
        name="transaction_rule_edit",
    ),
    path(
        "rules/transaction/<int:transaction_rule_id>/toggle-active/",
        views.transaction_rule_toggle_activity,
        name="transaction_rule_toggle_activity",
    ),
    path(
        "rules/transaction/<int:transaction_rule_id>/delete/",
        views.transaction_rule_delete,
        name="transaction_rule_delete",
    ),
    path(
        "rules/transaction/<int:transaction_rule_id>/action/add/",
        views.transaction_rule_action_add,
        name="transaction_rule_action_add",
    ),
    path(
        "rules/transaction/action/<int:transaction_rule_action_id>/edit/",
        views.transaction_rule_action_edit,
        name="transaction_rule_action_edit",
    ),
    path(
        "rules/transaction/action/<int:transaction_rule_action_id>/delete/",
        views.transaction_rule_action_delete,
        name="transaction_rule_action_delete",
    ),
    # path(
    #     "rules/<int:installment_plan_id>/transactions/",
    #     views.installment_plan_transactions,
    #     name="rule_view",
    # ),
    # path(
    #     "rules/<int:installment_plan_id>/edit/",
    #     views.installment_plan_edit,
    #     name="rule_edit",
    # ),
    # path(
    #     "rules/<int:installment_plan_id>/delete/",
    #     views.installment_plan_delete,
    #     name="rule_delete",
    # ),
]
