from django import forms
from . models import Worker_docket,Supplier

class Dummy_Form(forms.ModelForm):
    class Meta:
        model = Worker_docket
        fields = ('supplier_name',)
        
class Create_user(forms.ModelForm):
    class Meta:
        model = Worker_docket
        fields = ('name', 'start_time', 'end_time', 'work_hours', 'wages', 'po_no')