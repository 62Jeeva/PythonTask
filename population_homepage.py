from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Task16pages.basepagetask16 import Basepage

class Population_homepage(Basepage):


    POPULATION = (By.XPATH,"//div[@class='counter-ticker is-size-2-mobile']")

    def get_population(self):
        population_count = self.wait.until(EC.visibility_of_element_located(self.POPULATION))
        return population_count.text