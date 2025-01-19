from seleniumbase import BaseCase
import random
promp = "test"
class MyTestClass(BaseCase):
    def test_example(self):
        self.open("https://chatgpt.com")
        # Wait for the element with class name "placeholder"
        self.sleep(random.uniform(3, 8))
        # self.uc_gui_click_captcha()
        self.wait_for_element(".placeholder", timeout=10)
        # Send keys "test" to the element
        
        for char in promp:
            self.type(".placeholder", char)
            self.sleep(random.uniform(0.1, 0.3))
        self.sleep(random.uniform(1, 5))



if __name__ == "__main__":
    BaseCase.main(__name__, __file__ )
