from setuptools import setup
import os
_here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_here, 'README.md')) as f:
    pass

requires = ['pyclipper>=1.1.0',
            'numpy>=1.14',
            'pandas>=0.22.0',
            'matplotlib>=2.1.0',
            'scipy>=1.0.0',
            'pytest']

setup(name='multiflexxlib',
      version='0.2.11',
      description='Tools library for CAMEA neutron detector MultiFLEXX',
      long_description='See github page',
      url='http://github.com/sq-meng/multiflexxlib',
      author='Siqin Meng',
      author_email='mengsq04@gmail.com',
      license='',
      packages=['multiflexxlib'],
      install_requires=requires,
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      zip_safe=False,
      include_package_data=True,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Scientific/Engineering :: Visualization',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'],

      )
