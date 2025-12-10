#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

# input 0.045 p/ cd0 e 0.05194 p/ k
# Metodo analitico para o tracado da polar (miranda - simposio-unaerp)


import math
import matplotlib.pyplot as plt

def main():
    # Solicita os valores do usuário
    Cd0 = float(input("Insira Cd0 (Arrasto parasita): "))
    K = float(input("Insira K (Coeficiente de proporcionalidade): "))
    
    # Listas para armazenar os valores de cl e Cd
    cl_values = []
    Cd_values = []
    
    # Calcula os valores de Cd para cl de 0 a 2.5 com incrementos de 0.1
    cl = 0.0
    while cl <= 2.5:
        Cd = Cd0 + K * (cl ** 2)
        cl_values.append(cl)
        Cd_values.append(Cd)
        cl += 0.1
    
    # Exibe os valores calculados
    print(f"{'cl':>10} {'Cd':>10}")
    for cl, Cd in zip(cl_values, Cd_values):
        print(f"{cl:>10.1f} {Cd:>10.3f}")
    
    # Plota os resultados
    plt.figure(figsize=(10, 5))
    plt.plot(Cd_values, cl_values, marker='o', linestyle='-', color='b')
    plt.xlabel('CD (Coeficiente de Arrasto)')
    plt.ylabel('CL (Coeficiente de Sustentação)')
    plt.title('Polar de Arrasto')
    plt.grid(True)
    plt.ylim(0, 2.5)
    plt.xlim(0, max(Cd_values))
    plt.show()

if __name__ == "__main__":
    main()

# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.
