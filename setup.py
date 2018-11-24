from setuptools import setup


install_requires = [
        'falcon',
        'gunicorn',
        'httpie',
        'msgpack-python',
        ]

tests_requires = [
        'pytest',
        ]

setup(
        name='jadeapi',
        version=0.1,
        install_requires=install_requires,
        tests_requires=tests_requires,
        extras_require={
            'test':tests_requires,
            }
        )
