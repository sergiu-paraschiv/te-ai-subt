import os
from distutils.core import setup
from setuptools import find_packages
VERSION = __import__("man").VERSION
CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]
install_requires = [
    'django>=1.4.1',
]
# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
for dirpath, dirnames, filenames in os.walk('man'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "man/" or "man\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
setup(
    name="te-ai-subt",
    description="Rau de tot",
    version=VERSION,
    author="Sergiu",
    author_email="sergiuspk+gh@gmail.com",
    url="https://github.com/sergiu-paraschiv/te-ai-subt",
    download_url="https://github.com/sergiu-paraschiv/te-ai-subt",
    package_dir={'man': 'man'},
    packages=packages,
    package_data={'man': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
