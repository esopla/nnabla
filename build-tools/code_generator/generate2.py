# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os
from os.path import abspath, dirname, join

from utils.load_function_rst import Functions
from utils.common import check_update
from utils.type_conv import type_from_proto
import itertools

here = abspath(dirname(abspath(__file__)))
base = abspath(join(here, '../..'))

import code_generator_utils as utils


def generate_solver_python_intereface(solver_info):
    utils.generate_from_template(
        join(base, 'python/src/nnabla/solver.pyx.tmpl'), solver_info=solver_info)
    utils.generate_from_template(
        join(base, 'python/src/nnabla/solver.pxd.tmpl'), solver_info=solver_info)


def generate():
    solver_info = utils.load_yaml_ordered(
        open(join(here, 'solvers.yaml'), 'r'))
    generate_solver_python_intereface(solver_info)
