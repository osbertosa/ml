import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

_version_ = '0.0.1'

Repo_name = 'ml'
Author_user_name ='osbertosa'
Author_email = 'osbertosasere@yahoo.com'
SRC_REPO = 'ml'


setuptools.setup(
    name= SRC_REPO,
    version=_version_,
    author= Author_user_name,
    author_email= Author_email,
    description= 'A python package for machine learning',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url= f'https;//github.com/{Author_user_name}/{SRC_REPO}',
    project_urls={
        'Bug Tracker': f'https;//github.com/{Author_user_name}/{SRC_REPO}/issues',
    },
    package_dir = {'': 'src'},
    packages=setuptools.find_packages(where='src'),
    
    )

