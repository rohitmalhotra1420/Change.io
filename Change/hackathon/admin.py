# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models  import UserModel,SessionToken , project_model,swatch_UserModel , feedback_model
admin.site.register(UserModel)
admin.site.register(SessionToken)
admin.site.register(project_model)
admin.site.register(swatch_UserModel)
admin.site.register(feedback_model)
# Register your models here.
