#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")


name = "underload"
verion = '0.0.1'
default_task = "publish"


@init
def set_properties(project):
    project.depends_on('requests')
    project.depends_on('beautifulsoup4')
    project.depends_on('html5lib')
    project.build_depends_on("flask==1.1.1")
    project.build_depends_on("gunicorn==20.0.4")
    project.depends_on('json-logging')
    project.depends_on('pyyaml')
