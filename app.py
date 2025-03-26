# ignore front end for now
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "wats"

# if __name__ == '__main__':
#     app.run()


# work on back end/console version first
class Selection:
    def selectionSort(self, arr: list[int]) -> list[int]:
        # algorithm go here

        return arr

sol = Selection()
res = sol.selectionSort([2, 5, 1, 10])

expected = [1, 2, 5, 10]
print(expected == res)
print(res, expected)