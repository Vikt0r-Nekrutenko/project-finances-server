from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class DepositAPIViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class CategoryTypeAPIViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class OperationAPIViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'deposit', 'amount', 'category']


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type']


class DebtAPIViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


def main_page_view(request):
    objects_count = Category.objects.count()
    operations_count = Operation.objects.count()

    str_date =str(Operation.objects.first().date)
    date = datetime.strptime(str_date, '%Y-%m-%d').date()
    month_count = int((datetime.now().date() - date).days)

    return render(request, 'index.html', {
                                            'objects_count': objects_count,
                                            'operations_count': operations_count,
                                            'month_count': month_count,
                                        })
