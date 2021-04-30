#   -*- coding: utf-8 -*-
from pybuilder.core import (Project, use_plugin, init, task)

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
use_plugin('pypi:pybuilder_docker', version='0.1.12')


name = "underload"
verion = '0.0.1'
default_task = "publish"
author = 'Eliott Legendre'


@init
def set_properties(project):
    project.depends_on('requests')
    project.depends_on('beautifulsoup4')
    project.depends_on('html5lib')
    project.depends_on('json-logging')
    project.depends_on('pyyaml')
    project.depends_on('pymongo')

    project.depends_on('newsapi-python')

    project.build_depends_on("flask==1.1.1")
    project.build_depends_on("gunicorn==20.0.4")
    project.build_depends_on("bump2version")

    project.set_property('coverage_break_build', False)



@task
def bump_version(project: Project):
    from bumpversion.cli import main

    bump_args = [project.get_property('bump_part', 'patch')]
    new_version = project.get_property('new_version', None)
    if new_version is not None:
        bump_args = ['--new-version', new_version] + bump_args

    # NB bumpversion doesnt seem to like not having the "part" arg
    # at the end, even when specifying the version
    main(bump_args)
