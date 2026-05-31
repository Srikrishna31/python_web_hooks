# Application configuration file
###################################
#Secret key that will be used by Flask for securely signing the session cookie
SECRET_KEY = 'SECRET_KEY'
###################################
#Minimum Number of Tasks To Generate
MIN_NBR_TASKS = 1
#Maximum Number of Tasks To Generate
MAX_NBR_TASKS = 100
#Time to wait when producing tasks
WAIT_TIME = 1
#Webhook endpoint Mapping to the listener
WEBHOOK_RECEIVER_URL = 'http://localhost:5001/consumetasks'
####################################
#Map to the REDIS server port
BROKER_URL = 'redis://localhost:6379'
####################################