import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import time
import random

class AlgorithmVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Algorithm Visualizer")
        master.geometry("900x700")
        self.create_menu()
        self.create_main_frame()
        self.delay = 100  # Animation delay in milliseconds
        self.selected_algorithm = None

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.confirm_exit)
    
        # Algorithm menu
        algorithm_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Algorithms", menu=algorithm_menu)

        # Arrays and Strings submenu
        arrays_strings_menu = tk.Menu(algorithm_menu, tearoff=0)
        algorithm_menu.add_cascade(label="Arrays and Strings", menu=arrays_strings_menu)
        arrays_strings_menu.add_command(label="Array Reversal", command=lambda: self.select_algorithm("Array Reversal"))
        arrays_strings_menu.add_command(label="Array Rotation", command=lambda: self.select_algorithm("Array Rotation"))
        arrays_strings_menu.add_command(label="String Palindrome", command=lambda: self.select_algorithm("String Palindrome"))
        arrays_strings_menu.add_command(label="Substring Search", command=lambda: self.select_algorithm("Substring Search"))

        # Sorting submenu
        sorting_menu = tk.Menu(algorithm_menu, tearoff=0)
        algorithm_menu.add_cascade(label="Sorting", menu=sorting_menu)
        sorting_menu.add_command(label="Selection Sort", command=lambda: self.select_algorithm("Selection Sort"))
        sorting_menu.add_command(label="Bubble Sort", command=lambda: self.select_algorithm("Bubble Sort"))
        sorting_menu.add_command(label="Insertion Sort", command=lambda: self.select_algorithm("Insertion Sort"))
        sorting_menu.add_command(label="Merge Sort", command=lambda: self.select_algorithm("Merge Sort"))
        sorting_menu.add_command(label="Quick Sort", command=lambda: self.select_algorithm("Quick Sort"))
        sorting_menu.add_command(label="Heap Sort", command=lambda: self.select_algorithm("Heap Sort"))

        #searching submenu
        searching_menu = tk.Menu(algorithm_menu, tearoff=0)
        algorithm_menu.add_cascade(label="Searching", menu=searching_menu)
        searching_menu.add_command(label="Linear Search", command=lambda: self.select_algorithm("Linear Search"))
        searching_menu.add_command(label="Binary Search", command=lambda: self.select_algorithm("Binary Search"))
        searching_menu.add_command(label="Two Pointer Search", command=lambda: self.select_algorithm("Two Pointer Search"))
        searching_menu.add_command(label="Fibonacci Search", command=lambda: self.select_algorithm("Fibonacci Search"))

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.quit()
    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(self.main_frame, text="Welcome to Algorithm Visualizer", font=("Arial", 18))
        self.label.pack(pady=10)

        self.algorithm_label = ttk.Label(self.main_frame, text="No algorithm selected", font=("Arial", 14))
        self.algorithm_label.pack(pady=5)

        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(pady=10)

        self.example_label = ttk.Label(self.input_frame, text="", font=("Arial", 12))
        self.example_label.pack(pady=5)

        self.input_entry = ttk.Entry(self.input_frame, width=50)
        self.input_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.start_button = ttk.Button(self.input_frame, text="Visualize", command=self.start_visualization, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT)

        self.error_label = ttk.Label(self.main_frame, text="", foreground="red", font=("Arial", 12))
        self.error_label.pack(pady=5)

        self.canvas = tk.Canvas(self.main_frame, width=800, height=400, bg='white')
        self.canvas.pack(pady=10)

    def select_algorithm(self, algorithm):
        self.selected_algorithm = algorithm
        self.algorithm_label.config(text=f"Selected Algorithm: {algorithm}")
        self.start_button.config(state=tk.NORMAL)
        self.input_entry.delete(0, tk.END)
        self.error_label.config(text="")
        self.canvas.delete("all")

        if algorithm in ["Array Reversal", "Array Rotation"] + ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]:
            self.example_label.config(text="Example input: 5,2,8,12,1,6")
        elif algorithm == "String Palindrome":
            self.example_label.config(text="Example input: racecar")
        elif algorithm == "Substring Search":
            self.example_label.config(text="Example input: hello world")
        if algorithm in ["Linear Search", "Binary Search", "Two Pointer Search", "Fibonacci Search"]:
            self.example_label.config(text="Example input: 5,2,8,12,1,6 (comma-separated list)")

    def start_visualization(self):
        self.error_label.config(text="")
        self.canvas.delete("all")

        if self.selected_algorithm in ["Array Reversal", "Array Rotation"] + ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]:
            try:
                array = [int(x.strip()) for x in self.input_entry.get().split(',')]
                self.visualize_array_algorithm(array)
            except ValueError:
                self.error_label.config(text="Invalid input. Please enter comma-separated integers.")
        elif self.selected_algorithm in ["String Palindrome", "Substring Search"]:
            string = self.input_entry.get()
            if not string:
                self.error_label.config(text="Please enter a string.")
            else:
                self.visualize_string_algorithm(string)
        elif self.selected_algorithm in ["Linear Search", "Binary Search", "Two Pointer Search", "Fibonacci Search"]:
            try:
                array = [int(x.strip()) for x in self.input_entry.get().split(',')]
                target = simpledialog.askinteger("Input", "Enter the target value to search:", parent=self.master)
                if target is not None:
                    self.visualize_search_algorithm(array, target)
                else:
                    self.error_label.config(text="Target value is required.")
            except ValueError:
                self.error_label.config(text="Invalid input. Please enter comma-separated integers.")

    def visualize_array_algorithm(self, array):
        if self.selected_algorithm == "Array Reversal":
            self.visualize_array_reversal(array)
        elif self.selected_algorithm == "Array Rotation":
            rotation_amount = simpledialog.askinteger("Input", "Enter rotation amount:", parent=self.master)
            if rotation_amount is not None:
                self.visualize_array_rotation(array, rotation_amount)
            else:
                self.error_label.config(text="Rotation amount is required.")
        elif self.selected_algorithm in ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort"]:
            self.visualize_sorting(array)


    def visualize_string_algorithm(self, string):
        if self.selected_algorithm == "String Palindrome":
            self.visualize_string_palindrome(string)
        elif self.selected_algorithm == "Substring Search":
            substring = simpledialog.askstring("Input", "Enter substring to search:", parent=self.master)
            if substring:
                self.visualize_substring_search(string, substring)
            else:
                self.error_label.config(text="Substring is required.")

    def visualize_array_reversal(self, array):
        self.draw_array_operation(array, "Original Array", y_offset=-100)
        reversed_array = array[::-1]
        self.canvas.after(1000, lambda: self.draw_array_operation(reversed_array, "Reversed Array", y_offset=100))
        self.canvas.after(1000, lambda: self.draw_result("Array Reversed"))
    def visualize_array_rotation(self, array, k):
        self.draw_array_operation(array, "Original Array", y_offset=-100)
        n = len(array)
        k = k % n  # Normalize k
        rotated_array = array[-k:] + array[:-k]  # Fix the rotation calculation
        self.canvas.after(1000, lambda: self.draw_array_operation(rotated_array, f"Rotated Array (by {k})", y_offset=100))
        self.canvas.after(1000, lambda: self.draw_result(f"Array Rotated by {k}"))

    def visualize_string_palindrome(self, string):
        self.draw_string(string, "Input String", y_offset=50)
        reversed_string = string[::-1]
        is_palindrome = string.lower() == reversed_string.lower()
        color = "green" if is_palindrome else "red"
        self.canvas.after(1000, lambda: self.draw_string(reversed_string, "Reversed String", y_offset=150, color=color))
        result = "Palindrome" if is_palindrome else "Not a Palindrome"
        self.canvas.after(2000, lambda: self.draw_result(result))

    def visualize_substring_search(self, string, substring):
        self.draw_string(string, "Main String", y_offset=50)
        self.draw_string(substring, "Substring", y_offset=150)
        index = string.find(substring)
        if index != -1:
            self.canvas.after(1000, lambda: self.highlight_substring(string, substring, index))
        else:
            self.canvas.after(1000, lambda: self.draw_result("Substring not found"))
    def draw_string(self, string, label, y_offset=50, color="lightgreen"):
        self.canvas.create_text(400, y_offset - 30, text=label, font=("Arial", 16))
        for i, char in enumerate(string):
            x = 50 + i * 30
            self.canvas.create_rectangle(x, y_offset, x + 25, y_offset + 40, fill=color)
            self.canvas.create_text(x + 12, y_offset + 20, text=char)

    def draw_result(self, result):
        self.canvas.create_text(400, 350, text=result, font=("Arial", 20), fill="blue")
    def highlight_substring(self, string, substring, index):
        for i in range(len(substring)):
            x = 50 + (index + i) * 30
            self.canvas.create_rectangle(x, 50, x + 25, 90, fill="yellow")
        self.canvas.create_text(400, 350, text=f"Substring found at index {index}", font=("Arial", 16), fill="green")

    def visualize_sorting(self, array):
        self.array = array
        self.draw_array(self.array, self.selected_algorithm)
        self.master.update()
        time.sleep(1)  # Pause to show the initial array

        if self.selected_algorithm == "Selection Sort":
            self.selection_sort()
        elif self.selected_algorithm == "Bubble Sort":
            self.bubble_sort()
        elif self.selected_algorithm == "Insertion Sort":
            self.insertion_sort()
        elif self.selected_algorithm == "Merge Sort":
            self.merge_sort(0, len(self.array) - 1)
        elif self.selected_algorithm == "Quick Sort":
            self.quick_sort(0, len(self.array) - 1)
        elif self.selected_algorithm == "Heap Sort":
            self.heap_sort()

        self.draw_array(self.array, f"{self.selected_algorithm} - Sorted", color="lightgreen")

    def selection_sort(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array(self.array, self.selected_algorithm, [i, min_idx])
            self.master.update()
            time.sleep(self.delay / 1000)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw_array(self.array, self.selected_algorithm, [j, j+1])
                    self.master.update()
                    time.sleep(self.delay / 1000)
    
    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j+1] = self.array[j]
                j -= 1
                self.draw_array(self.array, self.selected_algorithm, [j, j+1])
                self.master.update()
                time.sleep(self.delay / 1000)
            self.array[j+1] = key
            self.draw_array(self.array, self.selected_algorithm, [j+1])
            self.master.update()
            time.sleep(self.delay / 1000)

    def merge_sort(self, l, r):
        if l < r:
            m = (l + r) // 2
            self.merge_sort(l, m)
            self.merge_sort(m+1, r)
            self.merge(l, m, r)

    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [self.array[l + i] for i in range(n1)]
        R = [self.array[m + 1 + i] for i in range(n2)]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1
            self.draw_array(self.array, self.selected_algorithm, [k])
            self.master.update()
            time.sleep(self.delay / 1000)
        while i < n1:
            self.array[k] = L[i]
            i += 1
            k += 1
            self.draw_array(self.array, self.selected_algorithm, [k])
            self.master.update()
            time.sleep(self.delay / 1000)
        while j < n2:
            self.array[k] = R[j]
            j += 1
            k += 1
            self.draw_array(self.array, self.selected_algorithm, [k])
            self.master.update()
            time.sleep(self.delay / 1000)

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def partition(self, low, high):
        i = low - 1
        pivot = self.array[high]
        for j in range(low, high):
            if self.array[j] <= pivot:
                i = i + 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.draw_array(self.array, self.selected_algorithm, [i, j])
                self.master.update()
                time.sleep(self.delay / 1000)
        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        self.draw_array(self.array, self.selected_algorithm, [i+1, high])
        self.master.update()
        time.sleep(self.delay / 1000)
        return i + 1

    def heap_sort(self):
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.draw_array(self.array, self.selected_algorithm, [i, 0])
            self.master.update()
            time.sleep(self.delay / 1000)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.array[i] < self.array[l]:
            largest = l
        if r < n and self.array[largest] < self.array[r]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.draw_array(self.array, self.selected_algorithm, [i, largest])
            self.master.update()
            time.sleep(self.delay / 1000)
            self.heapify(n, largest)
    
    def visualize_search_algorithm(self, array, target):
        if self.selected_algorithm == "Linear Search":
            self.visualize_linear_search(array, target)
        elif self.selected_algorithm == "Binary Search":
            self.visualize_binary_search(sorted(array), target)
        elif self.selected_algorithm == "Two Pointer Search":
            self.visualize_two_pointer_search(sorted(array), target)
        elif self.selected_algorithm == "Fibonacci Search":
            self.visualize_fibonacci_search(sorted(array), target)

    def visualize_linear_search(self, array, target):
        self.draw_array_operation(array, "Linear Search", y_offset=0)
        for i in range(len(array)):
            self.canvas.after(self.delay, lambda i=i: self.draw_array_operation(array, "Linear Search", highlighted=[i], y_offset=0))
            self.master.update()
            time.sleep(self.delay / 1000)
            if array[i] == target:
                self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} found at index {i}"))
                return
        self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} not found"))

    def visualize_binary_search(self, array, target):
        self.draw_array_operation(array, "Binary Search", y_offset=0)
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            self.canvas.after(self.delay, lambda l=left, m=mid, r=right: self.draw_array_operation(array, "Binary Search", highlighted=[l, m, r], y_offset=0))
            self.master.update()
            time.sleep(self.delay / 1000)
            if array[mid] == target:
                self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} found at index {mid}"))
                return
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} not found"))

    def visualize_two_pointer_search(self, array, target):
        self.draw_array_operation(array, "Two Pointer Search", y_offset=0)
        left, right = 0, len(array) - 1
        while left <= right:
            self.canvas.after(self.delay, lambda l=left, r=right: self.draw_array_operation(array, "Two Pointer Search", highlighted=[l, r], y_offset=0))
            self.master.update()
            time.sleep(self.delay / 1000)
            if array[left] + array[right] == target:
                self.canvas.after(self.delay, lambda: self.draw_result(f"Pair found: {array[left]} + {array[right]} = {target}"))
                return
            elif array[left] + array[right] < target:
                left += 1
            else:
                right -= 1
        self.canvas.after(self.delay, lambda: self.draw_result(f"No pair found that sums to {target}"))

    def visualize_fibonacci_search(self, array, target):
        self.draw_array_operation(array, "Fibonacci Search", y_offset=0)
        n = len(array)
        fib2 = 0
        fib1 = 1
        fib = fib1 + fib2
        while fib < n:
            fib2 = fib1
            fib1 = fib
            fib = fib1 + fib2
        offset = -1
        while fib > 1:
            i = min(offset + fib2, n - 1)
            self.canvas.after(self.delay, lambda i=i: self.draw_array_operation(array, "Fibonacci Search", highlighted=[i], y_offset=0))
            self.master.update()
            time.sleep(self.delay / 1000)
            if array[i] < target:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                offset = i
            elif array[i] > target:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else:
                self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} found at index {i}"))
                return
        if fib1 and array[offset + 1] == target:
            self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} found at index {offset + 1}"))
        else:
            self.canvas.after(self.delay, lambda: self.draw_result(f"Target {target} not found"))

    def draw_array_operation(self, array, label, highlighted=None, color="lightblue", y_offset=0):
        self.canvas.delete("all")
        self.canvas.create_text(400, 20 + y_offset, text=label, font=("Arial", 16))
        existing_items = self.canvas.find_all()
        # Calculate dimensions
        box_size = min(50, 700 // len(array))
        x_start = (800 - len(array) * box_size) // 2
        y_start = 200 + y_offset
        self.canvas.create_text(400, 20 + y_offset, text=label, font=("Arial", 16))
        for i, value in enumerate(array):
            x = x_start + i * box_size
            
            fill_color = "yellow" if highlighted and i in highlighted else color
            
            # Draw the box
            self.canvas.create_rectangle(x, y_start, x + box_size, y_start + box_size, fill=fill_color, outline="black")
            
            # Draw the value inside the box
            self.canvas.create_text(x + box_size // 2, y_start + box_size // 2, text=str(value), font=("Arial", 12))

        # Draw array indices
        for i in range(len(array)):
            x = x_start + i * box_size
            self.canvas.create_text(x + box_size // 2, y_start + box_size + 20, text=str(i), font=("Arial", 10))
        for item in existing_items:
            self.canvas.tag_raise(item)

    def draw_array(self, array, label, highlighted=None, color="lightblue", y_offset=0):
    

        self.canvas.delete("all")
        self.canvas.create_text(400, 20 + y_offset, text=label, font=("Arial", 16))
        max_height = 300
        bar_width = min(30, 700 // len(array))
        x_start = (800 - len(array) * bar_width) // 2

        # Find the minimum and maximum values in the array
        min_value = min(array)
        max_value = max(array)
        value_range = max_value - min_value

        for i, value in enumerate(array):
            x = x_start + i * bar_width
            
            # Normalize the height to handle negative numbers
            normalized_height = ((value - min_value) / value_range) if value_range != 0 else 0.5
            height = normalized_height * max_height

            fill_color = "red" if highlighted and i in highlighted else color
            
            # Draw the bar
            self.canvas.create_rectangle(x, 400 + y_offset - height, x + bar_width - 1, 400 + y_offset, fill=fill_color)
            
            # Draw the value at the top of the bar with a slight offset based on the index
            text_y = 395 + y_offset - height - (i % 3) * 10  # Offset text vertically
            self.canvas.create_text(x + bar_width // 2, text_y, text=str(value), font=("Arial", 8), anchor="s", fill="black")

        # Draw the x-axis
        self.canvas.create_line(x_start, 400 + y_offset, x_start + len(array) * bar_width, 400 + y_offset, fill="black")





if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()
