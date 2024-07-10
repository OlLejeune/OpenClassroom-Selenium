import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wcag_contrast_ratio import contrast
from Class.logger import Logger
import time

logger = Logger()

class ButtonVisibilityChecker:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def hex_to_rgb(hex_color):
        """ Converts hex color format to an RGB tuple. """
        hex_color = str(hex_color).lstrip('#')
        lv = len(hex_color)
        rgb =  tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        logger.log("log-contrast-color", f"La couleur en hexadecimal de {hex_color} vaux en rgb :  {rgb}")
        
        return rgb
    
    def fetch_search_button_colors(self):
        time.sleep(5)
        try:
            # Ciblage du bouton par CSS Selector
            button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.main-header-14-main-header33.main-header-14-main-header35')))

            # Ciblage du SVG à l'intérieur du bouton par CSS Selector
            button_svg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.main-header-14-main-header33.main-header-14-main-header35 svg')))

            background_color = button.value_of_css_property('background-color') or "#FFF"
            text_color = button_svg.value_of_css_property('color') or "#FFF"

            # Convert HEX colors to RGB tuples
            background_color_rgb = self.hex_to_rgb(background_color) 
            text_color_rgb = self.hex_to_rgb(text_color)

            logger.log("log-contrast-color", f"Les couleurs récupérées sont : {background_color_rgb}, {text_color_rgb}")
            return [background_color_rgb, text_color_rgb]
        
        except Exception as e:
            logger.log("error-contrast-color", f"Impossible de récupérer la couleur des éléments: {e}")
            self.driver.save_screenshot('debug_screenshot.png')
            return [(0, 0, 0), (0, 0, 0)]  # Default to black if any errors
    
    def check_contrast(self):
        colors = self.fetch_search_button_colors()
        ratio = contrast.rgb(colors[0], colors[1])
        
        logger.log("log-contrast-color", f"Le ratio de contraste entre les deux couleurs est de : {ratio}")
        if ratio > 0.45 :
            logger.log("log-contrast-color", f"Le  contraste entre les deux couleurs est bon")
        else:
            logger.log("error-contrast-color", f"Le  contraste entre les deux couleurs n'est pas bon bon")
            
        
        
