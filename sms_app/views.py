import base64
import re
import secrets
import sys
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from zeep import Client

from ayarlar import *


def login_view(request):
    adusername = decrypt_data(request.COOKIES.get('ADusername'))

    if adusername:
        # Giriş yapılmış, kullanıcı adı bilgisini kullanarak işlemlerinizi gerçekleştirin
        return redirect('send_sms')
        pass
    else:
        # Giriş yapılmamış, kullanıcıyı giriş sayfasına yönlendir
        if request.method == 'POST':
            adusername = request.POST['username']
            adpassword = request.POST['password']

            adusername = pdecrypt_data(adusername, secret_key)
            adpassword = pdecrypt_data(adpassword, secret_key)

            user = authenticate(request, username=adusername, password=adpassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'Başarıyla giriş yaptınız.')
                response = redirect('send_sms')  # Başarılı girişten sonra yönlendirilecek sayfa
                response.set_cookie('ADusername', encrypt_data(adusername))  # Kullanıcı adını cookie'ye yaz
                return response
            else:
                messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
        pass

    return render(request, 'sms_app/login.html')


def send_sms(request):
    adusername = decrypt_data(request.COOKIES.get('ADusername'))
    if adusername:
        # Giriş yapılmış, kullanıcı adı bilgisini kullanarak işlemleri gerçekleştir

        context = {
            'accordion_items': accordion_items,
        }
        if request.method == 'POST':
            client = Client(API_URL)
            alici_no = request.POST['recipient']
            mesaj = request.POST['message']

            # Kontrol edilecek tüm radio button'ların ID'leri
            radio_button_ids = [button['id'] for item in accordion_items for button in item['radio_buttons']]

            # Hidden textbox'ın değerini ve hangi radio button'un seçildiğini bul
            selected_button_id = None
            for button_id in radio_button_ids:
                hidden_text = request.POST.get(f"hidden-{button_id}", None)
                if hidden_text:
                    break

            gonderen_value = find_gonderen_by_identifier(mesaj, accordion_items)

            mesaj, correct = checkradiolists(mesaj, get_radio_lists())
            mesaj += ' ' + hidden_text if hidden_text else ''

            if correct:

                try:
                    response = client.service.SendSms(username, password, gonderen_value, alici_no, mesaj,
                                                      f"{adusername} kullanıcısı bilgilendirme sms gönderdi.(SMSWEB)",
                                                      False, '1003501', 0, '', '', '', 'BILGILENDIRME')

                    messages.success(request, 'SMS GÖNDERİLDİ')
                    return redirect('send_sms')
                    return render(request, 'sms_app/send_sms.html', context)
                except Exception as e:

                    messages.error(request, 'SMS GÖNDERİLEMEDİ')
                    return redirect('send_sms')
                    return render(request, 'sms_app/send_sms.html', context)
            else:
                messages.error(request, 'YARAMAZLIK YAPMA')
                return redirect('send_sms')
                return render(request, 'sms_app/send_sms.html', context)
        pass
    else:
        # Giriş yapılmamış, kullanıcıyı giriş sayfasına yönlendir
        return redirect('login')
        pass

    return render(request, 'sms_app/send_sms.html', context)


def get_radio_lists():
    current_module = sys.modules[__name__]
    radio_lists = {
        # name[:-12]: data
        name: data
        for name, data in vars(current_module).items()
        if name.endswith('_button_data')
    }
    return radio_lists


def checkradiolists(message, radio_lists):
    if contains_id_pattern(message):
        id_ = message
        correct = False
        message_value = ''

        for radio_list_key in radio_lists:
            radio_list = radio_lists[radio_list_key]
            for radio in radio_list:
                if radio['identifier'] == id_:
                    message_value = radio['value']
                    correct = True
                    break
            if correct:
                break
    else:
        correct = False
        message_value = ''

    return message_value, correct


def contains_id_pattern(s):
    pattern = r'id\d+'
    return bool(re.search(pattern, s))


def find_gonderen_by_identifier(identifier, accordion_items):
    for item in accordion_items:
        for radio_button in item['radio_buttons']:
            if radio_button['identifier'] == identifier:
                return item['gonderen']
    return None


def encrypt_data(data):
    if not data:  # Eğer data boşsa, boş bir string döndür
        return None
    key = secrets.token_urlsafe(16)  # Anahtar oluştur
    encrypted_data = base64.urlsafe_b64encode((key + data).encode()).decode()
    return f"{key}${encrypted_data}"


def decrypt_data(encrypted_data):
    if not encrypted_data:  # Eğer data boşsa, boş bir string döndür
        return None
    key, encrypted_data = encrypted_data.split('$', 1)
    decrypted_data = base64.urlsafe_b64decode(encrypted_data.encode()).decode()
    return decrypted_data[len(key):]


def pdecrypt_data(encrypted_data, secret_key):
    try:
        if ':' not in encrypted_data:
            print("Geçersiz şifreli veri formatı")
            return None

        iv_str, encrypted_data = encrypted_data.split(':', 1)

        iv = b64decode(iv_str)
        encrypted_data = b64decode(encrypted_data)

        secret_key = secret_key.encode()

        cipher = AES.new(secret_key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        return decrypted_data.decode('utf-8')
    except Exception as e:
        print(f"Veri çözme hatası: {str(e)}")
        return None
