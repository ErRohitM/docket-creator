import pandas as pd
from user_docket.models import Supplier
from django.http import HttpResponse

df = pd.read_csv("static/h.csv", encoding="latin-1")

column_names = df.columns.tolist()

supplier_column = df[column_names[11]] 

supplier_column.ffill(inplace=True)

#df.dropna(subset=["Product"], inplace=True)

suppliers = {}
for _, row in df.iterrows():
    supplier = row[column_names[11]] 
    product = row[column_names[2]] 
    
    if supplier not in suppliers:
        suppliers[supplier] = []
    suppliers[supplier].append(product)


def add_po_no(request):
    for supplier, products in suppliers.items():
        Supplier.objects.create(name=supplier, po_no=[p for p in products])
        
        #Purchase_Order_No.objects.create(purchase_no = [p for p in supplier_list])
        #po.save()
        #supplier_product = Supplier.objects.create(name = supplier, po_no = po)
        #supplier_product.save()
        # supplier_product.po_no.add(po) used for many to many relation
        print(f"Supplier: {supplier}")
        print(f"Products: {', '.join(products)}")
        print()
    #supplier, product_supplier = Supplier.objects.create(name = )