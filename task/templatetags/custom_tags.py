from django.template import Library

register = Library()

@register.inclusion_tag('task/menu.html')
def show_menu(menu, category_id):
    return {
        'menu': menu,
        'category_id': category_id,
        'categories': menu.category_set.all()
    }

