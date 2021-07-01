# coding: utf-8

from cx_Freeze import setup, Executable

# Параметры исполняемого файла

"""
class Executable(object):
    def __init__(self, script, initScript = None, base = None,
                 targetName = None, icon = None, shortcutName = None,
                 shortcutDir = None, copyright = None, trademarks = None):
"""

executables = [Executable('main.py',
                          targetName='my_app.exe',
                          # Для GUI по умолчанию console (т.ж. "Win32GUI" и "Win32Service")
                          base='Win32GUI',
                          icon='example.ico')]

# Исключить следующие модули
excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
            'unicodedata', 'bz2', 'select']

# Добавить модули
includes = ['time', 'os', 'subprocess']

# Какие модули нужно поместить в архив
zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']

# Добавление файлов в сборку
include_files = ['data']

# Особенности сборки для разных операционных систем и типов сборки
options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        # Имя папки куда будет помещена сборка
        'build_exe': 'my_app_dir',
        'include_files': include_files,
    }
}

# Параметры описывающие сборку
setup(name='my_app',
      version='0.1',
      description='My App!',
      executables=executables,
      options=options)
