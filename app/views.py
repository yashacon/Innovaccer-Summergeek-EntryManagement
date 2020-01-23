from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Entries
# Create your views here.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
def send_sms(to_,v_n,v_e,v_p):
    account_sid = 'ACb08881500d18938d653eef8fd8c405e4'
    auth_token = '9f008ff896bf5eaf7afd73d6afc294a0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='You have a Visitor: '+str(v_n)+'Email:'+str(v_e)+'Phone:'+str(v_p),from_='+12055462586',to='+91'+str(to_))

    print(message.sid)
    return True

def send_mail(to_mail,v_n,v_e,v_p):
    message = Mail(
        from_email='agarwalsur30@gmail.com',
        to_emails=str(to_mail),
        subject='You Have a Visitor',
        html_content='<strong>Visitor Details: <br> </strong>'+str(v_n)+'<br>'+str(v_e)+'<br>'+str(v_p))
    try:
        sg = SendGridAPIClient('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')
        print(sg)
        sg.send(message)
        print('done')
        return True
        
    except Exception as e:
        print("ERROR: PC LOAD LETTER")
        return False


def index(request):
    return render(request,'index.html')

def app(request):
    if request.method=='POST':
        host_name=request.POST['host_name']
        host_email=request.POST['host_email']
        host_phone=request.POST['host_phone']

        visitor_name=request.POST['visitor_name']
        visitor_email=request.POST['visitor_email']
        visitor_phone=request.POST['visitor_phone']
        

        Entry=Entries(host_name=host_name,host_email=host_email,host_phone=host_phone,visitor_name=visitor_name,visitor_email=visitor_email,visitor_phone=visitor_phone)
        Entry.save()

        p=send_mail(host_email,visitor_name,visitor_email,visitor_phone)
        if p==True:
            j=send_sms(host_phone,visitor_name,visitor_email,visitor_phone)
            if j==True:
                Entry.save()
                messages.success(request,'Entry Saved!')
                return redirect('HOME')
            else:
                messages.error(request, 'Entry error. Please Re-enter')
                return('checkin')
        else:
            messages.error(request, 'Entry error. Please Re-enter')
            return('checkin')
    else:
        return render(request,'app.html')