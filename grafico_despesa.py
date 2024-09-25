import matplotlib.pyplot as plt
import coleta_dados as t

plt.bar(t.lista_nome_despesa_ordenada, t.lista_valor_despesa_ordenada,)
plt.xlabel('Nome')
plt.ylabel('R$')
plt.title('Grafico de Gastos Mensais')
plt.show()