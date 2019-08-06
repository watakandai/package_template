from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
	name='package_template',
	version='0.0.1',
	description='Template for creating a Python package',
	long_description=readme,
	author='Kandai Watanabe',
	author_email='kandai.wata@gmail.com',
	url='https://github.com/watakandhi/package_template',
	license=license,
	packages=find_packages(exclude=('tests', 'docs')),
	test_suite='tests'
)
