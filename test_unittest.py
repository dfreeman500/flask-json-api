from flask_app import (
    list_of_recipe_names,
    get_recipes,
    get_recipe,
    post_recipes,
    edit_recipe,
)
import unittest


class Test_Flask_App(unittest.TestCase):
    def test_list_of_recipe_names(self):
        expected_result = ["scrambledEggs", "garlicPasta", "chai"]
        self.assertEqual(list_of_recipe_names(), expected_result)

    def test_get_recipes(self):
        expected_result = {"recipeNames": ["scrambledEggs", "garlicPasta", "chai"]}, 200
        self.assertEqual(get_recipes(), expected_result)

    def test_get_recipe(self):
        expected_result = {
            "details": {
                "ingredients": [
                    "500mL water",
                    "100g spaghetti",
                    "25mL olive oil",
                    "4 cloves garlic",
                    "Salt",
                ],
                "numSteps": 5,
            }
        }, 200

        self.assertEqual(get_recipe("garlicPasta"), expected_result)

    def test_post_recipes(self):
        # needs to access request.json
        pass

    def test_edit_recipes(self):
        expected_result = {"error": "Recipe does not exist"}, 404
        self.assertEqual(edit_recipe(), expected_result)


if __name__ == "__main__":
    unittest.main()
