from setuptools import setup, find_packages

setup(
    name='pyVRageAPI',
    version='0.0.1',
    description='pyVRageAPI is a python library for accessing the VRage Engine Remote Admin API.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author="Derek Vance",
    author_email="DACRepair@gmail.com",
    python_requires=">=3.0.0",
    url="https://github.com/CerberusGaming/pyVRageApi",
    packages=find_packages(),
    install_requires=open('requirements.txt', 'r').readlines(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
