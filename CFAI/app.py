from flask import Flask, render_template, request
import time

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return sorted(left + right)

@app.route("/", methods=["GET","POST"])
def home():
    bubble_time = merge_time = None

    if request.method == "POST":
        nums = list(map(int, request.form["numbers"].split(",")))

        start = time.time()
        bubble_sort(nums.copy())
        bubble_time = time.time() - start

        start = time.time()
        merge_sort(nums.copy())
        merge_time = time.time() - start

    return render_template("index.html", bubble=bubble_time, merge=merge_time)

if __name__ == "__main__":
    app.run(debug=True)