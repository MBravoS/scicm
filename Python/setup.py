import atexit
from setuptools import setup
from setuptools.command.install import install

setup(name='scicm',
		version='0.0.0',
		description='Science Colour Maps is a small package containing several colour maps created using viscm.',
		url='https://github.com/MBravoS/scicm',
		author='Matías A. Bravo Santa Cruz',
		author_email='matias.bravo@icrar.org',
		license='BSD-3-Clause',
		packages=['scicm'],
		package_dir={'scicm': 'src/scicm'},
		include_package_data=True,
		package_data={'src':['styles/*.style']},
		#cmdclass={'install':new_install},
		install_requires=['matplotlib>=3.0.0'],
		zip_safe=False)

