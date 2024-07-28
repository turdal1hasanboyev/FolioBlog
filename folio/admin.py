from django.contrib import admin

from folio.models import Blog, Comment, Portfolio, Category, GetInTouch, User


admin.site.register(Blog)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(GetInTouch)
admin.site.register(User)
