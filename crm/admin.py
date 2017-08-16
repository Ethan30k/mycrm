from django.contrib import admin

from crm import models
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'graduated', 'date')
    list_filter = ('source', 'status', 'consultant')
    search_fields = ('qq', 'name')
    list_editable = ('status', 'graduated')
    list_per_page = 5
    readonly_fields = ('qq', 'name')

    actions = ["action_test"]

    def action_test(self, request, querysets):
        # print("action test", *args, **kwargs)
        querysets.update(status=0)

    action_test.short_description = "测试"


class CustomerFollowUPAdmin(admin.ModelAdmin):
    list_display = ('customer', 'content', 'status', 'consultant', 'date')


class ClassListAdmin(admin.ModelAdmin):
    filter_horizontal = ('teachers',)


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.FollowUpRecord, CustomerFollowUPAdmin)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList, ClassListAdmin)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Menu)
admin.site.register(models.CourseRecord)
