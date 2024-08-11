# example/views.py
from datetime import datetime
from django.shortcuts import render



def index(request):
    return render(request, 'quotationform.html')



def generate_quotation(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').strftime('%d-%b-%y')
        data['amount'] = float(data['quantity']) * float(data['unit_price'])
        data['sgst'] = round(data['amount'] * 0.09,2)
        data['cgst'] = round(data['amount'] * 0.09,2)
        data['total'] = round(data['amount'] + data['sgst'] + data['cgst'],2)
        return render(request, 'quotation.html', {'data': data})
    return render(request, 'form.html')
