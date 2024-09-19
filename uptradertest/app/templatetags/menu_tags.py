from django import template
from django.db.models import Q
from app.models import Menu
from django.utils.safestring import mark_safe


register = template.Library()

@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    
    def format_menu(values):
        output = []
        for i in values:
            
            if not i.children:
                output.append(f'<li><a href = "{i.url}">{i.obj.title}</a></li>')
            else:
                if i.is_open:
                    output.append(f'<li><a href = "{i.url}">{i.obj.title}</a></li><ul>{format_menu(i.children)}</ul>')
                else:
                    output.append(f'<li><a href = "{i.url}">{i.obj.title}</a></li>')
        
        return " ".join(output)

    def open_parents(obj):
        if obj.obj.parent_id:
            obj.is_open = True
            open_parents(menu_hash_map[obj.obj.parent_id])


    class MenuObjects:
        def __init__(self, obj):
            self.obj = obj
            self.url = self.obj.get_absolute_url()  
            self.children = []
            self.is_open = True if not obj.parent_id else False


    current_url = context['request'].path
    menu_hash_map = {i.pk: MenuObjects(i) for i in Menu.objects.all()}
    obj_with_current_url = None

    for i in menu_hash_map.values():
        if i.obj.parent_id:
            menu_hash_map[i.obj.parent_id].children.append(i)
        if i.url == current_url:
            obj_with_current_url = i

    if obj_with_current_url:
        open_parents(obj_with_current_url)

    output = f'<ul>{format_menu([i for i in menu_hash_map.values() if not i.obj.parent_id])}</ul>'

    return {'menu': mark_safe(output)}




