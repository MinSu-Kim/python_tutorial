import matplotlib.pyplot as plt

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(2, 2, figsize=(9, 9), sharey=True)
axs[0][0].bar(names, values)
axs[0][1].scatter(names, values)
axs[1][0].plot(names, values)

cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]
axs[1][1].plot(activity, dog, label="dog")
axs[1][1].plot(activity, cat, label="cat")
axs[1][1].legend()

fig.suptitle('Categorical Plotting')
plt.show()
