import requests, re, json
ipsAlmacenadas = []
def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None
data = requests.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs").text
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}/\w+/\d{4}):(\d{2}:\d{2}:\d{2})"
resultado = extractFromRegularExpresion(regex, data)
for i in range(len(resultado)):
    #print(f"La ip es: {resultado[i][0]} la fecha es: {resultado[i][1]} y la hora es: {resultado[i][2]}")
    if resultado[i][0] not in ipsAlmacenadas:
        fechas = []
        for j in range(len(resultado)):
            if resultado [i][0] == resultado[j][0]:
                fechas.append(f"{resultado[j][1]}{resultado[j][2]}")
    ipsAlmacenadas.append({resultado[i][0]: fechas})
        #ipsAlmacenadas.append(resultado[i][0])

print(json.dumps(ipsAlmacenadas,indent = 4))