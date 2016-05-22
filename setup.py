from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funniest',
      version='0.1',
      description='Used in conjunction with MPB to design photonic crystal \
      nanobeam cavities',
      long_description='This python library is designed to be used in \
      conjunction with MPB (MIT photonic band solver: \
      http://ab-initio.mit.edu/wiki/index.php/MIT_Photonic_Bands) to \
      automate the design of a photonic nanobeam crystal cavity. It \
      allows for parameter space exploration of the geometric properties\
      of a unit cell, to design for a particular mode at a target frequency.\
      It will find then look for the optimal bandgap inside the parameter \
      space. It can also be used to simulate the full bandstructure.',
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Physics',
      ],
      keywords='MPB photonic crystal nanobeam cavity',
      url='http://github.com/tsmahony/pcnc',
      author='Tom Mahony',
      author_email='tsmahony@gmail.com',
      license='MIT',
      packages=['pcnc'],
      install_requires=[
          'subprocess, numpy, math, pickle, time, os',
      ],
      include_package_data=True,
      zip_safe=False)
      