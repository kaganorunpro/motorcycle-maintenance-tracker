print("🏍️ Motorcycle Maintenance Tracker")

current_km = int(input("Current Motorcycle KM: "))
last_oil_change = int(input("Last Oil Change KM: "))
last_chain_maintenance = int(input("Last Chain Maintenance KM: "))
last_tire_check = int(input("Last Tire Check KM: "))

oil_interval = 3000
chain_interval = 1000
tire_interval = 2000

oil_km = current_km - last_oil_change
chain_km = current_km - last_chain_maintenance
tire_km = current_km - last_tire_check

print("\n----- MAINTENANCE REPORT -----")

if oil_km >= oil_interval:
    print("Oil Change: REQUIRED ❌")
else:
    print(f"Oil Change: OK ✅ ({oil_interval - oil_km} km remaining)")

if chain_km >= chain_interval:
    print("Chain Maintenance: REQUIRED ❌")
else:
    print(f"Chain Maintenance: OK ✅ ({chain_interval - chain_km} km remaining)")

if tire_km >= tire_interval:
    print("Tire Check: REQUIRED ❌")
else:
    print(f"Tire Check: OK ✅ ({tire_interval - tire_km} km remaining)")

print("\nRide safe! 🏍️")