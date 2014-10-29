from setuptools import setup

setup(
    name='check_x224',
    version='0.1',
    description='Script to check RDP connection based on x224 exchange.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
    ],
    url='https://github.com/dnozay/check_x224',
    license='BSD',
    author='Troels Arvin',
    author_email='tra@sst.dk',
    scripts=['check_x224.py'],
)
