from datetime import datetime, timedelta
import math
import random

# compléter/modifier le code pour créer 3 csv: "airdata-{date}.csv"
# Nom des entêtes csv:
# timestamp,temperature_c,humidity_pct,co2_ppm,voc_ppb,radon_bq_m3,pm25_ug_m3,pressure_hpa
start = datetime(2026, 11, 9)


for i in range(288):  # 24h x 12 mesures/h
    # timedelta permet d'additionner/soustraire du temps/dates
    t = start + timedelta(minutes=5*i)

    angle = 2 * math.pi * i / 288

    # température (C)
    temperature = round(22 + 2 * math.sin(angle), 1)
    # humidite (%)
    humidite = round(46 - 4 * math.sin(angle), 1)
    # niveau de CO2 en partie par million (ppm)
    co2 = round(650 + 80 * math.sin(angle + 1) + random.randint(-10, 10))
    # niveau de COV en partie par milliard (ppb)
    tvoc = round(120 + 25 * math.sin(angle + 1) + random.randint(-5, 5))
    # Radon (Bq/m3)
    radon = round(12 + 3 * math.sin(angle / 2), 1)
    # Particules dans l'air <= 2.5 micromètres (ug/m3)
    pm25 = round(4 + random.uniform(0, 2), 1)
    # pression atmosphérique en hectopascal (hPa)
    pression = round(1013 + 2 * math.sin(angle / 3), 1)

    # Le format des lignes à persister dans le csv
    print(
        f"{t:%Y-%m-%dT%H:%M:%SZ},"
        f"{temperature},{humidite},{co2},{tvoc},"
        f"{radon},{pm25},{pression}"
    )
