#!/usr/bin/python3
import sys
import antigravity

def gera_geohash():
    try:
        if len(sys.argv) < 3:
            print("Necessário 3 agurmentos (latitude, longitude, datedow)")
            return
        
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3].encode('utf-8')
        
        antigravity.geohash(latitude, longitude, datedow)

    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    gera_geohash()


    # python3 geohashing.py -23.5489 -46.6388 10458.68
    # python geohashing.py -23.5489 -46.6388 10458.68