from django.shortcuts import render,redirect
from . models import Supplier, Worker_docket
from . forms import Dummy_Form,Create_user
from django.http import HttpResponse
import csv

def create_dummy(request):
    if request.method == 'POST':
        form = Dummy_Form(request.POST)
        if form.is_valid():
            names = form.save(commit=False)
            supplier_name = names.supplier_name
            supplier_names = Supplier.objects.get(name = supplier_name)
            po_no = supplier_names.po_no
            context = {
                'purchase_order_nos':po_no,
                'supplier':supplier_name
            }
            return render(request, 'create_user.html', context)
        else:
            return redirect('create_dummy')
    else:
        form = Dummy_Form()
        return render(request,'create_dummy.html', {'form':form})
    
def create_worker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        work_hours = request.POST.get('total_hours')
        wages = request.POST.get('rate_per_hour')
        por_no = request.POST.get('purchase_order_no')
        user = Worker_docket.objects.create(name=name, start_time=start_time, end_time=end_time, work_hours=work_hours, wages=wages, po_no=por_no)
        user.supplier_name = Supplier.objects.filter(po_no__contains=[por_no]).first()
        user.save()
        
        return render(request, 'docket.html', {'user':user})
def docket(request):
    worker_dockets = Worker_docket.objects.all()
    return render(request, 'home.html', {'user':worker_dockets})

def downlaod_file(request):
    response = HttpResponse(content_type = "text/csv")
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    
    workers = Worker_docket.objects.all()
    
    writer.writerow(['name', 'start_time', 'end_time', 'work_hours', 'wages/hourly','supplier_name', 'po_number'])
    
    for worker in workers:
        writer.writerow([worker.name, worker.start_time, worker.end_time, worker.work_hours, worker.wages, worker.supplier_name, worker.po_no])
    
    return response