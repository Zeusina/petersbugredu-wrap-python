from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding="utf8") as f:
        return f.read()


setup(
    name='petersburgedu_wrap',
    version='0.0.1',
    author='zeusina',
    author_email='kachusov_k@outlook.com',
    description='This is module for work with petersburgedu website API',
    license = "MIT",
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Zeusina/petersbugredu-wrap-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    keywords='api python petersburgedu',
    project_urls={
        "Source": "https://github.com/Zeusina/petersbugredu-wrap-python",
    },
    python_requires='>=3.8',
    install_requires=['requests>=2.25.1'],
)
