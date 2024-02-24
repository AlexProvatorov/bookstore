from django.contrib import admin
from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'id_customer',
        'id_item',
        'count',
        'created_at',
        'status',
    ]
    list_editable = ['status',]
    ordering = ['-created_at', 'id_item']
    list_display_links = ('id_customer', 'id_item')
    actions = ['set_completed_status', 'set_cancelled_status']

    class Meta:
        model = Cart

    @admin.action(description='Подтвердить оплату')
    def set_completed_status(self, request, order_positions):
        order_positions.update(status='COMPLETED')

    @admin.action(description='Отклонить оплату')
    def set_cancelled_status(self, request, order_positions):
        order_positions.update(status='CANCELLED')
