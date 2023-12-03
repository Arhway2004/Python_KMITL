# import matplotlib.pyplot as plt

# def pie_chart(data):
#     unique_values = set(data)
#     counts = [data.count(val) for val in unique_values]
    
#     labels = [str(val) for val in unique_values]
    
#     plt.figure(figsize=(8, 8))
#     plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
#     plt.title("Pie Chart")
    
 
#     # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     plt.show()

# # Example usage
# data = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3]
# pie_chart(data)
import matplotlib.pyplot as plt

def pie_chart(data):
    unique_values = set(data)
    counts = [data.count(val) for val in unique_values]
    
    
    plt.figure(figsize=(8, 8))
    plt.pie(counts, startangle=140)
    plt.title("Pie Chart")

    plt.show()

# Example usage
data = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3]
pie_chart(data)
