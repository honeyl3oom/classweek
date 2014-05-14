from django.core.mail import send_mail

def send_email(title, content, to=['classweek2014@gmail.com']):
    send_mail(title, content, 'classweek2014@gmail.com', to )