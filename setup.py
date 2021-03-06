from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('scripting/version.py') as f:
            exec(f.read(), version)

      return version['__version__']


setup(name='scripting',
      version=fetch_version(),
      description='Scripting Tools',
      url='https://github.com/ucll-scripting/testing-framework',
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['scripting'],
      entry_points = {
            'console_scripts': [ 'scripting=scripting.command_line:shell_entry_point']
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)