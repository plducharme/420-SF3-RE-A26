from datetime import datetime, timedelta
import math
import random
import csv

# compléter/modifier le code pour créer 3 csv: "airdata-{date}.csv"
# Nom des entêtes csv:
# timestamp,temperature_c,humidity_pct,co2_ppm,voc_ppb,radon_bq_m3,pm25_ug_m3,pressure_hpa
dates = [datetime(2026, 11, 9), datetime(2026, 11, 8), datetime(2026, 11, 7)]


# timestamp,temperature_c,humidity_pct,co2_ppm,voc_ppb,radon_bq_m3,pm25_ug_m3,pressure_hpa

def creer_csv(date_debut: datetime):
    with open(f"airdata-{date_debut.year}-{date_debut.month}-{date_debut.day}.csv", mode="w", encoding="utf8", newline='') as fichier:
        entetes = ["timestamp", "temperature_c", "humidity_pct", "co2_ppm", "voc_ppb", "radon_bq_m3", "pm25_ug_m3",
                   "pressure_hpa"]
        csv_dict_writer = csv.DictWriter(fichier, entetes)
        csv_dict_writer.writeheader()

        start = date_debut
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

            data = {
                "timestamp": f"{t:%Y-%m-%dT%H:%M:%SZ}",
                "temperature_c": temperature,
                "humidity_pct": humidite,
                "co2_ppm": co2,
                "voc_ppb": tvoc,
                "radon_bq_m3": radon,
                "pm25_ug_m3": pm25,
                "pressure_hpa": pression
            }

            csv_dict_writer.writerow(data)


for d in dates:
    creer_csv(d)

