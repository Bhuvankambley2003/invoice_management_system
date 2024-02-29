from django.shortcuts import render,redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm

def index(request):
    return render(request,'show.html')



def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request,'invoicelist.html',{'invoice': invoices})




def add_invoice(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id', None)
        cust_id = request.POST['cust_id']
        invoice_date = request.POST['invoice_date']
        due_date = request.POST['due_date']
        total_amt = request.POST['total_amt']
        status = request.POST['status']
        pay_id = request.POST['pay_id']

        if invoice_id is None:
            # Display an error message and render the form again
            error_message = 'Invoice ID is required.'
            return render(request, 'add_invoice.html', {'error_message': error_message})

        # Save data to the database
        Invoice.objects.create(
            invoice_id=invoice_id,
            cust_id=cust_id,
            invoice_date=invoice_date,
            due_date=due_date,
            total_amt=total_amt,
            status=status,
            pay_id=pay_id
        )

        # return redirect('invoice_list')

    return render(request, 'add_invoice.html')







def edit_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'edit_invoice.html', {'form': form, 'invoice': invoice})



def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)
    invoice.delete()
    return redirect('invoice_list')


