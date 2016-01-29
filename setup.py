from setuptools import setup, find_packages

setup(
    name='arrrsync',
    author='Arne Beer',
    author_email='arne@twobeer.de',
    version='0.0.1',
    description='Secure and restricted file copying and exploring with rsync over ssh.',
    keywords='Filetransfer rsync ssh secure restricted',
    url='http://github.com/nukesor/arrrsync',
    license='MIT',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console'
    ],
    packages=find_packages(exclude=["*.egg-info"]),
    entry_points={
        'console_scripts': [
            'arrrsync=client.arrrsync:main',
            'arrrsync-server=server.arrrsync_server:main'
        ]
    })
