from setuptools import setup, find_packages

setup(
    name='safari-bookmarks-jsonize',
    version='1.0.2',
    keywords=['Safari', 'Bookmarks', 'JSON', 'Monsoir'],
    description='transform Safari bookmarks export to JSON file',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],

    url='https://github.com/Monsoir/safari-bookmarks-jsonizer',
    author='Monsoir',
    author_email='monwingyeung@gmail.com',

    packages=find_packages(),
    include_package_data=False,
    platforms=["any"],
    install_requires=['beautifulsoup4'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'jsonize = jsonizer.jsonize:main',
        ]
    }
)