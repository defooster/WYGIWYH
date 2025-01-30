<h1 align="center">
  <br>
  <img alt="WYGIWYH" title="WYGIWYH" src="./.github/img/logo.png" />
  <br>
  WYGIWYH
  <br>
</h1>

<h4 align="center">An opinionated and powerful finance tracker.</h4>

<p align="center">
  <a href="#why-wygiwyh">Why</a> •
  <a href="#key-features">Features</a> •
  <a href="#how-to-use">Usage</a> •
  <a href="#how-it-works">How</a> •
  <a href="#caveats-and-warnings">Caveats and Warnings</a> •
  <a href="#built-with">Built with</a>
</p>

**WYGIWYH** (_What You Get Is What You Have_) is a powerful, principles-first finance tracker designed for people who prefer a no-budget, straightforward approach to managing their money. With features like multi-currency support, customizable transactions, and a built-in dollar-cost averaging tracker, WYGIWYH helps you take control of your finances with simplicity and flexibility.

<img src=".github/img/monthly_view.png" width="18%"></img> <img src=".github/img/yearly.png" width="18%"></img> <img src=".github/img/networth.png" width="18%"></img> <img src=".github/img/calendar.png" width="18%"></img> <img src=".github/img/all_transactions.png" width="18%"></img> 

# Why WYGIWYH?
Managing money can feel unnecessarily complex, but it doesn’t have to be. WYGIWYH (pronounced "wiggy-wih") is based on a simple principle:

> Use what you earn this month for this month. Any savings are tracked but treated as untouchable for future months.

By sticking to this straightforward approach, you avoid dipping into your savings while still keeping tabs on where your money goes.

While this philosophy is simple, finding tools to make it work wasn’t. I initially used a spreadsheet, which served me well for years—until it became unwieldy as I started managing multiple currencies, accounts, and investments. I tried various financial management apps, but none met my key requirements:

1. **Multi-currency support** to track income and expenses in different currencies.
2. **Not a budgeting app** — as I dislike budgeting constraints.
3. **Web app usability** (ideally with mobile support, though optional).
4. **Automation-ready API** to integrate with other tools and services.
5. **Custom transaction rules** for credit card billing cycles or similar quirks.

Frustrated by the lack of comprehensive options, I set out to build **WYGIWYH** — an opinionated yet powerful tool that I believe will resonate with like-minded users.

# Key Features

**WYGIWYH** offers an array of features designed to simplify and streamline your personal finance tracking:

* **Unified transaction tracking**: Record all your income and expenses, organized in one place.
* **Multiple accounts support**: Keep track of where your money and assets are stored (banks, wallets, investments, etc.).
* **Out-of-the-box multi-currency support**: Dynamically manage transactions and balances in different currencies.
* **Custom currencies**: Create your own currencies for crypto, rewards points, or any other models.
* **Automated adjustments with rules**: Automatically modify transactions using customizable rules.
* **Built-in Dollar-Cost Average (DCA) tracker**: Essential for tracking recurring investments, especially for crypto and stocks.
* **API support for automation**: Seamlessly integrate with existing services to synchronize transactions.

# How To Use

To run this application, you'll need [Docker](https://docs.docker.com/engine/install/) with [docker-compose](https://docs.docker.com/compose/install/).

From your command line:

```bash
# Create a folder for WYGIWYH (optional)
$ mkdir WYGIWYH

# Go into the folder
$ cd WYGIWYH

$ touch docker-compose.yml
$ nano docker-compose.yml
# Paste the contents of https://github.com/eitchtee/WYGIWYH/blob/main/docker-compose.prod.yml and edit according to your needs

# Fill the .env file with your configurations
$ touch .env
$ nano .env # or any other editor you want to use
# Paste the contents of https://github.com/eitchtee/WYGIWYH/blob/main/.env.example and edit accordingly

# Run the app
$ docker compose up -d

# Create the first admin account
$ docker compose exec -it web python manage.py createsuperuser
```

## Running locally

If you want to run WYGIWYH locally, on your env file:

1. Remove `URL`
2. Set `HTTPS_ENABLED` to `false`
3. Leave the default `DJANGO_ALLOWED_HOSTS` (localhost 127.0.0.1 [::1])

