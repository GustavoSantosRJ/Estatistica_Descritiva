import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class dashboard_2x2:

    def __init__(self, titulo_dash, largura=14, altura=9, seaborn_style='whitegrid', seaborn_palette='Blues_r'):
        self.titulo_dash = titulo_dash
        sns.set_theme(style=seaborn_style, palette=seaborn_palette)
        fig, self.axes = plt.subplots(2, 2, figsize=(largura, altura))
        fig.suptitle(self.titulo_dash, fontsize=16, fontweight='bold', y=0.98,)

    def pos_x(self, posicao):
        match posicao:
            case 1:
                return 0
            case 2:
                return 0
            case 3:
                return 1
            case 4:
                return 1

    def pos_y(self, posicao):
        match posicao:
            case 1:
                return 0
            case 2:
                return 1
            case 3:
                return 0
            case 4:
                return 1
                        
    def lineplot(self, posicao, titulo, df_dados, marcador='o', cor='#08519c'):
        x = self.pos_x(posicao)
        y = self.pos_y(posicao)
        sns.lineplot(
            data=df_dados,
            x=df_dados.columns[0],
            y=df_dados.columns[1],
            marker=marcador,
            color=cor,
            linewidth=2.5,
            ax=self.axes[x, y],
        )
        self.axes[x, y].set_title(titulo, fontweight='bold')
        self.axes[x, y].set_xlabel(df_dados.columns[0])
        self.axes[x, y].set_ylabel(df_dados.columns[1])

    def barplot(self, posicao, titulo, df_dados, marcador='o', bar_palette='Blues_d'):
        x = self.pos_x(posicao)
        y = self.pos_y(posicao)
        sns.barplot(
            data=df_dados,
            x=df_dados.columns[0],
            y=df_dados.columns[2],
            hue=df_dados.columns[1],
            palette=bar_palette,
            ax=self.axes[x, y],
        )
        self.axes[x, y].set_title(titulo, fontweight='bold')
        self.axes[x, y].set_xlabel(df_dados.columns[0])
        self.axes[x, y].set_ylabel(df_dados.columns[2])
        self.axes[x, y].legend(title=df_dados.columns[1])

    def regplot(self, posicao, titulo, df_dados, cor='#2171b5', estilo_pontos={'s': 60}):
        x = self.pos_x(posicao)
        y = self.pos_y(posicao)
        sns.regplot(
            data=df_dados,
            x=df_dados.columns[0],
            y=df_dados.columns[1],
            color=cor,
            scatter_kws=estilo_pontos,
            ax=self.axes[x, y],
        )
        self.axes[x, y].set_title(titulo, fontweight='bold')
        self.axes[x, y].set_xlabel(df_dados.columns[0])
        self.axes[x, y].set_ylabel(df_dados.columns[1])

    def heatmap(self, posicao, titulo, df_dados, mapa_cor='Blues', formato_numero='.2f'):
        x = self.pos_x(posicao)
        y = self.pos_y(posicao)
        sns.heatmap(
            df_dados,
            annot=True,
            cmap=mapa_cor,
            fmt=formato_numero,
            cbar=False,
            square=True,
            ax=self.axes[x, y],
        )
        self.axes[x, y].set_title(titulo, fontweight='bold')

    def show(self):
        plt.tight_layout()
        plt.show()