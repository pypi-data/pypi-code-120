from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='qt-sass-theme-getter',
    version='0.0.13',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'qt_sass_theme_getter.sass': ['theme.scss',
                                               'icon_button.scss',
                                               'icon_text_button.scss',
                                               'menu_bar.scss',
                                               'main_widget.scss'],
                  'qt_sass_theme_getter.var': ['variables.scss']
                  },
    description='Qt sass theme getter',
    url='https://github.com/yjg30737/qt-sass-theme-getter.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'qtsass'
    ]
)