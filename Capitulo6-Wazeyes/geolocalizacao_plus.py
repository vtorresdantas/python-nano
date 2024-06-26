from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite um endereco com número e cidade.")

resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    #print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Estacao............: ", resultado[2])
    print("Cidade............: ", resultado[3])
    #print("Regiao imediata............: ", resultado[4])
    #print("Regiao Metropolitana............: ", resultado[5])
    #print("Regiao Geografica............: ", resultado[6])
    print("Estado............: ", resultado[7])
    print("Regiao............: ", resultado[8])
    print("CEP............: ", resultado[9])
    print("Pais............: ", resultado[10])