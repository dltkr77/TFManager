# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from . import *
import models.factory as factory


app.route('/v1/model', methods=['GET'])
def list():
    pass