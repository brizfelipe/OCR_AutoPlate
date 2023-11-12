# OCR_AutoPlate

**OCR_AutoPlate** é um sistema de reconhecimento óptico de caracteres (OCR) desenvolvido em Python para identificação e leitura automatizada de placas de carro.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
OCR_AutoPlate/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── labeled/
│   ├── train/
│   ├── val/
│   └── test/
│
├── models/
│   ├── saved/
│   └── logs/
│
├── src/
│   ├── data_preprocessing/
│   ├── model/
│   ├── train/
│   ├── evaluate/
│   └── utils/
│
├── app/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Pré-requisitos

- Python 3.x
- Ambiente virtual (recomendado)
- Pacotes Python listados em `requirements.txt`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-username/OCR_AutoPlate.git
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Treinamento do Modelo

1. Coloque as imagens brutas na pasta `data/raw/`.
2. Execute os scripts de pré-processamento em `src/data_preprocessing/`.
3. Execute os scripts de treinamento em `src/train/`.
4. Verifique os modelos treinados na pasta `models/saved/`.

## Uso da Aplicação

O código da aplicação final está localizado na pasta `app/`. Integre o modelo treinado neste ambiente conforme necessário.


## Licença

Este projeto é distribuído sob a licença [MIT](LICENSE).

---
Felipe Briz 
Email: briz.felipe@gmail.com
