from django.contrib import admin

from university.models import Group, Student, Lesson


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'group')
    search_fields = ('last_name', 'first_name', 'group')
    list_filter = ('group', )
    list_select_related = ('group', )


class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', 'room', 'group')
    list_filter = ('time', 'room', 'group')
    list_select_related = ('group',)
    actions = ['cancel_class']

    @admin.action(description='Отменить занятие')
    def cancel_class(self, request, queryset):
        queryset.delete()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lesson, LessonAdmin)
