## SamacharPatra (समाचारपत्र)

A simple newsletter subscription based module with email verification.

<span align="center">
<img src="media/mainpage.png" width="100%" height="auto">
</span><br>

### Prerequisites

- Python 3.7 or higher (tested in version 3.7.10)

### Tools & Technologies

- Database: SQLite | ORM
- Framework: Django 3.2
- Email & Credentials: SMTP (tested with Google account)

### Run & Setups

- Clone this repository
- [Install & activate virtual environment in the root folder](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
- Install required dependencies by running `pip3 install -r requirements.txt`

- Add these `credentials` inside `main/settings.py`

```bash
EMAIL_HOST_USER = '<paste email address>'
EMAIL_HOST_PASSWORD = '<paste password>'
```

- Run the following command in terminal

```bash
python3 manage.py runserver
```

#### URL Routes

- Main Subscribing page >> [http://localhost:8000/subscribe](http://localhost:8000/subscribe)

### Made with ❤️ in Nepal.
