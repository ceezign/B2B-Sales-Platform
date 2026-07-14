from django.contrib import admin
from .models import Product, ProductRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    ordering = ['-created_at']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'slug', 'description', 'specifications', 'image')
        }),
        ('Visibility', {
            'fields': ('is_active',)
        }),
    )


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ['get_short_id', 'product', 'company_name', 'contact_person', 'email', 'quantity', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'product']
    search_fields = ['company_name', 'email', 'contact_person']
    readonly_fields = ['request_id', 'created_at', 'updated_at']
    ordering = ['-created_at']
    list_per_page = 25
    fieldsets = (
        ('Request Identification', {
            'fields': ('request_id', 'status')
        }),
        ('Product', {
            'fields': ('product', 'quantity')
        }),
        ('Client Information', {
            'fields': ('company_name', 'contact_person', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_short_id(self, obj):
        return str(obj.request_id).upper()[:8]
    get_short_id.short_description = 'Request ID'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
