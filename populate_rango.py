import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial', 'url':'http://docs.python.org/3/tutorial/', 'views': 487},
        {'title':'How to Think like a Computer Scientist', 'url':'http://www.greenteapress.com/thinkpython/', 'views': 67},
        {'title':'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/', 'views': 123} 
    ]

    django_pages = [
        {'title':'Official Django Tutorial', 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 8431},
        {'title':'Django Rocks', 'url':'http://www.djangorocks.com/', 'views': 1189998819991197253},
        #imagine theres a 0 infront of above :)
        {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/', 'views': 411} 
        ]

    other_pages = [
        {'title':'Bottle', 'url':'http://bottlepy.org/docs/dev/', 'views': 5},
        {'title':'Flask', 'url':'http://flask.pocoo.org', 'views': 3} 
        ]

    cats = {
        'Python': {
            'pages': python_pages,
            'views': 128,
            'likes': 64
        },

        'Django': {
            'pages': django_pages,
            'views': 64,
            'likes': 32
        },

        'Other Frameworks': {
            'pages': other_pages,
            'views': 32,
            'likes': 16
        }
    }


    # If you want to add more categories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        c.views = cat_data['views']
        c.likes = cat_data['likes']
        c.save()
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])


    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()