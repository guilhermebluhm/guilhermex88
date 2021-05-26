lista_jogador = [];
#lista_melhor_jogador = [];
import random

aux = 0;
continuar = True;
soma_votos = [];
retorno_soma_votos = 0;
opcao = '';
escolha_melhor_jogador = '';
melhor_jogador = False;

while(continuar != False):
    print("votos para os melhores jogadores");
    for i in range(1,6,1):
        try:
            lista_jogador.append(int(input("votos jogador nº {} -> ".format(i))));
            escolha_melhor_jogador = input("foi o melhor jogador da temporada: [s] - sim [n] - nao").lower();
            if(escolha_melhor_jogador == 's'and melhor_jogador != True):
                melhor_jogador = True;
                voto_melhor_jogador = int(input("confirme o voto do melhor jogador: "));
            elif(escolha_melhor_jogador == 'n'):
                print("o proximo jogador quem sabe");
            soma_votos.append(lista_jogador);
        except ValueError:
            print("informe um valor numero valido");
            lista_jogador.append(int(input("votos jogador nº {} -> ".format(i))));
            soma_votos.append(lista_jogador);

    def soma_lista(lista):
        retorno_soma_votos = 0;
        for i in range(len(soma_votos)):
            if(len(lista[i]) - 1):
                retorno_soma_votos = sum(lista[i]);
                retorno_soma_votos += voto_melhor_jogador;                
        return retorno_soma_votos;
    
    soma = soma_lista(soma_votos);
    print(soma);    

    size_list = len(lista_jogador);

    for j in range(size_list):
        if(lista_jogador[j] != 0):
            print("jogadores que receberam votos: {}".format((lista_jogador[j]/soma)));
            #lista_jogador_aux.append(lista_jogador[j]);
    
    print("houve melhor jogador: {} votos do melhor jogador: {}".format(melhor_jogador,voto_melhor_jogador));
    opcao = input("deseja corrigir algo e inserir os dados novamente: [s] - Sim [n] - Não").lower();
    if(opcao == 's'):
        continuar = True;
    elif(opcao == 'n'):
        continuar = False;
