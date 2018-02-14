import os
from yaml import load

def before_all(context):
    context.settings = load(open('features/conf.yaml').read())
    context.port = os.environ.get('PORT', 5000)
    context.base_url = '{}:{}'.format(context.settings['base_url'], context.port)
    context.headers = {}
    context.verify_ssl = True