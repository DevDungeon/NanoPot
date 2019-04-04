from setuptools import setup


def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data


setup(
    name='nanopot',
    version='1.0.0',
    description='Simple TCP honeypot',
    long_description=readme_file_contents(),
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='MIT',
    packages=['nanopot'],
    zip_safe=False,
    install_requires=[]
)
