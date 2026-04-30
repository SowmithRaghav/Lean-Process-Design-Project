import matplotlib.pyplot as plt

parameters = ['Lead Time', 'Defects', 'Inventory']
before = [12, 8, 500]
after = [7, 2, 280]

x = range(len(parameters))

plt.figure(figsize=(8,5))
plt.bar(x, before, width=0.4, label='Before Lean')
plt.bar([i + 0.4 for i in x], after, width=0.4, label='After Lean')

plt.xticks([i + 0.2 for i in x], parameters)
plt.ylabel('Values')
plt.title('Lean Manufacturing Improvement Analysis')
plt.legend()

plt.savefig('efficiency_graph.png')
plt.show()
