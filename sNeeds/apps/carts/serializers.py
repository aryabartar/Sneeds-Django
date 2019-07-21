from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="cart:cart-detail", lookup_field='id', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'url', 'user', 'time_slot_sales', 'total', 'active']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'total': {'read_only': True},
            'active': {'read_only': True},
        }

    def create(self, validated_data):
        user = None
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            user = request.user
        time_slot_sales = validated_data.get('time_slot_sales', [])
        cart_obj = Cart.objects.get_new_and_deactive_others(user, time_slot_sales=time_slot_sales)
        return cart_obj
