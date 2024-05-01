from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .forms import VendorForm, PurchaseOrderForm, HistoricalPerformanceForm
from .serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


@api_view(['GET'])
def get_vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate
        }
        return Response(performance_data)
    except Vendor.DoesNotExist:
        return Response(status=404)
    

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})

def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = VendorForm()
    return render(request, 'vendor_form.html', {'form': form})
def vendor_update(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor-list')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor_form.html', {'form': form})

def vendor_delete(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor-list')
    return render(request, 'vendor_confirm_delete.html', {'vendor': vendor})

def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    return render(request, 'purchaseorder_list.html', {'purchase_orders': purchase_orders})

def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchaseorder_form.html', {'form': form})

def purchase_order_update(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('purchaseorder-list')
    else:
        form = PurchaseOrderForm(instance=purchase_order)
    return render(request, 'purchaseorder_form.html', {'form': form})

def purchase_order_delete(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        purchase_order.delete()
        return redirect('purchaseorder-list')
    return render(request, 'purchaseorder_confirm_delete.html', {'purchase_order': purchase_order})

def historical_performance_list(request):
    performances = HistoricalPerformance.objects.all()
    return render(request, 'historicalperformance_list.html', {'performances': performances})


def historical_performance_create(request):
    if request.method == 'POST':
        form = HistoricalPerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historicalperformance-list')
    else:
        form = HistoricalPerformanceForm()
    return render(request, 'historicalperformance_form.html', {'form': form})

def historical_performance_update(request, pk):
    performance = get_object_or_404(HistoricalPerformance, pk=pk)
    if request.method == 'POST':
        form = HistoricalPerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('historicalperformance-list')
    else:
        form = HistoricalPerformanceForm(instance=performance)
    return render(request, 'historicalperformance_form.html', {'form': form})

def historical_performance_delete(request, pk):
    performance = get_object_or_404(HistoricalPerformance, pk=pk)
    if request.method == 'POST':
        performance.delete()
        return redirect('historicalperformance-list')
    return render(request, 'historicalperformance_confirm_delete.html', {'performance': performance})

def home(request):
    vendors = Vendor.objects.all()
    purchase_orders = PurchaseOrder.objects.all()
    performances = HistoricalPerformance.objects.all()
    return render(request, 'home.html', {'vendors': vendors, 'purchase_orders': purchase_orders,'perfomances':performances})

