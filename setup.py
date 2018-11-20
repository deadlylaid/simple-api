from setuptools import setup


install_requires = [
        'falcon',
        'gunicorn',
        'httpie',
        ]

setup(
        name='jadeapi',
        version=0.1,
        install_requires=install_requires,
        )
