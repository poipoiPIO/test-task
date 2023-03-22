from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader 

from .models import Menu

def index(req):
    first_menu = Menu.objects.all()[0]
    first_category_id = first_menu.category_set.all()[0].id

    return redirect(
        'category',
        menu_name=first_menu.title,
        category_id=first_category_id
    )

def category(req, menu_name, category_id):
    menu = Menu.objects.all()
    template = loader.get_template('task/index.html') 
    ctx = {
        'menu': menu,
        'menu_name': menu_name,
        'category_id': category_id
    }

    return HttpResponse(template.render(ctx, req))
