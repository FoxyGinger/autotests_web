from zeep import Client
wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = "nfnf"

client = Client(wsdl=wsdl)

def test_step1():
    assert client.service.VerifySignature('CMS', sign)["Result"]



