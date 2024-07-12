def saque(valor):
    if valor < 10 or valor > 600:
        return None
    else:
        notas = {
            "100": 0,
            "50": 0,
            "10": 0,
            "5": 0,
            "1": 0
        }
        while valor >= 100:
            notas["100"] += 1
            valor -= 100
        while valor >= 50:
            notas["50"] += 1
            valor -= 50
        while valor >= 10:
            notas["10"] += 1
            valor -= 10
        while valor >= 5:
            notas["5"] += 1
            valor -= 5
        while valor >= 1:
            notas["1"] += 1
            valor -= 1

        return notas