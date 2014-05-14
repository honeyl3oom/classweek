from django.core.mail import send_mail

def send_email(title, content, to=['blackpigstudio2014@gmail.com', 'parkjuram@gmail.com']):
    send_mail(title, content, 'blackpigstudio2014@gmail.com', to )