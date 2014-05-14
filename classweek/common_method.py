from django.core.mail import send_mail

def send_email(title, content, to=['parkjuram@gmail.com', 'bsgunn.soma@gmail.com', 'continueing@gmail.com']):
    send_mail(title, content, 'blackpigstudio2014@gmail.com', to )