from glob import glob
from os.path import splitext, basename

from setuptools import setup, find_packages

setup(
	name='weather',
	version='0.0.1',
	description='Honeycomb Weather API',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
	zip_safe=False,
	install_requires=[]
)
