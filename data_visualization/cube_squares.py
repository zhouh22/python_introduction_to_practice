import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['KaiTi']

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("立方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
