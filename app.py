from flask import Flask, jsonify, send_file
import random
import os

app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = r"C:\Users\KAYENAT EQBAL\OneDrive\Desktop\Task Force\dish-it-out\dishes"

if not os.path.exists(DISHES_DIR):
    os.makedirs(DISHES_DIR)

@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        dish_images=os.listdir(DISHES_DIR)

        random_image=random.choice(dish_images)

        return send_file(os.path.join(DISHES_DIR,random_image), mimetype='image/jpg')
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/dish/<dish_type>', methods=['GET'])
def dish_by_type(dish_type):
    try:
        dish_types={
            "dessert":["ladoo.jpg","brownie.jpg","las.jpg","cheesecake.jpg"],
            "main-course":["biryani.jpg","egg.jpg"]
        }
        if dish_types not in dish_types:
            return jsonify({"error": "Invalid dish type"}), 404
        
        random_image=random.choice(dish_type[dish_type])

        return send_file(os.path.join(DISHES_DIR,random_image), mimetype='image/jpg')
    
    except Exception as e:
        return jsonify({"error":"Something went wrong:"+str(e)}), 500
    

@app.route('/dishes', methods=['GET'])
def list_dishes():
    try:
        dish_images=os.listdir(DISHES_DIR)
        if len(dish_images)==0:
            return jsonify({"error": "No dishes Available"}), 404
        return jsonify({"dishes":dish_images})
    except Exception as e:
        return jsonify({"error":"Something went wrong:"+str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)