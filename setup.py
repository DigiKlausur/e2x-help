import os
from setuptools import setup, find_packages

# get paths to all static files and templates
static_files = []
for (dirname, dirnames, filenames) in os.walk('e2xhelp/server_extensions/help/static'):
    root = os.path.relpath(dirname, 'e2xhelp/server_extensions/help')
    for filename in filenames:
        static_files.append(os.path.join(root, filename))


name = u'e2xhelp'

setup_args = dict(
    name=name,
    version='0.0.1',
    author='Tim Metzler',
    author_email='tim.metzler@h-brs.de',
    license='MIT',
    packages=find_packages(),
    package_data= {
        'e2xhelp.server_extensions.help': static_files
    },
    install_requires=[
        'jupyter',
        'notebook',
        'tornado'
    ],
)

if __name__ == '__main__':
    setup(**setup_args)