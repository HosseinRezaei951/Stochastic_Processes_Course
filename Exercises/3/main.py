import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

def birthDeath(_firstPopulation, _maxPopulation, _nPath , _birthRate, _deathRate):
    X0 = _firstPopulation # initial population size

    s = np.zeros((_nPath , _maxPopulation))
    X = np.zeros((_nPath , _maxPopulation))
    X[:,0] = X0
    s[:,0] = 0.001

    for j in range(_nPath):
        i = 0
        while X[j,i] > 0 and i < (_maxPopulation-1):
            U1 = np.random.rand()
            U2 = np.random.rand()
            h = - np.log(U1)/((_birthRate+_deathRate)*X[j,i])
            s[j,i+1] = s[j,i] + h
            if U2 < _birthRate/(_birthRate+_deathRate):
                X[j,i+1] = X[j,i] + 1 # birth occurs
            else:
                X[j,i+1] = X[j,i] - 1 # death occurs
            i += 1
    return [s, X]


    
def main():
    firstPopulation = 50
    maxPopulation = 1000
    nPath = 3
    birthRates = [1.0, 0.9, 0.7, 0.5, 0.3, 0.1] 
    deathRates = [1.0, 0.9, 0.7, 0.5, 0.3, 0.1]

    fig, axs = plt.subplots(len(birthRates), len(deathRates),figsize=(32, 18))

    for i in range(len(birthRates)):
        for j in range(len(deathRates)):
            [sojourn , population] = birthDeath(firstPopulation,
                                                maxPopulation,
                                                nPath,
                                                birthRates[i],
                                                deathRates[j])

            ## Sets axis ranges for plotting
            xmax = max([max(sojourn[k,:]) for k in range(nPath)])
            ymax = max([max(population[k,:]) for k in range(nPath)])

            sojourn[sojourn==0] = np.nan

            ## Generates plots
            for r in range(nPath):
                axs[i, j].step(sojourn[r,:], population[r,:], where="pre", label="Path %s" % str(r+1))

            axs[i, j].axis([-0.1, xmax+0.2, 0, ymax+2])
            axs[i, j].set_xlabel("Time", fontsize=14)
            axs[i, j].set_ylabel("Population Size", fontsize=14)
            axs[i, j].set_title("birth rate=" + str(birthRates[i]) + ", death rate=" + str(deathRates[j]))
            axs[i, j].legend()

    plt.tight_layout()
    plt.savefig("results/result.jpeg")
    

if __name__ == "__main__":
    main()