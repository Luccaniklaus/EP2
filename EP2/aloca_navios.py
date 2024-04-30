import from posicao_suporta
def aloca_navios(mapa,blocos):
    for bloco in blocos:
        alocado=True
        while alocado:
            linha = random.randint(0, bloco-1)
            coluna = random.randint(0, bloco-1)
            orientacao = random.choice(['h', 'v'])
            posicao=posicao_suporta(mapa,bloco,linha,coluna,orientacao)
            if posicao:
                alocado=False
        for k in range(bloco):
            if orientacao=='v':
                mapa[linha+k][coluna]='N'    
            if orientacao=='h':
                mapa[linha][coluna+k]='N'
    return mapa
