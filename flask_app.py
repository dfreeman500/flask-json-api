import webbrowser
from flask import Flask
import json

from matplotlib.font_manager import json_dump

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

    return {"recipeNames": list_of_recipe_names()}
    

@app.route('/recipes/details/<recipe>',methods=['GET'])
def get_recipe(recipe):    
    index = list_of_recipe_names().index(recipe)
    print(index)
    return {"details": { "ingredients": data['recipes'][index]["ingredients"], "numSteps": len(data['recipes'][index]["instructions"])}}
    
    return "Response body (JSON): {} Status: 200"



if __name__ == "__main__":
    pass
    # webbrowser.open("http://localhost:5000/")

app.run(debug=True,use_reloader=False)