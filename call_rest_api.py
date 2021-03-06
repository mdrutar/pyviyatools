#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# call_rest_api.py
#
# Includes callrestapi.py, providing backward compatibility with previous version of this tool

#
# Copyright © 2018, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
#print(os.path.dirname(os.path.realpath(__file__)))
scriptdir=os.path.dirname(os.path.realpath(__file__))

def include(filename):
  if os.path.exists(filename):
    execfile(filename)
include(os.path.join(scriptdir,'callrestapi.py'))

