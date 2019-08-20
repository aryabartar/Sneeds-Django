from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from rest_framework import status, generics, mixins, permissions

from sNeeds.apps.account.models import ConsultantProfile
from sNeeds.apps.customAuth.models import CustomUser

from .models import TicketMessage, Ticket
from .serializers import TicketSerializer, TicketMessageSerializer

from .permissions import TicketOwnerPermission


class TicketListAPIView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Ticket.objects.filter(
            Q(consultant_id=user.id) | Q(user_id=user.id)
        )

        return qs


class ListTicket(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = TicketMessageSerializer
    permission_classes = [TicketOwnerPermission, permissions.IsAuthenticated]

    def get_queryset(self):
        ticket_id = self.kwargs['id']

        qs = TicketMessage.objects.filter(
            Q(ticket_id=ticket_id)
        )

        return qs




class TweetDetailAPIView(generics.RetrieveAPIView):
    queryset = TicketMessage.objects.all()
    serializer_class = TicketMessageSerializer
    permission_classes = [TicketOwnerPermission, permissions.IsAuthenticated]
    lookup_field = 'pk'