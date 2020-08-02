from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()
setup(
    name='weather_py',
    version='0.1',
    install_requires=required,
    description='Package for Weather Forecasting with API Call',
    url='git@github.com:AnkitAnand2/weatherpackage2.git',
    author='Ankit_Anand',
    author_email='ankitanand5024@gmail.com',
    license='unlicense',
    packages=['weather_py'],
    zip_safe=False
)