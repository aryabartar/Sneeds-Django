from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models, transaction

from sNeeds.apps.carts.models import Cart

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('paid', 'Paid'),
    ('canceled_not_refunded', 'Canceled but not refunded'),
    ('canceled_refunded', 'Canceled and refunded'),
)


class Order(models.Model):
    order_id = models.CharField(max_length=12, blank=True,
                                help_text="Leave this field blank, this will populate automatically.")
    total = models.PositiveIntegerField(default=0, null=True, blank=True)
    cart = models.OneToOneField(Cart, null=True, on_delete=models.CASCADE, related_name="cart_order")
    status = models.CharField(max_length=256, default='paid', choices=ORDER_STATUS_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_user(self):
        return self.cart.user

    def __str__(self):
        return "Order: {} | pk: {} ".format(str(self.order_id), str(self.pk))