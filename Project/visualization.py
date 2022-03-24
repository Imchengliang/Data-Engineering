import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("test.xlsx")
print(df)
executor1 = ("1 executor", "2 executors", "3 executors", "4 executors")
executor2 = ("2cores+2GB", "3cores+4GB", "4cores+6GB")

def create_list(a, b, g):
    c, d, e, f = [], [], [], []
    for i in range(a, b, g):
        c.append(df["Time for loading data (s)"][i])
        d.append(df["Time for model training (s)"][i])
        e.append(df["Time for model testing (s)"][i])
        f.append(df["Time for loading data (s)"][i]+df["Time for model training (s)"][i]+df["Time for model testing (s)"][i])
    return f, c, d, e

def horizontal_scalability(a, b, c, d, e, f, y):
    bar_width = 0.15 
    index1 = np.arange(len(executor1)) 
    index2 = index1 + bar_width 
    index3 = index2 + bar_width
    plt.bar(index1, height=a, width=bar_width, color='red', label=d)
    plt.bar(index2, height=b, width=bar_width, color='blue', label=e)
    plt.bar(index3, height=c, width=bar_width, color='green', label=f)
    if y == 1:
        x = [c[0], b[1], a[2]]
        executor0 = ("1 executor", "2 executors", "3 executors")
        plt.plot(executor1, a, color='red', linewidth=2.0, linestyle='--', label='strong scaling')
        #plt.plot(executor1, b, color='blue', linewidth=2.0, linestyle='--')
        #plt.plot(executor1, c, color='green', linewidth=2.0, linestyle='--')
        plt.plot(executor0, x, color='black', linewidth=2.0, linestyle='-', label='weak scaling')
    plt.legend() 
    plt.xticks(index1+bar_width/2, executor1) 
    plt.ylabel('Time') 
    plt.title('core for each executor is 2 and memory for each executor is 2GB') 
    plt.show()

def vertical_scalability(a, b, c, d, e, f, y):
    bar_width = 0.15 
    index1 = np.arange(len(executor2)) 
    index2 = index1 + bar_width 
    index3 = index2 + bar_width
    plt.bar(index1, height=a, width=bar_width, color='red', label=d)
    plt.bar(index2, height=b, width=bar_width, color='blue', label=e)
    plt.bar(index3, height=c, width=bar_width, color='green', label=f)
    if y == 1:
        x = [c[0], b[1], a[2]]
        plt.plot(executor2, a, color='red', linewidth=2.0, linestyle='--', label='strong scaling')
        #plt.plot(executor2, b, color='blue', linewidth=2.0, linestyle='--')
        #plt.plot(executor2, c, color='green', linewidth=2.0, linestyle='--')
        plt.plot(executor2, x, color='black', linewidth=2.0, linestyle='-', label='weak scaling')
    plt.legend() 
    plt.xticks(index1+bar_width/2, executor2) 
    plt.ylabel('Time') 
    plt.title('number of executor is 1') 
    plt.show()

time_horizonital_11, time_horizonital_11_load, time_horizonital_11_train, time_horizonital_11_test = create_list(3, -1, -1)
time_horizonital_3_1, time_horizonital_3_1_load, time_horizonital_3_1_train, time_horizonital_3_1_test = create_list(9, 5, -1)
time_horizonital_1_6, time_horizonital_1_6_load, time_horizonital_1_6_train, time_horizonital_1_6_test = create_list(15, 11, -1)
time_vertical_11, time_vertical_11_load, time_vertical_11_train, time_vertical_11_test = create_list(3, 6, 1)
time_vertical_3_1, time_vertical_3_1_load, time_vertical_3_1_train, time_vertical_3_1_test = create_list(9, 12, 1)
time_vertical_1_6, time_vertical_1_6_load, time_vertical_1_6_train, time_vertical_1_6_test = create_list(15, 18, 1)

#horizontal_scalability(time_horizonital_11_load, time_horizonital_3_1_load, time_horizonital_1_6_load, 'Time for loading 11 GB data', 'Time for loading 3.1 GB data', 'Time for loading 1.6 GB data', 0)
#horizontal_scalability(time_horizonital_11_train, time_horizonital_3_1_train, time_horizonital_1_6_train, 'Time for training(11 GB test data)', 'Time for training(3.1 GB test data)', 'Time for training(1.6 GB test data)', 0)
#horizontal_scalability(time_horizonital_11_test, time_horizonital_3_1_test, time_horizonital_1_6_test, 'Time for testing 11 GB data', 'Time for testing 3.1 GB data', 'Time for testing 1.6 GB data', 0)
#horizontal_scalability(time_horizonital_11, time_horizonital_3_1, time_horizonital_1_6, 'Time for running 11 GB data', 'Time for running 3.1 GB data', 'Time for running 1.6 GB data', 1)
#vertical_scalability(time_vertical_11_load, time_vertical_3_1_load, time_vertical_1_6_load, 'Time for loading 11 GB data', 'Time for loading 3.1 GB data', 'Time for loading 1.6 GB data', 0)
#vertical_scalability(time_vertical_11_train, time_vertical_3_1_train, time_vertical_1_6_train, 'Time for training(11 GB test data)', 'Time for training(3.1 GB test data)', 'Time for training(1.6 GB test data)', 0)
#vertical_scalability(time_vertical_11_test, time_vertical_3_1_test, time_vertical_1_6_test, 'Time for testing 11 GB data', 'Time for testing 3.1 GB data', 'Time for testing 1.6 GB data', 0)
vertical_scalability(time_vertical_11, time_vertical_3_1, time_vertical_1_6, 'Time for running 11 GB data', 'Time for running 3.1 GB data', 'Time for running 1.6 GB data', 1)