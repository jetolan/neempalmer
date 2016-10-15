from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(name='neempalmer',
      version='0.0.1',
      description=u"Build predictive model from Semantics3 price data",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Jamie Tolan",
      author_email='jamie.tolan@gmail.com',
      url='https://github.com/jetolan/neempalmer',
      license='MIT',
      packages=['semantics_utils'],
      package_dir={'semantics_utils': 'semantics_utils'},
      install_requires=['numpy', 'pandas', 'semantics3']
      )
