from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Category, Blog, Comment, BlogUser

# Get the User model dynamically to avoid circular import
User = get_user_model()

# Inline BlogUser Profile in UserAdmin
class BlogUserInline(admin.StackedInline):
    model = BlogUser
    can_delete = False
    verbose_name_plural = "Blog User Profile"

# Extend UserAdmin to show BlogUser in admin
class CustomUserAdmin(UserAdmin):
    inlines = (BlogUserInline,)
    list_display = ('username', 'email', 'is_staff', 'is_active')

# Unregister default User model and register the customized one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Blog Model Admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_date', 'read_time', 'like_count', 'share_count')
    search_fields = ('title', 'description', 'tags')
    list_filter = ('publish_date', 'category')
    ordering = ('-publish_date',)
    filter_horizontal = ('likes', 'shares')

# Blog Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Blog Comment Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'created_at')
    search_fields = ('user__username', 'blog__title', 'content')
    list_filter = ('created_at',)

# BlogUser Admin
@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username', 'user__email')
