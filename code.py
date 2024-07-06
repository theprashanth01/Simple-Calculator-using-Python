import tkinter as tk

def button_click(number):
  current = tx1.get("1.0", tk.END) 
  tx1.delete("1.0", tk.END) 
  tx1.insert("1.0", str(current) + str(number))  # Insert the new text at the beginn

def button_clear():
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end

def button_add():
  first_number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  global f_num
  global math
  math = "addition"
  f_num = float(first_number)  # Convert the text to a float
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end

def button_sub():
  first_number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  global f_num
  global math
  math = "subtraction"
  f_num = float(first_number)  # Convert the text to a float
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end

def button_mul():
  first_number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  global f_num
  global math
  math = "multiplication"
  f_num = float(first_number)  # Convert the text to a float
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end

def button_div():
  first_number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  global f_num
  global math
  math = "division"
  f_num = float(first_number)  # Convert the text to a float
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end

def button_equal():
  second_number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end
  if math == "addition":
      tx1.insert("1.0", f_num + float(second_number))  # Insert the result at the beginning
  elif math == "subtraction":
      tx1.insert("1.0", f_num - float(second_number))  # Insert the result at the beginning
  elif math == "multiplication":
      tx1.insert("1.0", f_num * float(second_number))  # Insert the result at the beginning
  elif math == "division":
      tx1.insert("1.0", f_num / float(second_number))  # Insert the result at the beginning

def button_per():
  number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end
  tx1.insert("1.0", float(number) / 100)  # Insert the result at the beginning

def button_plusmin():
  number = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end
  tx1.insert("1.0", -float(number))  # Insert the result at the beginning

def button_dot():
  current = tx1.get("1.0", tk.END)  # Get the text from the beginning to the end
  tx1.delete("1.0", tk.END)  # Delete the text from the beginning to the end
  tx1.insert("1.0", current + ".")  # Insert the new text at the beginning

t1=tk.Tk()
t1.title("Calculator")

tx1=tk.Text(t1,width=57,height=4,borderwidth=2)
tx1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
button_1 = tk.Button(t1, text="1", width=10, height=3, command=lambda: button_click(1))
button_2 = tk.Button(t1, text="2", width=10, height=3, command=lambda: button_click(2))
button_3 = tk.Button(t1, text="3", width=10, height=3, command=lambda: button_click(3))
button_4 = tk.Button(t1, text="4", width=10, height=3, command=lambda: button_click(4))
button_5 = tk.Button(t1, text="5", width=10, height=3, command=lambda: button_click(5))
button_6 = tk.Button(t1, text="6", width=10, height=3, command=lambda: button_click(6))
button_7 = tk.Button(t1, text="7", width=10, height=3, command=lambda: button_click(7))
button_8 = tk.Button(t1, text="8", width=10, height=3, command=lambda: button_click(8))
button_9 = tk.Button(t1, text="9", width=10, height=3, command=lambda: button_click(9))
button_0 = tk.Button(t1, text="0", width=23, height=3, command=lambda: button_click(0))
button_add = tk.Button(t1, text="+", width=10, height=3, bg="orange", command=button_add)
button_sub = tk.Button(t1, text="-", width=10, height=3, bg="orange", command=button_sub)
button_mul = tk.Button(t1, text="*", width=10, height=3, bg="orange", command=button_mul)
button_div = tk.Button(t1, text="/", width=10, height=3, bg="orange", command=button_div)
button_equal = tk.Button(t1, text="=", width=10, height=3, bg="orange", command=button_equal)
button_clear = tk.Button(t1, text="AC", width=10, height=3, command=button_clear)
button_per = tk.Button(t1, text="%", width=10, height=3, command=button_per)
button_plusmin = tk.Button(t1, text="+/-", width=10, height=3, command=button_plusmin)
button_dot = tk.Button(t1, text=".", width=10, height=3, command=button_dot)

button_clear.grid(row=1, column=0, padx=0, pady=0)
button_plusmin.grid(row=1, column=1, padx=0, pady=0)
button_per.grid(row=1, column=2, padx=0, pady=0)
button_div.grid(row=1, column=3, padx=0, pady=0)
button_7.grid(row=2, column=0, padx=0, pady=0)
button_8.grid(row=2, column=1, padx=0, pady=0)
button_9.grid(row=2, column=2, padx=0, pady=0)
button_mul.grid(row=2, column=3, padx=0, pady=0)
button_4.grid(row=3, column=0, padx=0, pady=0)
button_5.grid(row=3, column=1, padx=0, pady=0)
button_6.grid(row=3, column=2, padx=0, pady=0)
button_sub.grid(row=3, column=3, padx=0, pady=0)
button_1.grid(row=4, column=0, padx=0, pady=0)
button_2.grid(row=4, column=1, padx=0, pady=0)
button_3.grid(row=4, column=2, padx=0, pady=0)
button_add.grid(row=4, column=3, padx=0, pady=0)
button_0.grid(row=5, column=0, padx=0, pady=0,columnspan=2)
button_dot.grid(row=5, column=2, padx=0, pady=0)
button_equal.grid(row=5, column=3, padx=0, pady=0)
t1.mainloop()
