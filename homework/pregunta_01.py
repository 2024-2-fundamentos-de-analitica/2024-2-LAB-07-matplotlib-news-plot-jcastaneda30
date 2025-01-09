"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import matplotlib.pyplot as plt
import pandas as pd
import os
def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    colors = {
    'Television': 'dimgray',
    'Newspaper': 'grey',
    'Internet': 'tab:blue',
    'Radio': 'lightgrey',
    }
    zorder = {
    'Television': 1,
    'Newspaper': 1,
    'Internet': 2,
    'Radio': 1,
    }
    lineweight = {
    'Television': 2,
    'Newspaper': 2,
    'Internet': 3,
    'Radio': 2,
    }
    df = pd.read_csv("files/input/news.csv", index_col=0)
    plt.figure()
    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=lineweight[col],
        )
        
    plt.title("How people get their new", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    for col in df.columns:
        first = df.index[0]
        plt.scatter(
            x=first,
            y=df[col].loc[first],
            color = colors[col],
            zorder=zorder[col],
        )
        plt.text(
        first - 0.2,
        df [col] [first],
        col + " " + str(df[col][first] ) + "%",
        ha='right',
        va='center',
        color=colors[col],)
        last = df.index[-1]
        plt.scatter(
            x=last,
            y=df[col].loc[last],
            color = colors[col],
        )
        plt.text(
        last + 0.2,
        df [col] [last],
        col + " " + str(df[col][first] ) + "%",
        ha='left',
        va='center',
        color=colors[col],)
    if not os.path.isdir(os.path.join("files", "plots")):
        os.makedirs(os.path.join("files", "plots"))
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.show()

