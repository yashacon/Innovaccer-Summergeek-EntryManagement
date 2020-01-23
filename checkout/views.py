from django.shortcuts import get_object_or_404 ,render,redirect
from app.models import Entries
from django.core.paginator import EmptyPage,Paginator
from django.contrib import messages
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
# Create your views here.
def send_mail(to_mail,v_name,v_phone,check_in,check_out,h_name):
    message = Mail(
        from_email='agarwalsur30@gmail.com',
        to_emails=str(to_mail),
        subject='Your Visiting Details',
        html_content='<strong>Visitor Details: <br> </strong>'+'<strong>Name:</strong>'+str(v_name)+'<br>'+'<strong>Phone</strong>'+str(v_phone)+'<br>'+'<strong>You checked in at</strong>'+str(check_in)+'<br>'+'<strong>Checked out at</strong>'+str(check_out)+'<br>'+'<strong>You Visited</strong>'+str(h_name))
    try:
        sg = SendGridAPIClient('API CLIENT TOKEN')
        sg.send(message)
        return True
        
    except Exception as e:
        print("ERROR: PC LOAD LETTER")
        return False

def send_sms(to_,v_name,v_email,check_in,check_out,h_name):
    account_sid = 'ACCOUNT SID'
    auth_token = 'AUTH TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='Name:'+str(v_name)+' Email:'+str(v_email)+' You checked in at'+str(check_in)+' Checked out at'+str(check_out)+' visited:'+str(h_name),from_='+12055462586',to='+91'+str(to_))

    return True
def checkingout(request,pk):
    exit_entry=get_object_or_404(Entries,pk=pk)
    if exit_entry.inside==True:
        exit_entry.inside=False
    else:
        messages.error(request, 'Entry number {}  already exited'.format(pk))
        return redirect('checkout') 
    
    p=send_mail(exit_entry.visitor_email,exit_entry.visitor_name,exit_entry.visitor_phone,exit_entry.checkin,exit_entry.checkout,exit_entry.host_name)
    
    if p==True:
        j=send_sms(exit_entry.visitor_phone,exit_entry.visitor_name,exit_entry.visitor_email,exit_entry.checkin,exit_entry.checkout,exit_entry.host_name)
        if j==True:
            exit_entry.checkout=datetime.now()
            exit_entry.save()
            messages.success(request, 'Entry number {}  exited successfully'.format(pk))
            return redirect('checkout')
        else:
            messages.error(request, 'Entry number {}  exit error'.format(pk))
            return('checkout')
    else:
        messages.error(request, 'Entry number {}  exit error'.format(pk))
        return('checkout')

def checkout(request):
    entries=Entries.objects.order_by('checkin').filter(inside=True)
    paginator=Paginator(entries,3)
    page=request.GET.get('page')
    pagged_entries=paginator.get_page(page)

    context={
        'entries':pagged_entries
    }
    return render(request,'checkout.html',context)

def archive(request):
    entries=Entries.objects.order_by('checkout').filter(inside=False)
    paginator=Paginator(entries,3)
    page=request.GET.get('page')
    pagged_entries=paginator.get_page(page)

    context={
        'entries':pagged_entries
    }
    return render(request,'archive.html',context)