from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
silhouette_vals = silhouette_samples(reduced_data, clusters)
silhouette_avg = silhouette_score(reduced_data, clusters)
plt.figure(figsize=(8, 6))
y_lower = 10
for i in range(k):
    cluster_silhouette_vals = silhouette_vals[clusters == i]
    cluster_silhouette_vals.sort()
    size_cluster_i = cluster_silhouette_vals.shape[0]
    y_upper = y_lower + size_cluster_i
    color = cm.nipy_spectral(float(i) / k)
    plt.fill_betweenx(np.arange(y_lower, y_upper),
                      0, cluster_silhouette_vals,
                      facecolor=color, edgecolor=color, alpha=0.7)
    plt.text(-0.5, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10
plt.title("Silhouette plot dla k = %d" % k)
plt.xlabel("Wartość silhouette")
plt.ylabel("Indeks klastra")
plt.axvline(x=silhouette_avg, color="red", linestyle="--")
plt.text(silhouette_avg + 0.1, 10, 'Średnia: %.2f' % silhouette_avg)
plt.show()
