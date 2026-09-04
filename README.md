# Coletor de Tráfego Aéreo — Região Sul do Brasil

Coletor de dados de aeronaves em tempo real, filtrado para o espaço aéreo da região sul do Brasil (Paraná, Santa Catarina e Rio Grande do Sul), com conversão de unidades e exportação para JSON.

## Sobre o projeto

Sou controlador de tráfego aéreo e estou migrando para a área de desenvolvimento. Este projeto nasceu como o primeiro de uma série de projetos de portfólio aplicando, ao código, conhecimento real de operação de tráfego aéreo — unidades de medida, conceitos como flight level, e a forma como os dados de uma aeronave são normalmente lidos e interpretados no dia a dia de controle.

Os dados são obtidos em tempo real através da [OpenSky Network API](https://opensky-network.org/), um projeto aberto que agrega dados de ADS-B de receptores ao redor do mundo.

## O que o projeto faz

- Consulta a API pública da OpenSky Network, filtrando apenas aeronaves dentro dos limites aproximados da região sul do Brasil
- Modela cada aeronave como um objeto (`Aircraft`), usando Programação Orientada a Objetos
- Converte automaticamente:
  - Altitude de metros para **flight level** (acima de FL100) ou pés (abaixo disso)
  - Velocidade de m/s para **nós (kt)**
- Trata corretamente casos em que a API não retorna determinado dado (ex: aeronaves sem altitude ou velocidade disponível), sem quebrar a execução
- Exporta o resultado formatado para um arquivo **JSON**, com timestamp no nome do arquivo, para não sobrescrever capturas anteriores

## Como rodar

1. Clone este repositório
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install requests
   ```
4. Execute o script:
   ```bash
   python main.py
   ```
5. O resultado será salvo em um arquivo `frota_sul_<timestamp>.json` na pasta do projeto

## Exemplo de saída

```json
[
    {
        "Callsign": "TAM3456 ",
        "Origin": "Brazil",
        "Longitude": -49.1758,
        "Latitude": -25.5285,
        "Flight level": "FL 350",
        "Speed": "465 kt"
    },
    {
        "Callsign": "GLO1234 ",
        "Origin": "Brazil",
        "Longitude": -51.2177,
        "Latitude": -30.0346,
        "Altitude": "2400 ft",
        "Speed": "180 kt"
    }
]
```

## Limitações conhecidas

- O filtro geográfico usa uma **bounding box** (caixa retangular) aproximada da região sul, não o polígono real da FIR Curitiba, que possui bordas irregulares
- A API do OpenSky não fornece dados de origem/destino de rota no endpoint utilizado (`/states/all`) — o campo `Origin` representa o país de registro da aeronave, não o aeroporto de origem do voo

## Próximos passos

Este é o primeiro de uma série de projetos que, futuramente, serão integrados em uma ferramenta única de monitoramento e análise de tráfego aéreo, incluindo dashboard visual e detecção de conflitos de separação.

## Tecnologias

- Python 3
- [requests](https://pypi.org/project/requests/)
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/)
