

def plot_grid_search_result(grid_scores, x, y = "mean_validation_score", hue = None, row = None, col = None, save_to_file = False, file_name = "plot.png"):
	from matplotlib import pyplot as plt
	import pandas as pd
	import seaborn as sns
	plot_df = pd.DataFrame([result.parameters for result in grid_scores])
 	plot_df["mean_validation_score"] = [result.mean_validation_score for result in grid_scores]
 	sns.set(style="whitegrid")
	plt.rcParams['figure.figsize'] = (16, 9)
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
