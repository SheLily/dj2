from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import os


def file_list(request, date: str = None):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    date = datetime.fromisoformat(date) if date else None
    context = {
        'files': [
            dict(
                name=filename,
                ctime=datetime.fromtimestamp(int(os.stat(os.path.join(settings.FILES_PATH, filename)).st_ctime)),
                mtime=datetime.fromtimestamp(int(os.stat(os.path.join(settings.FILES_PATH, filename)).st_mtime)),
            )
            for filename in os.listdir(settings.FILES_PATH)
            if any(
                [
                    not date,
                    date == datetime.fromtimestamp(int(os.stat(os.path.join(settings.FILES_PATH, filename)).st_ctime)),
                    date == datetime.fromtimestamp(int(os.stat(os.path.join(settings.FILES_PATH, filename)).st_mtime)),
                ]
            )

        ],
        # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        'date': date
    }

    template_name = 'index.html'
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(settings.FILES_PATH, name)) as file:
        return render(
            request,
            'file_content.html',
            context={'file_name': 'file_name_1.txt', 'file_content': file.read()}
        )
