import webbrowser
from flask import Flask
import json

with open('data.json') as data:
   data = json.load(data)

app = Flask(__name__)

def list_of_recipe_names():
    recipe_names=[]
    for i in range(0,len(data['recipes'])):
        recipe_names.append(data['recipes'][i]['name'])
    return recipe_names

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/recipes',methods=['GET'])
def get_recipes():
    return {"recipeNames": list_of_recipe_names()}, 200


@app.route('/recipes/details/<recipe>',methods=['GET'])
def get_recipe(recipe):
    try:    
        index = list_of_recipe_names().index(recipe)
        print(index)
        return {"details": { "ingredients": data['recipes'][index]["ingredients"], "numSteps": len(data['recipes'][index]["instructions"])}}, 200
    except:
        return {}, 200



@app.route('/recipes',methods=['POST'])
def post_recipes():
    if request.json["name"] in list_of_recipe_names():
        return {"error": "Recipe already exists" }, 400
    data['recipes'].append(request.json)
    return "", 201
    

@app.route('/recipes',methods=['PUT'])
def edit_recipe():
    try:
        index = list_of_recipe_names().index(request.json["name"])
        data["recipes"][index] = request.json
        return "", 204
    except:
        return {"error": "Recipe does not exist" }, 404
   

if __name__ == "__main__":
    pass
    # webbrowser.open("http://localhost:5000/")

app.run(debug=True,use_reloader=False)