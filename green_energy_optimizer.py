def calculate_emission(energy_kwh, source):
    factors = {
        "coal": 0.91,
        "natural_gas": 0.45,
        "solar": 0.05,
        "wind": 0.02,
        "hydro": 0.03
    }
    return energy_kwh * factors.get(source.lower(), 0.91)

def suggest_alternative(source):
    if source == "coal":
        return "Switch to solar or wind — they produce 95% less CO₂ emissions."
    elif source == "natural_gas":
        return "Consider using hydro or wind energy for lower emissions."
    else:
        return "Great choice! Keep using clean energy."

def estimate_savings(current_source, energy_kwh):
    emission_current = calculate_emission(energy_kwh, current_source)
    emission_green = calculate_emission(energy_kwh, "solar")
    reduction = emission_current - emission_green
    saving_percent = (reduction / emission_current) * 100 if emission_current else 0
    return reduction, saving_percent

def main():
    print("🔋 Energy Sustainability Optimizer 🔋")
    print("------------------------------------")
    energy_kwh = float(input("Enter monthly energy consumption (in kWh): "))
    source = input("Enter your current energy source (coal, natural_gas, solar, wind, hydro): ").lower()
    
    emission = calculate_emission(energy_kwh, source)
    print(f"\nEstimated monthly CO₂ emissions: {emission:.2f} kg")
    
    print(suggest_alternative(source))
    
    reduction, saving_percent = estimate_savings(source, energy_kwh)
    print(f"If you switch to solar, you could reduce emissions by {reduction:.2f} kg ({saving_percent:.1f}% less CO₂).")
    
    yearly_reduction = reduction * 12
    print(f"Yearly CO₂ reduction potential: {yearly_reduction:.2f} kg\n")
    print("🌍 Every small step counts toward a greener planet!")

if __name__ == "__main__":
    main()
