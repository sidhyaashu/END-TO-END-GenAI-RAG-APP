from setuptools import find_packages, setup

version = '0.0.1'
author = 'Asutosh Sidhya'
mail = 'ashutoshsidhya69@gmail.com'
desc = 'A GenAI project for college use cases'
opt_url = 'https://github.com/sidhyaashu/END-TO-END-GenAI-RAG-APP.git'

setup(
    name='GenAi',  # Use snake_case for package names
    version=version,
    author=author,
    author_email=mail,
    description=desc,
    long_description=open('README.md').read(),  # Make sure to have a README.md file
    long_description_content_type='text/markdown',
    url=opt_url,  # Optional project URL
    packages=find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)