def city_country(city, country, population=""):
    if population != "":
        return f"{city},{country} - population {population}"
    else:
        return f"{city},{country}"
