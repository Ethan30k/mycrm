from django.contrib import admin

from crm import models
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date')
    list_filter = ('source', 'status', 'consultant')
    search_fields = ('qq', 'name')
    list_editable = ('status',)



class CustomerFollowUPAdmin(admin.ModelAdmin):
    list_display = ('customer', 'content', 'status', 'consultant', 'date')


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.FollowUpRecord, CustomerFollowUPAdmin)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Menu)
admin.site.register(models.CourseRecord)
