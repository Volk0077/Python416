from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('HW/HW_34')
env = Environment(loader=file_loader)

tm = env.get_template('content.html')
msg = tm.render()

print(msg) 

