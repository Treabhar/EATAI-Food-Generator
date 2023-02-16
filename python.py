import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap



class MealPlanner(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.title_label = QLabel("Choose your Meal based on your preferences & Restrictions!")
        font = self.title_label.font()
        font.setBold(True)
        self.title_label.setFont(font)
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap('/home/networkarena/Desktop/icon.png'))
        self.vegetarian_cb = QCheckBox("Vegetarian")
        self.gluten_free_cb = QCheckBox("Gluten Free")
        self.warm_cb = QCheckBox("Warm")
        self.cold_cb = QCheckBox("Cold")
        self.breakfast_cb = QCheckBox("Breakfast")
        self.lunch_cb = QCheckBox("Lunch")
        self.dinner_cb = QCheckBox("Dinner")
        self.generate_btn = QPushButton("Generate Meal Plan")
        font = self.generate_btn.font()
        font.setBold(True)
        self.generate_btn.setFont(font)

        self.result_label = QLabel()
        font = self.result_label.font()
        font.setPointSize(20)
        self.result_label.setFont(font)

        # Create layout
        self.main_layout = QVBoxLayout()
                
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.title_label)

        self.restriction_layout = QGridLayout()
        self.restriction_layout.addWidget(self.vegetarian_cb, 0, 0)
        self.restriction_layout.addWidget(self.gluten_free_cb, 0, 1)
        self.main_layout.addLayout(self.restriction_layout)

        self.preference_layout = QGridLayout()
        self.preference_layout.addWidget(self.warm_cb, 0, 0)
        self.preference_layout.addWidget(self.cold_cb, 0, 1)
        self.preference_layout.addWidget(self.breakfast_cb, 1, 0)
        self.preference_layout.addWidget(self.lunch_cb, 1, 1)
        self.preference_layout.addWidget(self.dinner_cb, 2, 0)
        self.main_layout.addLayout(self.preference_layout)

        self.main_layout.addWidget(self.generate_btn)
        self.main_layout.addWidget(self.result_label)
        self.setLayout(self.main_layout)

        # Connect signal
        self.generate_btn.clicked.connect(self.generate_meal_plan)

    def generate_meal_plan(self):
        # Get the selected dietary restrictions
        restrictions = []
        if self.vegetarian_cb.isChecked():
            restrictions.append("vegetarian")
        if self.gluten_free_cb.isChecked():
            restrictions.append("gluten-free")

        # Get the selected meal preferences
        preferences = []
        if self.warm_cb.isChecked(): 
            preferences.append("warm")
        if self.cold_cb.isChecked():
            preferences.append("cold")
        if self.breakfast_cb.isChecked():
            preferences.append("breakfast")
        if self.lunch_cb.isChecked():
            preferences.append("lunch")
        if self.dinner_cb.isChecked():
            preferences.append("dinner")

        # Code to generate the meal plan based on restrictions and preferences goes here
        
        #  # Create list of meal options
        meal_options = []
        if "vegetarian" in restrictions:
            meal_options.extend(["Vegetable Curry with Quinoa and Chickpeas", "Vegetable Stir-Fry with Tofu and Brown Rice", "Veggie Sandwich with Grilled Portobello and Roasted Red Peppers", "Vegetable Lasagna with Spinach and Ricotta", "Veggie Burgers with Black Beans and Sweet Potato", "Spinach and Feta Stuffed Portobello Mushrooms with Quinoa Pilaf", "Vegetable Paella with Saffron and Chickpeas", "Vegetable and Tofu Pad Thai with Peanut Sauce", "Roasted Vegetable Quinoa Bowl with Avocado and Lime", "Vegetable and Lentil Shepherd's Pie with Sweet Potato Topping"])
        else:
            meal_options.extend(["Chicken Curry with Coconut Milk and Cashews", "Beef Stir-Fry with Snow Peas and Sesame Oil", "BLT Sandwich with Turkey Bacon and Heirloom Tomato", "Spaghetti Bolognese with Grass-Fed Beef and Organic Tomato Sauce", "Hamburgers with Grass-Fed Beef and Caramelized Onions", "Teriyaki Salmon with Sesame Seeds and Green Onion", "Beef and Broccoli Stir-Fry with Brown Rice and Sesame Oil", "Lemon Herb Chicken with Roasted Potatoes and Rosemary", "Pork Chops with Apple Compote and Quinoa Pilaf", "Beef and Vegetable Pot Roast with Carrots and Potatoes"])
        if "gluten-free" in restrictions:
            meal_options = [option for option in meal_options if "Sandwich" not in option and "Spaghetti" not in option and "Burgers" not in option and "Pot Roast" not in option]
        if "warm" in preferences:
            meal_options = [option for option in meal_options if "Stir-Fry" in option or "Curry" in option or "Roasted" in option or "Grilled" in option or "Pot Roast" in option or "Pad Thai" in option or "Paella" in option]
        if "cold" in preferences:
            meal_options = [option for option in meal_options if "Salad" in option or "Soup" in option or "Yogurt" in option or "Sandwich" in option or "Taco Salad" in option or "Cobb Salad" in option]
        if "breakfast" in preferences:
            meal_options.extend(["Scrambled Eggs with Spinach and Feta", "Yogurt and Granola with Fresh Berries", "Pancakes with Blueberries and Maple Syrup", "French Toast with Strawberries and Powdered Sugar", "Smoked Salmon and Cream Cheese Bagel", "Egg and Sausage Breakfast Burrito with Avocado and Salsa", "Crepes with Fresh Berries and Cream", "Hashbrowns and Sausage with Bell Peppers and Onions", "Biscuits and Gravy with Turkey Sausage"])
        if "lunch" in preferences:
            meal_options.extend(["Soup and Sandwich", "Salad", "Taco Salad", "Cobb Salad", "Grilled Chicken Caesar Salad", "Veggie Wrap", "Tuna Salad Sandwich", "Turkey and Avocado Club Sandwich", "Roasted Vegetable and Pesto Panini"])
        if "dinner" in preferences:
            meal_options.extend(["Grilled Fish with Lemon and Herb Butter", "Steak with Mushroom and Onion Compote", "Grilled Chicken with Garlic and Rosemary", "Lamb Chops with mint and yogurt sauce"])
            


        # Select a random meal option
        import random
        meal = random.choice(meal_options)

        # Display the generated meal plan
        self.result_label.setText("Meal Plan: " + meal)
        
        
class StartPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap('/home/networkarena/Desktop/icon.png'))
        self.icon_label.setScaledContents(True)
        self.icon_label.setFixedSize(300,300)

        self.start_button = QPushButton("Start Now!")
        self.start_button.clicked.connect(self.open_mealplanner_window)

        text_label = QLabel("Welcome to EatAI! Discover your Food Buddy.")

        button_layout = QVBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.start_button)
        button_layout.addStretch()

        icon_layout = QVBoxLayout()
        icon_layout.addStretch()
        icon_layout.addWidget(self.icon_label)
        icon_layout.addStretch()

        text_layout = QVBoxLayout()
        text_layout.addStretch()
        text_layout.addWidget(text_label)
        text_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(icon_layout)
        main_layout.addLayout(text_layout)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)
        self.setLayout(main_layout)
        
    def open_mealplanner_window(self):
        self.mealplanner_window = MealPlanner()
        self.mealplanner_window.resize(400, 100)
        self.mealplanner_window.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('/home/networkarena/Desktop/icon.png'))
    start_page = StartPage()
    start_page.setGeometry(100, 100, 200, 200)
    start_page.show()
    sys.exit(app.exec_())
        

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    meal_planner = MealPlanner()
    meal_planner.show()
    sys.exit(app.exec_())
