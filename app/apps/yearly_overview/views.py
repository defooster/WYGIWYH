from datetime import date
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum, F, Q, Value, CharField, DecimalField
from django.db.models.functions import TruncMonth, Coalesce
from django.db.models.expressions import Case, When
from django.db.models.functions import Concat

from apps.transactions.models import Transaction


@login_required
def index_by_currency(request):
    now = timezone.localdate(timezone.now())

    return redirect(to="yearly_overview_currency", year=now.year)


@login_required
def index_by_account(request):
    now = timezone.localdate(timezone.now())

    return redirect(to="yearly_overview_account", year=now.year)


@login_required
def yearly_overview_by_currency(request, year: int):
    next_year = year + 1
    previous_year = year - 1

    transactions = Transaction.objects.filter(
        reference_date__year=year, account__is_archived=False
    )

    monthly_data = (
        transactions.annotate(month=TruncMonth("reference_date"))
        .values(
            "month",
            "account__currency__code",
            "account__currency__prefix",
            "account__currency__suffix",
            "account__currency__decimal_places",
        )
        .annotate(
            income_paid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.INCOME, is_paid=True, then=F("amount")
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            expense_paid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.EXPENSE,
                            is_paid=True,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            income_unpaid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.INCOME,
                            is_paid=False,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            expense_unpaid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.EXPENSE,
                            is_paid=False,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
        )
        .annotate(
            balance_unpaid=F("income_unpaid") - F("expense_unpaid"),
            balance_paid=F("income_paid") - F("expense_paid"),
            balance_total=F("income_paid")
            + F("income_unpaid")
            - F("expense_paid")
            - F("expense_unpaid"),
        )
        .order_by("month", "account__currency__code")
    )

    # Create a list of all months in the year
    all_months = [date(year, month, 1) for month in range(1, 13)]

    # Create a dictionary to store the final result
    result = {
        month: {
            "income_paid": [],
            "expense_paid": [],
            "income_unpaid": [],
            "expense_unpaid": [],
            "balance_unpaid": [],
            "balance_paid": [],
            "balance_total": [],
        }
        for month in all_months
    }

    # Fill in the data
    for entry in monthly_data:
        month = entry["month"]
        currency_code = entry["account__currency__code"]
        prefix = entry["account__currency__prefix"]
        suffix = entry["account__currency__suffix"]
        decimal_places = entry["account__currency__decimal_places"]

        for field in [
            "income_paid",
            "expense_paid",
            "income_unpaid",
            "expense_unpaid",
            "balance_unpaid",
            "balance_paid",
            "balance_total",
        ]:
            if entry[field] != 0:
                result[month][field].append(
                    {
                        "code": currency_code,
                        "prefix": prefix,
                        "suffix": suffix,
                        "decimal_places": decimal_places,
                        "amount": entry[field],
                    }
                )

    # Fill in missing months with empty lists
    for month in all_months:
        if not any(result[month].values()):
            result[month] = {
                "income_paid": [],
                "expense_paid": [],
                "income_unpaid": [],
                "expense_unpaid": [],
                "balance_unpaid": [],
                "balance_paid": [],
                "balance_total": [],
            }

    return render(
        request,
        "yearly_overview/pages/overview_by_currency.html",
        context={
            "year": year,
            "next_year": next_year,
            "previous_year": previous_year,
            "totals": result,
        },
    )


@login_required
def yearly_overview_by_account(request, year: int):
    next_year = year + 1
    previous_year = year - 1

    transactions = Transaction.objects.filter(
        reference_date__year=year, account__is_archived=False
    )

    monthly_data = (
        transactions.annotate(month=TruncMonth("reference_date"))
        .values(
            "month",
            "account__id",
            "account__name",
            "account__currency__code",
            "account__currency__prefix",
            "account__currency__suffix",
            "account__currency__decimal_places",
        )
        .annotate(
            income_paid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.INCOME, is_paid=True, then=F("amount")
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            expense_paid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.EXPENSE,
                            is_paid=True,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            income_unpaid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.INCOME,
                            is_paid=False,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
            expense_unpaid=Coalesce(
                Sum(
                    Case(
                        When(
                            type=Transaction.Type.EXPENSE,
                            is_paid=False,
                            then=F("amount"),
                        ),
                        default=Value(Decimal("0")),
                        output_field=DecimalField(),
                    )
                ),
                Value(Decimal("0")),
                output_field=DecimalField(),
            ),
        )
        .annotate(
            balance_unpaid=F("income_unpaid") - F("expense_unpaid"),
            balance_paid=F("income_paid") - F("expense_paid"),
            balance_total=F("income_paid")
            + F("income_unpaid")
            - F("expense_paid")
            - F("expense_unpaid"),
        )
        .order_by("month", "account__name")
    )

    # Create a list of all months in the year
    all_months = [date(year, month, 1) for month in range(1, 13)]

    # Get all accounts that had transactions in this year
    accounts = (
        transactions.values(
            "account__id",
            "account__name",
            "account__group__name",
            "account__currency__code",
            "account__currency__prefix",
            "account__currency__suffix",
            "account__currency__decimal_places",
        )
        .distinct()
        .order_by("account__name")
    )

    # Create a dictionary to store the final result
    result = {
        month: {
            account["account__id"]: {
                "name": account["account__name"],
                "group": account["account__group__name"],
                "currency": {
                    "code": account["account__currency__code"],
                    "prefix": account["account__currency__prefix"],
                    "suffix": account["account__currency__suffix"],
                    "decimal_places": account["account__currency__decimal_places"],
                },
                "income_paid": Decimal("0"),
                "expense_paid": Decimal("0"),
                "income_unpaid": Decimal("0"),
                "expense_unpaid": Decimal("0"),
                "balance_unpaid": Decimal("0"),
                "balance_paid": Decimal("0"),
                "balance_total": Decimal("0"),
            }
            for account in accounts
        }
        for month in all_months
    }

    # Fill in the data
    for entry in monthly_data:
        month = entry["month"]
        account_id = entry["account__id"]

        for field in [
            "income_paid",
            "expense_paid",
            "income_unpaid",
            "expense_unpaid",
            "balance_unpaid",
            "balance_paid",
            "balance_total",
        ]:
            result[month][account_id][field] = entry[field]

    return render(
        request,
        "yearly_overview/pages/overview_by_account.html",
        context={
            "year": year,
            "next_year": next_year,
            "previous_year": previous_year,
            "totals": result,
            "accounts": accounts,
        },
    )
