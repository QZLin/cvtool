from setuptools import setup

setup(
    name='cvtool',
    version='0.1',
    packages=['cvtool', 'pathless_asset'],
    package_data={'': ['LICENSE']},
    install_requires=['opencv-python', 'numpy'],
    url='https://github.com/QZLin/cvtool',
    author='Q.Z.Lin',
    author_email='qzlin01@163.com',
    description='',
    classifiers=['License :: OSI Approved :: GNU General Public License v3 (GPLv3)']
)
