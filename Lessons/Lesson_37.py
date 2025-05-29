# from jinja2 import Template


# menu = [   
#     {'href': '/index', 'link': 'Главная'},   
#     {'href': '/news', 'link': 'Новости'},    
#     {'href': '/about', 'link': 'О компании'},    
#     {'href': '/shop', 'link': 'Магазин'},    
#     {'href': '/contacts', 'link': 'Контакты'},
#     ]


# link = """
# <ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#             <li><a href="{{ i.href }}" class="active">{{ i.link }}</a></li>
#         {% else %}
#             <li><a href="{{ i.href }}">{{ i.link }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>
# """


# tm = Template(link)
# msg = tm.render(menu=menu)

# print(msg)


# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Volvo', 'price': 44300},
#     {'model': 'VW', 'price': 21300},
# ]

# tpl = "{{ cs | sum(attribute='price') }}"
# tpl = "{{ (cs | max(attribute='price')).model }}" # получаем модель самой дорогой машины также можно использовать min



# html = """
# {% macro set_input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}

# <p>{{ set_input('username') }}</p>
# <p>{{ set_input('email') }}</p>
# <p>{{ set_input('password', '', 'password') }}</p>

# """

# tm = Template(html)
# msg = tm.render()

# print(msg)


from turtle import title
from jinja2 import Environment, FileSystemLoader

persons =[
    {"name": "Алексей"},
    {"name": "Никита"},
    {"name": "Виталий"},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(users=persons, title="About Jinja")

print(msg)