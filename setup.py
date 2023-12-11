from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='petersburgedu_wrap',
    version='0.0.1',
    author='zeusina',
    author_email='kachusov_k@outlook.com',
    description='This is module for work with petersburgedu website API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent'
    ],
    keywords='api python petersburgedu',
    project_urls={
        'Documentation': ''
    },
    python_requires='>=3.7',
    install_requires=['requests>=2.25.1'],
)
