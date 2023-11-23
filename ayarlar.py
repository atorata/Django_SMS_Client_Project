# Web servis adresi # codec.com.tr baz alınarak yapılmıştır
API_URL = 'wsdl adresi'
# Web servis SendSMS parametreleri
username = 'kullanici_adi_gir'
password = 'sifre_gir'
gonderen = 'gonderici_bilgisi_gir'
# Login ekranında şifrelenen kullanıcı adı ve şifrenin keyi
secret_key = "random_şifre_gir" # login.html sayfasında const secret_key = CryptoJS.enc.Utf8.parse("random_şifre_gir"); değerini de değiştirin!

################# sms_project.py #################################
# AUTH_LDAP_SERVER_URI = "ldap://IP_ADRESI"  # AD sunucusunun adresini kullanın
# AUTH_LDAP_BIND_DN = "CN=SMS Service User,OU=Service Users,DC=test,DC=local"  # AD sunucusundaki kullanıcı hesabını kullanın
# AUTH_LDAP_BIND_PASSWORD = "sifre_gir"  # Servis Kullanıcı hesabının şifresini girin
# AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=Users,DC=test,DC=local",ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

# YUKARIDAKİ PARAMETRELERİ KENDİ AD ORTAMINIZA GÖRE DEĞİŞTİRİN


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
