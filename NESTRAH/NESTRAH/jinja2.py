from jinja2 import Environment, FileSystemLoader
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from pathlib import Path

def environment(**options):
    # Указываем путь к папке с шаблонами
    template_dir = Path(__file__).resolve().parent.parent / 'templates'
    env = Environment(
        loader=FileSystemLoader(template_dir),
        extensions=[
            'jinja2.ext.loopcontrols',
            'jinja2.ext.do',
            'jinja2.ext.i18n',
            
        ],
        autoescape=True,
        auto_reload=options.get('auto_reload', False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env