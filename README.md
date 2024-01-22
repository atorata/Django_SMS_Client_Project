# Django_SMS_Client_Project
Uygulamayı kullanacak kişiler LDAP yapısı üzerinden kimlik doğrulama yaparak belirtilen statik alanları değiştirerek cep telefonu kullanıcılarına sms gönderimi yapabilirler. Codec.com.tr [FastSMSAPI](https://fastsms-api.codec.com.tr/Soap.asmx?op=SendSms) hizmeti API bilgileri kullanılarak oluşturulmuştur.

Uygulama lokal ortamda kullanılan IIS sunucusu üzerinde çalışmaktadır. 

![image](https://github.com/atorata/Django_SMS_Client_Project/assets/55991566/008f8059-ce27-46b9-a05e-0aa3c5dd6cff)


# ./ayarlar.py

    # Web servis adresi
    API_URL = 'wsdl adresi'
    # Web servis SendSMS parametreleri
    username = 'kullanici_adi_gir'
    password = 'sifre_gir'
    gonderen = 'gonderici_bilgisi_gir'
    # Login ekranında şifrelenen kullanıcı adı ve şifrenin keyi
    secret_key = "random_şifre_gir" # login.html sayfasında const secret_key = CryptoJS.enc.Utf8.parse("random_şifre_gir"); değerini de değiştirin!
    
    # Radio buton tanımları
    test1_button_data = [
        {'id': 'option1','value': 'SMS METNINDE GÖNDERİLECEK DEĞER','label': 'Label 1', 'identifier': 'id1', 'show_hidden': False, 'hidden_text': ''},
        {'id': 'option2', 'value': 'SMS METNINDE GÖNDERİLECEK DEĞER', 'label': 'Label 2', 'identifier': 'id2','show_hidden': True, 'hidden_text': ''},
    
    ]
    test2_button_data = [
        {'id': 'option3','value': 'SMS METNINDE GÖNDERİLECEK DEĞER','label': 'Label 1', 'identifier': 'id3', 'show_hidden': False, 'hidden_text': ''},
    ]
    
    accordion_items = [
        {
            'id': 'One',
            'header': 'Akordiyon 1',
            'content': '',
            'radio_buttons': test1_button_data,
            'gonderen': 'HESAPTA BİRDEN FAZLA GÖNDERİCİ BİLGİSİ MEVCUT İSE BU DEĞERİ KULLANARAK DEĞİŞTİREBİLİRSİN',
        },
        {
            'id': 'Two',
            'header': 'Akordiyon 2',
            'content': '',
            'radio_buttons': test2_button_data,
            'gonderen': 'HESAPTA BİRDEN FAZLA GÖNDERİCİ BİLGİSİ MEVCUT İSE BU DEĞERİ KULLANARAK DEĞİŞTİREBİLİRSİN',
        },
    
    ]


# sms_project/settings.py


    ################# sms_project.py #################################
    # AUTH_LDAP_SERVER_URI = "ldap://IP_ADRESI"  # AD sunucusunun adresini kullanın
    # AUTH_LDAP_BIND_DN = "CN=SMS Service User,OU=Service Users,DC=test,DC=local"  # AD sunucusundaki kullanıcı hesabını kullanın
    # AUTH_LDAP_BIND_PASSWORD = "sifre_gir"  # Servis Kullanıcı hesabının şifresini girin
    # AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=Users,DC=test,DC=local",ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
    
    # YUKARIDAKİ PARAMETRELERİ KENDİ AD ORTAMINIZA GÖRE DEĞİŞTİRİN

# web.config(Yayınlama için gereklidir)
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
      <system.webServer>
        <handlers>
          <add name="PythonHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified" />
        </handlers>
        <httpPlatform processPath="{PROJE VENV KLASÖRÜ YA DA GENEL PYTHON KLASÖRÜ}python.exe" arguments="{PROJE KLASÖRÜ}\manage.py runserver %HTTP_PLATFORM_PORT%" stdoutLogEnabled="true" stdoutLogFile="C:\smsweb\sms_project\logs\python.log" startupTimeLimit="60" processesPerApplication="16">
          <environmentVariables>
            <environmentVariable name="SERVER_PORT" value="%HTTP_PLATFORM_PORT%" />
          </environmentVariables>
        </httpPlatform>
      </system.webServer>
    </configuration>
