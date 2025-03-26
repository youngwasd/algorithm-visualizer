# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "wats"

# if __name__ == '__main__':
#     app.run()

class Selection:
    def selectionSort(self, arr: list[int]) -> list[int]:
        index = 0
        
        for i in range(len(arr) - 1):
            index = i # set index to curr val
            for j in range(i + 1, len(arr)):
                if (arr[j] < arr[index]): # new val < min?
                    index = j # save index

            arr[i], arr[index] = arr[index], arr[i] # a, b = b, a or swaps min with first

        return arr

sol = Selection()
res = sol.selectionSort([64, 25, 12, 22, 11])

expected = [11, 12, 22, 25, 64]
print(f"PASS? {expected == res}")
print(f"RESULT: {res}\nEXPECTED: {expected}")