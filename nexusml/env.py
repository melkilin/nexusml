"""
This script defines the names of all required environment variables.
"""
#######
# API #
#######

# Identifiers
ENV_API_CLIENT_ID = 'NEXUSML_API_CLIENT_ID'
ENV_API_DOMAIN = 'NEXUSML_API_DOMAIN'

# Passwords
ENV_API_CLIENT_SECRET = 'NEXUSML_API_CLIENT_SECRET'
ENV_MAIL_PASSWORD = 'NEXUSML_API_MAIL_PASS'

# RSA key for signed data
ENV_RSA_KEY_FILE = 'NEXUSML_API_RSA_KEY_FILE'  # private RSA key file

# Official clients
ENV_WEB_CLIENT_ID = 'NEXUSML_API_WEB_CLIENT_ID'

# JWT Token Configuration
ENV_TOKEN_AUDIENCE = 'NEXUSML_API_TOKEN_AUDIENCE'  # Recipient of the token.
ENV_TOKEN_ISSUER = 'NEXUSML_API_TOKEN_ISSUER'  # Issuer of the token.

# Mail
ENV_MAIL_SERVER = 'NEXUSML_API_MAIL_SERVER'
ENV_MAIL_USERNAME = 'NEXUSML_API_MAIL_USERNAME'
ENV_NOTIFICATION_EMAIL = 'NEXUSML_API_NOTIFICATION_EMAIL'
ENV_WAITLIST_EMAIL = 'NEXUSML_API_WAITLIST_EMAIL'
ENV_SUPPORT_EMAIL = 'NEXUSML_API_SUPPORT_EMAIL'

# Main organization
ENV_MAIN_ORG_TRN = 'NEXUSML_API_MAIN_ORG_TRN'
ENV_MAIN_ORG_NAME = 'NEXUSML_API_MAIN_ORG_NAME'
ENV_MAIN_ORG_DOMAIN = 'NEXUSML_API_MAIN_ORG_DOMAIN'
ENV_MAIN_ORG_ADDRESS = 'NEXUSML_API_MAIN_ORG_ADDRESS'

############
# DATABASE #
############

ENV_DB_NAME = 'NEXUSML_DB_NAME'
ENV_DB_USER = 'NEXUSML_DB_USER'
ENV_DB_PASSWORD = 'NEXUSML_DB_PASS'

######################
# EXTERNAL RESOURCES #
######################

# AWS (see https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration)
ENV_AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'  # Access key for the AWS account
ENV_AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'  # Secret key for the AWS account
ENV_AWS_S3_BUCKET = 'AWS_S3_BUCKET'  # AWS S3 bucket name

# CELERY
ENV_CELERY_BROKER_URL = 'NEXUSML_CELERY_BROKER_URL'
ENV_CELERY_RESULT_BACKEND = 'NEXUSML_CELERY_RESULT_BACKEND'

# REDIS
ENV_REDIS_PASS = 'NEXUSML_REDIS_PASS'

# AUTH0
ENV_AUTH0_DOMAIN = 'NEXUSML_AUTH0_DOMAIN'  # Domain to the Auth0 tenant
ENV_AUTH0_CLIENT_ID = 'NEXUSML_AUTH0_CLIENT_ID'  # Auth0 client management ID
ENV_AUTH0_CLIENT_SECRET = 'NEXUSML_AUTH0_CLIENT_SECRET'  # Auth0 client management secret
ENV_AUTH0_JWKS = 'NEXUSML_AUTH0_JWKS'  # Url to the token verification key sets
ENV_AUTH0_SIGN_UP_REDIRECT_URL = 'NEXUSML_AUTH0_SIGN_UP_REDIRECT_URL'  # Redirect URL after password change
