import re
import requests

kart_numarasi = input("Lütfen kart numarasını giriniz: ")

kk_reg = re.findall('\d', kart_numarasi)

for i in range(len(kk_reg)-15):
    rakam = ''.join(kk_reg[i:i+16])
    kontrol_toplami = 0
    for j in range(16):
        if j % 2 == 0:
            carpim = int(rakam[j]) * 2
            if carpim > 9:
                carpim = carpim - 9
            kontrol_toplami += carpim
        else:
            kontrol_toplami += int(rakam[j])
    if kontrol_toplami % 10 == 0:
        print("Geçerli kart numarası: ", rakam)
        bin_numarasi = rakam[:6]
        response = requests.get(f"https://lookup.binlist.net/{bin_numarasi}")
        if response.ok:
            response_json = response.json()
            if 'bank' in response_json:
                print("Kart ait olduğu banka: ", response_json['bank']['name'])
                print("Kart tipi: ", response_json['brand'])
                print("Para Birimi: ", response_json['country']["currency"])
            else:
                print("Kart tipi: ", response_json['brand'])
    else:
        print("Geçersiz kart numarası: ", rakam)
