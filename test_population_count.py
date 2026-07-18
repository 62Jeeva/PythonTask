from Task16pages.population_homepage import Population_homepage

def test_population_homepage(driver):
    population = Population_homepage(driver)
    population.open_url("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
    print("\n Press CTRL +C to stop the count \n")

    previous = ""

    try:
        while True:

            current = population.get_population().strip()

            if current != previous:
                print("World Population :", current)
                previous = current

    except KeyboardInterrupt:
        print("\n Stopped by user")