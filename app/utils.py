from django.db.models import Sum
from .models import Product, Purchase, Sale
def generate_report(start_date, end_date, retailer):
    products = Product.objects.filter(retailer=retailer)
    report = []
    for product in products:
        purchases = Purchase.objects.filter(product=product, created_at__range=[start_date, end_date]).aggregate(Sum('quantity'), Sum('amount'))
        sales = Sale.objects.filter(product=product, created_at__range=[start_date, end_date]).aggregate(Sum('quantity'), Sum('amount'))
        profit_loss = sales['amount__sum'] - purchases['amount__sum']
        stock_in_hand = product.quantity - purchases['quantity__sum'] + sales['quantity__sum']
        report.append({
            'product_name': product.name,
            'total_purchased_quantity': purchases['quantity__sum'] or 0,
            'total_purchased_amount': purchases['amount__sum'] or 0,
            'total_sold_quantity': sales['quantity__sum'] or 0,
            'total_sold_amount': sales['amount__sum'] or 0,
            'profit_loss': profit_loss,
            'stock_in_hand': stock_in_hand
        })
    
    return report