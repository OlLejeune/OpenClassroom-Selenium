from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from Class.logger import Logger

logger = Logger()
class OpenClassRoomsActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def search_words(self, words) :
        try :
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-search"]/div/form/button[1]')))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
            search_button.click()
            logger.log("log-openclassrooms", f"Vous avez cliqué sur le bouton de recherche")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors du clique sur le bouton de recherche : {e}")

            
        time.sleep(2)  
        try:    
            
            search_field = self.wait.until(EC.element_to_be_clickable((By.ID, 'algolia-search-input')))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
            search_field.click()
            
            # Effacer le champ avant de taper pour éviter des problèmes de texte pré-rempli
            search_field.clear()
            search_field.send_keys(words)
            search_field.send_keys(Keys.ENTER)               
            logger.log("log-openclassrooms", f"Vous d'éffectuer la recherche sur le mots: {words}")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur la recherche a échoué : {e}")

    def selected_course(self):
        try: 
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainSearch"]/div/div/div/ul/li[3]/a/div/div/div/div')))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
            search_button.click()
                
            logger.log("log-openclassrooms", f"Vous avez selectionné le 3 ème élément de la liste de recherche")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors de la selectionnion du 3 ème élément de la liste de recherche : {e}")

    def show_tittle_course(self):
        try: 
            # Attendez que le titre du cours soit visible et récupérez-le
            course_title_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="path_details_screen"]/section[1]/div[1]/div/div[1]/div/h1'))
            )
            course_title = course_title_element.text  # Récupération du texte du titre
            logger.log("access-openclassrooms", f"Vous êtes sur le cours qui porte le titre : {course_title}")
            
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors de l'affichage du titre du cours : {e}")
