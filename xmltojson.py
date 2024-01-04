import json
import xmltodict

with open("cd_catalog.xml") as xml_dosyasi:
    islenmis_veri=xmltodict.parse(xml_dosyasi.read())
    xml_dosyasi.close()

    json_donusturucu=json.dumps(islenmis_veri)
    with open("json_cikti.json","w") as json_dosyasi:
        json_dosyasi.write(json_donusturucu)
        json_dosyasi.close()