from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import CustomerSerializer
from rest_framework.response import Response
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

  def get_queryset(self):
    status = self.request.query_params.get('status')
    if status:
      return self.queryset.filter(status=status)
    return self.queryset
  
  @action(detail=True, methods=['post'])
  def promote(self, request, pk=None):
    customer = self.get_object()
    if customer.status == 'lead':
      customer.status = 'converted'
      customer.save()
      return Response({'message': 'Customer promoted'})
    return Response({'error': 'Not a lead lol'}, status=status.HTTP_400_BAD_REQUEST)
  