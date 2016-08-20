
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (16, 9)


def plot_grid_search_result(grid_scores, x, y = "mean_validation_score", hue = None, row = None, col = None, save_to_file = False, file_name = "plot.png"):
	"""expecting grid_scores to be the grid_scores attribute from a fitted grid_search object"""
	plot_df = pd.DataFrame([result.parameters for result in grid_scores])
 	plot_df["mean_validation_score"] = [result.mean_validation_score for result in grid_scores]
	if not hue:
		figure = sns.factorplot(x = x, y = y, data = plot_df)
	elif not row:
		figure = sns.factorplot(x = x, y = y, hue = hue, data = plot_df)
	elif not col:
		figure = sns.factorplot(x = x, y = y, hue = hue, row = row, data = plot_df)
	else:
		figure = sns.factorplot(x = x, y = y, hue = hue, row = row, col = col, data = plot_df)
	if not save_to_file:
		plt.show()
	else:
		figure.savefig(file_name)


def plot_roc_curve(roc_curves,save_to_file = False, file_name = "plot.png"):
	"""expecting roc_curves to be a list of tuples, ("method_name", (fpr, tpr, threshold)))"""
	num_methods = len(roc_curves)
	plt.figure()
	plt.xlim([-0.05,1.05])
	plt.ylim([-0.05,1.05])
	for curve in roc_curves:
		method_name = curve[0]
		fpr, tpr, _ = curve[1]
		fpr = np.concatenate([[0], fpr, [1]])
		tpr = np.concatenate([[0], tpr, [1]])
		plt.plot(fpr, tpr, label = method_name)
	plt.xlabel("False Positive Rate")
	plt.ylabel("True Positive Rate")
	plt.title("ROC curve(s)")
	plt.legend(loc="lower right")
	if not save_to_file:
		plt.show()
	else:
		figure.savefig(file_name)
