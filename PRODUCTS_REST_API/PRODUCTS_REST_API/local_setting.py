# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6irsnb-bzm8bgr%)c(fu5)!d4#t+@l89t$njp@)cajxnx&j&on'

# Database
# # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'Test',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "autocommit": True
        },
    }
}
