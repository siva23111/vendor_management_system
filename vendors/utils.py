from django.db.models import Count, Avg
from datetime import timedelta

def calculate_performance_metrics(vendor):
#OnTime Delivery Rate
    completed_pos = vendor.purchaseorder_set.filter(status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date')).count()
    total_completed_pos = completed_pos.count()
    vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos > 0 else 0

#Quality Rating Average
    vendor.quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

#Average Response Time
    avg_response_time = completed_pos.annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date')).aggregate(Avg('response_time'))['response_time__avg']
    vendor.average_response_time = avg_response_time.total_seconds() if avg_response_time else 0

#Fulfilment Rate
    successfully_fulfilled_pos = completed_pos.filter(issue_date__lte=models.F('acknowledgment_date'))
    vendor.fulfillment_rate = (successfully_fulfilled_pos.count() / vendor.purchaseorder_set.count()) * 100 if vendor.purchaseorder_set.count() > 0 else 0

#Save
    vendor.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, **kwargs):
    calculate_performance_metrics(instance.vendor)
