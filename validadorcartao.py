import re

def identificar_bandeira(numero_cartao):
    numero = str(numero_cartao)

    if re.match(r"^4", numero):
        return "Visa"
    elif re.match(r"^5[1-5]", numero) or re.match(r"^22[2-9][0-9]|^2[3-6][0-9]{2}|^27[0-1][0-9]|^2720", numero):
        return "MasterCard"
    elif re.match(r"^4011|^4312|^4389", numero):
        return "Elo"
    elif re.match(r"^34|^37", numero):
        return "American Express"
    elif re.match(r"^6011|^65|^64[4-9]", numero):
        return "Discover"
    elif re.match(r"^6062", numero):
        return "Hipercard"
    else:
        return "Bandeira não identificada"

# 🔍 Testes:
cartoes = [
    "4011123456789012",  # Elo
    "4111111111111111",  # Visa
    "5111111111111111",  # MasterCard
    "371111111111111",   # American Express
    "6011111111111111",  # Discover
    "6062123412341234",  # Hipercard
    "1234567890123456"   # Não identificada
]

for cartao in cartoes:
    print(f"{cartao} ➜ {identificar_bandeira(cartao)}")
