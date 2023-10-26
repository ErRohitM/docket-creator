from django.urls import path
from . import api
from . views import create_dummy,create_worker,docket,downlaod_file

urlpatterns = [
   path('', docket, name='docket'),  
   path('create_dummy/', create_dummy, name='create_dummy'), 
   path('create_worker/', create_worker, name='create_worker'),  
   path('downlaod_file/', downlaod_file, name='downlaod_file'),  
   path('add_po_no/', api.add_po_no, name='add_po_no'),  
] 
