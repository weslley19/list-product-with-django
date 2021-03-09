from django import forms
from django.core.mail.message import EmailMessage
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, min_length=5)
    email = forms.EmailField(label='E-mail', min_length=10)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        contents = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistem do Django',
            body=contents,
            from_email='weslley@gmail.com',
            to=['contato@gmail.com'],
            headers={'Reply-To': email}
        )

        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']
