import matplotlib.pyplot as plt
import argparse
import numpy as np
import mpltex
# Parser
parser = argparse.ArgumentParser(description='Plot First-to-first passage time histgram')

parser.add_argument('filepath', type=str, help='Give the file location')
parser.add_argument('tau_m', type=float, help='τₘ/τ_D, rescaled mass')
parser.add_argument('tau_g', type=float, help='Memory time τ_Γ')

args=parser.parse_args()

FFPT = np.loadtxt(args.filepath)



@mpltex.acs_decorator
def hist_log_plot(FPT, bins_size):
    bins_number = int(np.log(int(np.max(FPT)+1)+1))*5
    bins_edge = [np.exp(i/bins_size) for i in range(-5*4, bins_number)]
    # The range of plot, from (-1, max(FPT))
    # bins_edge.insert(bins_edge.index(bins_edge[0]), 1e-4)
    data, bins= np.histogram(FPT, bins=bins_edge, density=True) # Mid points of two edges of bins
    bin_midpoit = []
    mid = 0.0
    for i in range(len(bins)-1):
        if bins[i]==0:
            mid = np.exp(2*np.log(bins[i+1]))
            bin_midpoit.append(mid)
        else:
            mid = np.exp(1/2*(np.log(bins[i]) + np.log(bins[i+1])))
            bin_midpoit.append(mid)
    return bin_midpoit, data

def plot_beginning_index(array):
    for i in range(len(array)):
        if array[i]!=0:
            return i



def plot_ffpt():
    m = args.tau_m
    g = args.tau_g
    fig, ax = plt.subplots(1)
    fig.set_size_inches(w=3.25, h=3.25/1.618)
    fig.dpi=300

    linestyles = mpltex.linestyles()
    bin_FFPT, count_FFPT = hist_log_plot(FFPT, 5)
    f = plot_beginning_index(count_FFPT)
    ax.scatter(bin_FFPT[f:], count_FFPT[f:])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("$\\tau_m/\\tau_D$={:5.3f}, $\\tau_\Gamma/\\tau_D$={:5.3f}".format(m, g))
    ax.set_ylabel("Probability")
    ax.set_xlabel("Escape time ($t/\\tau_D$)")

    plt.show()
    plt.savefig(args.filepath[:-4]+".png", bbox_inches="tight")
    plt.close()

plot_ffpt()




