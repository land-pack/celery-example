import sys
import json

print 'args-->',sys.argv
cere_param = [i for i in sys.argv if i.startswith('--config')][0]
value_param = cere_param.split('=')[1]
print 'value-->',value_param

db_url = ''
with open(value_param,'r') as fd:
    global db_url
    conf = json.load(fd)
    db_url = conf.get('redis_db',{}).get('db_foo')
print 'db_url-->',db_url

BROKER_URL = db_url
CELERY_RESULT_BACKEND = db_url
