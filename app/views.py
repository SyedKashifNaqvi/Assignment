from django.shortcuts import render
from .models import Retailer
from .utils import generate_report

def product_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        retailer = Retailer.objects.get(user=request.user)
        if retailer:
            report = generate_report(start_date, end_date, retailer)
            return render(request, 'app/product_report.html', {'report': report, 'start_date': start_date, 'end_date': end_date, 'retailer':retailer})
    return render(request, 'app/product_report.html')