You can now access localhost:OUTBOUND_PORT

> [!NOTE]
> - If you're planning on running this behind Tailscale or other similar service also add your machine given IP to `DJANGO_ALLOWED_HOSTS`
> - If you're going to use another IP that isn't localhost, add it to `DJANGO_ALLOWED_HOSTS`, without `http://`


## Building from source
Features are only added to main when ready, if you want to run the latest version, you must build from source.

All the required Dockerfiles are [here](https://github.com/eitchtee/WYGIWYH/tree/main/docker/prod).

## Unraid

[nwithan8](https://github.com/nwithan8) has kindly provided a Unraid template for WYGIWYH, have a look at the [unraid_templates](https://github.com/nwithan8/unraid_templates) repo.

WYGIWYH is available on the Unraid Store. You'll need to provision your own postgres (version 15 or up) database.

## Enviroment Variables

| variable                      | type        | default                           | explanation                                                                                                                                                                                                                              |
|-------------------------------|-------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DJANGO_ALLOWED_HOSTS          | string      | localhost 127.0.0.1               | A list of space separated domains and IPs representing the host/domain names that WYGIWYH site can serve. [Click here](https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts) for more details                               |
| HTTPS_ENABLED                 | true\|false | false                             | Whether to use secure cookies. If this is set to true, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection                                                     |
|              URL              | string      | http://localhost http://127.0.0.1 | A list of space separated domains and IPs (with the protocol) representing the trusted origins for unsafe requests (e.g. POST). [Click here](https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-trusted-origins ) for more details |
| SECRET_KEY                    | string      | ""                                | This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.                                                                                                                                       |
| DEBUG                         | true\|false | false                             | Turns DEBUG mode on or off, this is useful to gather more data about possible errors you're having. Don't use in production.                                                                                                             |
| SQL_DATABASE                  | string      | None *required                    | The name of your postgres database                                                                                                                                                                                                       |
| SQL_USER                      | string      | user                              | The username used to connect to your postgres database                                                                                                                                                                                   |
| SQL_PASSWORD                  | string      | password                          | The password used to connect to your postgres database                                                                                                                                                                                   |
| SQL_HOST                      | string      | localhost                         | The adress used to connect to your postgres database                                                                                                                                                                                     |
| SQL_PORT                      | string      | 5432                              | The port used to connect to your postgres database                                                                                                                                                                                       |
| SESSION_EXPIRY_TIME           | int         | 2678400 (31 days)                 | The age of session cookies, in seconds. E.g. how long you will stay logged in                                                                                                                                                            |
| ENABLE_SOFT_DELETE            | true\|false | false                             | Whether to enable transactions soft delete, if enabled, deleted transactions will remain in the database. Useful for imports and avoiding duplicate entries.                                                                             |
| KEEP_DELETED_TRANSACTIONS_FOR | int         | 365                               | Time in days to keep soft deleted transactions for. If 0, will keep all transactions indefinitely. Only works if ENABLE_SOFT_DELETE is true.                                                                                             |
| TASK_WORKERS                  | int         | 1                                 | How many workers to have for async tasks. One should be enough for most use cases                                                                                                                                                        |

# How it works

Check out our [Wiki](https://github.com/eitchtee/WYGIWYH/wiki) for more information.

# Caveats and Warnings

- I'm not an accountant, some terms and even calculations might be wrong. Make sure to open an issue if you see anything that could be improved.
- Pretty much all calculations are done at run time, this can lead to some performance degradation. On my personal instance, I have 3000+ transactions over 4+ years and 4000+ exchange rates, and load times average at around 500ms for each page, not bad overall.
- This isn't a budgeting or double-entry-accounting application, if you need those features there's a lot of options out there, if you really need them in WYGIWYH, open a discussion.

# Built with

WYGIWYH is possible thanks to a lot of amazing open source tools, to name a few:

* Django
* HTMX
* _hyperscript
* Procrastinate
* Bootstrap
* Tailwind
* Webpack
* PostgreSQL
* Django REST framework
* Alpine.js
