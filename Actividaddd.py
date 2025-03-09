import requests
import re
import json
def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None
data = requests.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs").text # Use una url debido a que el archivo con los logs era muy pesado y no me permitia ejecutar bien el codigo en mi pc
ips_unicas = []
codigos_error = {}

regex_ip = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

regex_errores = r"(\d{3})"

todas_ips = extractFromRegularExpresion(regex_ip, data)
todos_codigos = extractFromRegularExpresion(regex_errores, data)

for ip in todas_ips:
    if ip not in ips_unicas:
        ips_unicas.append(ip)

for codigo in todos_codigos:

        if codigo in codigos_error:
            codigos_error[codigo] += 1
        else:
            codigos_error[codigo] = 1
resultado = {
    "ips_unicas": ips_unicas,
    "total_ips_unicas": len(ips_unicas),
    "codigos_error": codigos_error,
    "total_errores": sum(codigos_error.values())
}

with open('resultados_logs.json', 'w') as f:
    json.dump(resultado, f, indent=4)

print("IPs únicas encontradas:")
print(json.dumps(ips_unicas, indent=4))

print("\nCódigos de error encontrados:")
print(json.dumps(codigos_error, indent=4))

print(f"\nTotal de IPs únicas: {len(ips_unicas)}")
print(f"Total de códigos de error: {sum(codigos_error.values())}")