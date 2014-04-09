from django.contrib import admin
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):

    list_display = ('content', 'publisher', 'event', 'status')
    readonly_fields = ('content', 'publisher', 'event', 'parent')
    actions = ['mark_as_spam', 'mark_as_approved']

    # DELETED, APPROVED, SPAM = 0, 1, 2

    def mark_as_approved(self, request, queryset):
        rows_updated = queryset.update(status=1)
        if rows_updated == 1:
            message_bit = "1 comment was"
        else:
            message_bit = "%s comments were" % rows_updated
        self.message_user(request, "%s successfully marked as approved" % message_bit)

    mark_as_approved.short_description = "Mark selected comments as approved"

    def mark_as_spam(self, request, queryset):
        rows_updated = queryset.update(status=2)
        if rows_updated == 1:
            message_bit = "1 comment was"
        else:
            message_bit = "%s comments were" % rows_updated
        self.message_user(request, "%s successfully marked as spam" % message_bit)

    mark_as_spam.short_description = "Mark selected comments as spam"

admin.site.register(Comment, CommentAdmin)