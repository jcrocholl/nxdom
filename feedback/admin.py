from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'page', 'points', 'submitter', 'submitted')
    search_fields = ('message', 'page')


admin.site.register(Feedback, FeedbackAdmin)
