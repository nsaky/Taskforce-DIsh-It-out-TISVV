# Dish It Out - API Challenge [10 points]

## Task Description
Create a Flask API that returns random pictures of dishes. Your API should have at least one endpoint that, when called, responds with a random image of a dish.

## Requirements
1. Use Flask to create the API
2. Implement at least one endpoint that returns a random dish image
3. Handle potential errors gracefully
4. Include basic documentation for your API
5. Have at least 5 dishes

## Starter Code

```python
from flask import Flask, jsonify, send_file
import random
import os

app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'dishes'

@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        # Your code here: 
        # 1. Get a list of all image files in the DISHES_DIR
        # 2. Choose a random image from the list
        # 3. Return the image file
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## Getting Started
1. Install Flask: `pip install flask` - you should have Python installed already if you went through the [instructions](https://shriteq.org/task-force/instructions)
2. Create a directory called 'dishes' in the same directory as your Python file
3. Add some image files of dishes to the 'dishes' directory
4. Implement the `random_dish()` function
5. Run your Flask app: `python your_file_name.py`

## Tips
- Use `os.listdir()` to get a list of files in a directory
- Use `random.choice()` to select a random item from a list
- Use Flask's `send_file()` function to return image files

## Bonus Challenges
1. Add an endpoint that allows filtering dishes by type (e.g., /dish/dessert, /dish/main-course) [2 points]
2. Add an endpoint that returns a list of all available dishes [2 points]

## Learning Resources

### Flask Tutorials and Documentation
1. ⭐️ [Official Flask Documentation](https://flask.palletsprojects.com/)
2. [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
3. [Flask for Beginners](https://www.pythonforbeginners.com/flask/) - Python for Beginners
4. [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)

### RESTful API Design
1. [RESTful API Design: Best Practices](https://blog.restcase.com/restful-api-design-13-best-practices-to-make-your-users-happy/)
2. [Flask RESTful Documentation](https://flask-restful.readthedocs.io/en/latest/)

### Error Handling in Flask
1. [Flask Error Handling](https://flask.palletsprojects.com/en/2.0.x/errorhandling/)
2. [Better Error Handling for Flask](https://www.youtube.com/watch?v=lYqxU4z5sHE) - Pretty Printed (YouTube)

Remember to consult these resources if you get stuck or want to learn more about specific aspects of Flask and API development. Good luck, and happy coding!