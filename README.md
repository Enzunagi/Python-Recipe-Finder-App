
# **Recipe Finder using Edamam API**  

## **Project Overview**  
Recipe Finder is a Python-based application that enables users to search for recipes and fetch nutritional information using the Edamam Recipe and Nutrition APIs. The program allows users to search recipes by ingredients, filter them by dietary restrictions, and optionally view nutritional data for individual ingredients.  

---

## **Features**  
- Search for recipes by specifying up to three ingredients.  
- Filter recipes based on various dietary restrictions, including vegetarian, gluten-free, peanut-free, vegan, and more.  
- Fetch and display detailed nutritional information for individual ingredients.  
- Export recipe search results to a CSV file (`recipes.csv`).  

---

## **Prerequisites**  

### **Install Dependencies**  
1. Python 3.x  
2. `requests` library for making API calls:  
   ```bash
   pip install requests
   ```  
3. `python-dotenv` for environment variable management:  
   ```bash
   pip install python-dotenv
   ```

### **Environment Setup**  
Create a `.env` file in the root directory with the following content:  
```bash
APP_ID=your_edamam_recipe_app_id
APP_KEY=your_edamam_recipe_app_key
NUTRIENT_ID=your_edamam_nutrition_app_id
NUTRIENT_KEY=your_edamam_nutrition_app_key
```
Replace the placeholders (`your_edamam_recipe_app_id`, etc.) with your actual API credentials obtained from the [Edamam Developer Portal](https://developer.edamam.com/).  

---

## **How to Run the Program**  
1. Clone or download the project files.  
2. Run the script:  
   ```bash
   python recipe_finder.py
   ```  

---

## **Usage Instructions**  
1. Enter the primary ingredient for your recipe search.  
2. Optionally, choose up to two additional ingredients.  
3. You will be asked whether you want nutritional information for each ingredient.  
4. Choose whether you have any dietary restrictions from the available list.  
5. Recipes matching your ingredients and dietary criteria will be displayed along with URLs.  
6. Search results are exported to a `recipes.csv` file in the project directory.  

---

## **Dietary Restrictions Supported**  
- `alcohol-free`  
- `dairy-free`  
- `gluten-free`  
- `kosher`  
- `peanut-free`  
- `pork-free`  
- `shellfish-free`  
- `vegan`  
- `vegetarian`  

---

## **Sample Nutritional Output**  
If you opt to view the nutritional information for an ingredient, you will receive a JSON-like output containing calorie information, total fat, protein, and other nutritional details.

---

## **Potential Improvements**  
- Enhanced error handling for API requests and user inputs.  
- GUI implementation using `tkinter` for a better user experience.  
- Pagination for recipe results to handle large datasets.  
- More robust CSV data storage with complete nutritional information.  

