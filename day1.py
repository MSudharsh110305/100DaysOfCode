import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_input(prompt):
    user_input = input(prompt).strip()
    if not user_input:
        raise ValueError("Input cannot be empty.")
    return user_input.title()

def validate_city_name(city_name):
    if not re.match(r"^[a-zA-Z\s]+$", city_name):
        raise ValueError("City name must contain only letters and spaces.")
    return city_name

def validate_pet_name(pet_name):
    if not re.match(r"^[a-zA-Z\s]+$", pet_name):
        raise ValueError("Pet name must contain only letters and spaces.")
    return pet_name

def generate_band_name(city, pet):
    return f"{city} {pet}"

def main():
    try:
        logging.info("Welcome to the Advanced Band Name Generator.")
        
        city = get_input("What's the name of the city you grew up in?\n")
        validate_city_name(city)
        
        pet = get_input("What's your pet's name?\n")
        validate_pet_name(pet)
        
        band_name = generate_band_name(city, pet)
        print(f"Your band name could be {band_name}")
        logging.info(f"Generated band name: {band_name}")
    
    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
