from django.contrib import admin
from quotes import models as qmodels


admin.site.register(qmodels.Book)
admin.site.register(qmodels.Author)
