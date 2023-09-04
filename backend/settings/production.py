from .base import *



INSTALLED_APPS += [
     
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
     'default':dj_database_url.config(
          default=env('DATABASE_URL'),
          conn_max_age=600
     )
}

# Following settings only make sense on production and may break development environments.
if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'plugins/assets')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'