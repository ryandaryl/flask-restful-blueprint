import os
from yaml import load

def before_all(context):
    context.settings = load(open('features/conf.yaml').read())
    context.base_url = '{}:{}'.format(context.settings['host'], context.settings['port'])
    context.headers = {}
    context.verify_ssl = True