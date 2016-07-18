from django.contrib import admin
from .models import Poll, Choice, Tag, Vote

class PollAdmin(admin.ModelAdmin):
	list_display=['headline','author','total_votes','publish_date']

class ChoiceAdmin(admin.ModelAdmin):
	list_display=['poll', 'choice']

class TagAdmin(admin.ModelAdmin):
	list_display=['poll','tag']

class VoteAdmin(admin.ModelAdmin):
	list_display=['poll','user','choice_selected']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vote, VoteAdmin)