import re

from setuptools import find_packages, setup

with open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

with open('git_ignore/__version__.py', 'rt', encoding='utf8') as f:
    VERSION = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='git-ignore',
    version=VERSION,
    url='https://github.com/hanpannet/Git-ignore',
    author='Qiushi Pan',
    author_email='ice.gitshell@gmail.com',
    license='MIT',
    keywords='git gitignore template default',
    description='Git ignore template helper',
    long_description=readme,
    packages=find_packages(),
    package_data={
        'git_ignore': ['template/*.gitignore'],
    },
    # include_package_data=True,
    install_requires=["click >= 6.7"],
    # scripts = ['directory/__main__.py'],
    entry_points={'console_scripts': 'git-ignore = git_ignore:main'},
    test_suite='tests',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=True,
)
