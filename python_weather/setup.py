from setuptools import setup
setup(
  name='python-weather',
  packages=['python_weather'],
  version='0.3.6',
  description='A free Weather API Wrapper.',
  long_description=open('README.md', 'r', encoding='utf-8').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/ronnie8789/MLH',
  download_url='https://github.com/ronnie8789/MLH/archive/0.3.6.tar.gz',
  keywords=['Weather', 'API', 'Weather API', 'API Wrapper', 'Weather CLI', 'CLI'],
  install_requires=[
    'aiohttp>=3.7.4',
    'xmltodict',
    'halo'
  ],
  entry_points={
    'console_scripts': [
      'weather = python_weather.cli:main'
    ]
  },
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
  python_requires='>=3.7',
)
