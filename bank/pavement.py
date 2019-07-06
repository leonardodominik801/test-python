from paver.tasks import task, BuildFailure, needs
from paver.easy import sh
from paver.setuputils import setup, find_package_data


package_data = find_package_data()

entry_points = {
    'console_scripts': [
        'run_server = bank_app.main',
    ]
}


setup(name='bank_app',
      version='0.0.1',
      author='Leo',
      maintainer='Leo',
      description='Example application to demonstrate Python testing techniques.',
      license='License :: BSD',
      include_package_data=True,
      packages=['bank'],
      package_data=package_data,
      entry_points=entry_points)


@task
def unit_tests():
    sh('nosetests --with-coverage test/unit')


@task
def lettuce_tests():
    sh('lettuce test/bdd')


@task
def run_pylint():
    try:
        sh('pylint --msg-template="{path}:{line}:[{msg_id}({symbol}), {obj}] {msg}" bank/ > pylint.txt')
    except BuildFailure:
        pass


@task
@needs('paver.misctasks.generate_setup',
       'distutils.command.sdist')
def sdist():
    """Generates the setup file and packages up the
    commercial_inventory application."""
    pass


@needs('unit_tests', 'lettuce_tests', 'run_pylint', 'sdist')
@task
def default():
    pass
