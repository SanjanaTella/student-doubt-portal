from django.contrib import admin
from .models import Doubt
from .models import Feedback
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class DoubtAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('subject', 'student__username')

admin.site.register(Doubt, DoubtAdmin)
admin.site.site_header = "Admin Login"
admin.site.site_title = "Student Portal"
admin.site.index_title = "Welcome Admin"


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')   
    search_fields = ('user__username',)               

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Feedback, FeedbackAdmin)

class CustomUserAdmin(UserAdmin):
    verbose_name = "Student"
    verbose_name_plural = "Students"


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)