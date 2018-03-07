ENVIRONMENT = 'development'
# ENVIRONMENT = 'production'


if ENVIRONMENT == 'development':
    SETTINGS_FILE = 'conf.settings.development'
elif ENVIRONMENT == 'production':
    SETTINGS_FILE = 'conf.settings.production'
