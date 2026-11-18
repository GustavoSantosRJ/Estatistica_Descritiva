import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

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

class dash_distribuicao:
    
    def __init__(self, titulo_dash, largura=14, altura=9, seaborn_style='whitegrid', seaborn_palette='Blues_r'):
        self.titulo_dash = titulo_dash
        sns.set_theme(style=seaborn_style, palette=seaborn_palette)
        fig, self.axes = plt.subplots(2, 2, figsize=(largura, altura))
        fig.suptitle(self.titulo_dash, fontsize=16, fontweight='bold', y=0.98,)

    def show(self):
        # Passo 1: Isola a coluna de prejuízos e transforma em um Array do NumPy (como pede o PTD)
        serie_prejuizo = df_completo['Prejuizo_Estimado_Mil']
        array_prejuizo = serie_prejuizo.to_numpy()

        # Passo 2: Calcula Média, Mediana e o quanto elas estão distantes entre si
        media = np.mean(array_prejuizo)
        mediana = np.median(array_prejuizo)
        distancia_mm = (media - mediana) / mediana

        print(f"Média dos prejuízos:      R$ {media:.2f} mil")
        print(f"Mediana (valor típico):   R$ {mediana:.2f} mil")
        print(f"Distância Média-Mediana:  {distancia_mm:.1%} (Acima de 25% -> Média distorcida!)")

        # Passo 3: Calcula Quartis (Q1 e Q3), IQR e conta quantos Outliers Superiores existem
        q1, q3 = np.percentile(array_prejuizo, [25, 75])
        iqr = q3 - q1
        teto_outlier = q3 + 1.5 * iqr
        casos_outliers = df_completo[df_completo['Prejuizo_Estimado_Mil'] > teto_outlier]

        # Passo 4: Calcula Dispersão (CV), Assimetria e Curtose (escala do curso + 3)
        desvio_padrao = np.std(array_prejuizo, ddof=0)
        cv = desvio_padrao / media
        assimetria = serie_prejuizo.skew()
        curtose = serie_prejuizo.kurtosis() + 3

        print(f"Teto normal (Limite Sup.): R$ {teto_outlier:.2f} mil -> {len(casos_outliers)} casos acima do teto (Outliers)")
        print(f"Desvio Padrão: R$ {desvio_padrao:.2f} mil | Coeficiente de Variação (CV): {cv:.1%}")
        print(f"Assimetria: +{assimetria:.2f} (Assimétrica Positiva) | Curtose: {curtose:.2f} (Leptocúrtica)")

        # Cria uma tela dividida em 1 linha e 2 colunas
        fig, axes = plt.subplots(1, 2, figsize=(14, 4.8))

        # Quadro da esquerda: Histograma mostrando onde a maioria dos casos se concentra
        sns.histplot(serie_prejuizo, bins=35, kde=True, color='#3182bd', ax=axes[0])
        axes[0].axvline(media, color='#de2d26', linestyle='--', linewidth=2, label=f'Média: R$ {media:.1f}k')
        axes[0].axvline(mediana, color='#2ca25f', linestyle='-', linewidth=2, label=f'Mediana: R$ {mediana:.1f}k')
        axes[0].set_title('Distribuição dos Prejuízos (Cauda Longa à Direita)', fontweight='bold')
        axes[0].set_xlabel('Prejuízo Estimado (R$ mil)')
        axes[0].legend()

        # Quadro da direita: Cartão executivo sem eixos, apenas com os números traduzidos
        axes[1].axis('off')
        texto_diretoria = (
            f"PRONTUÁRIO EXECUTIVO — DATA ORGANIZED\n"
            f"{'='*37}\n"
            f"• Prejuízo Típico (Mediana): R$ {mediana:.2f} mil\n"
            f"• Média (Inflada):           R$ {media:.2f} mil (+{distancia_mm:.1%})\n"
            f"• Variação (CV):             {cv:.1%} (Alta instabilidade)\n"
            f"• Formato da Curva:          Assimétrica Positiva (+{assimetria:.2f})\n"
            f"• Risco de Extremos:         Leptocúrtica ({curtose:.2f})\n"
            f"• Casos Críticos (Outliers): {len(casos_outliers)} ocorrências\n"
            f"{'-'*57}\n"
            f"DECISÃO: Planejar orçamento pela Mediana e investigar\n"
            f"os {len(casos_outliers)} casos críticos."
        )
        axes[1].text(
            0.03, 0.5, texto_diretoria, fontsize=11, family='cascadia code', va='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor="#d2dce6", edgecolor='#08519c')
        )

        plt.tight_layout()
        plt.show()

