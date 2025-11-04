import math
import matplotlib.pyplot as plt
x_data=[1,2,3,4,5,6,7,8]
y_data=[0,0,0,0,1,1,1,1]
def sigmoid(x):
    return 1/(1+math.exp(-x))
def predict(x):
    return sigmoid(1.5*x-6)
predicted_values=[predict(x) for x in x_data]
print("Predicted values")
for i in range(len(x_data)):
    print(f"Study hours:{x_data[i]}------>Pass chance:{predicted_values[i]:.2f}")
plt.scatter(x_data,y_data,color="orange",label="Actual data(Pass/Fail)",s=80,edgecolor="black")
x_range=[i/10 for i in range(0,100)]
y_range=[predict(x)for x in x_range]
plt.plot(x_range,y_range,color="purple",line_width=2.5,label="Logistic regression curve")
plt.title("Data point")
plt.xlabel("Study hours")
plt.ylabel("Pass(1)/Fail(0)")
plt.legend()
plt.show()