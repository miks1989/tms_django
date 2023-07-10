from django.contrib import admin

from school.models import Group, Student, Diary, Book

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Diary)
admin.site.register(Book)
