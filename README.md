### API PREDIÇÃO CLASSIFICATÓRIA

***

Essa atividade foi desenvolvida para disponibilizar um sistema na AWS que ao acessar a rota `/` terá como resposta uma frase de sucesso e ao acessar a rota `/api/v1/predict` utilizando o método post com parâmetros no formato Json, após processamento a resposta será outro Json com a informação da predição da classificação gerado indicando qual reserva se encaixa em qual faixa de preço estipulado.

## Índice
<a name="ancora"></a>
1. [Desenvolvimento do projeto](#desenvolvimento-do-projeto)
2. [Estrutura de pastas](#estrutura-de-pastas)
3. [Funcionalidades](#funcionalidades)
4. [Como utilizar a aplicação?](#como-utilizar)
5. [Modelos para testes do sistema](#modelos-teste)
6. [Escolha de modelo](#escolhaModelo)
7. [Arquitetura do projeto](#arquitetura)
8. [Testes de unidade](#testes)

## Desenvolvimento do projeto <a name="desenvolvimento-do-projeto"></a>

As tecnologias adotadas para o desenvolvimento incluem Python, que atuou como base para o backend da aplicação, e o framework http FastAPI. Para efetuar a conexão com a API desenvolvida.

O Sagemaker foi utilizado para treinamento dos modelos utilizando o notebook em python, o sistema foi inserido em um container utilizando o Dockerfile e por fim para a hospedagem da aplicação, a opção recaiu sobre o AWS Elastic Beanstalk. 

 O resultado final é uma aplicação que retorna a predição da classificação de valores das reservas para cada faixa de preço.

## Estrutura de pastas <a name="estrutura-de-pastas"></a>

O editor de códigos utilizado foi o Visual Studio Code, aplicando a seguinte estrutura de pastas:
```shell
├─ src/
│   ├─ controllers/ 
│   │   └── predict_controller.py
│   │ 
│   ├─ models/ 
│   │   └── hotel_reservation.py
│   │
│   ├─ routes/
│   │   └── router.py
│   │ 
│   ├─ sagemaker_configuration/
│   │   └── predict_model_configuration.py
│   │
│   ├─ tests/
│   │
│   ├─ utils/
│   │   └── constants/
│   │   │   	└── base_values.py		
│   │   │
│   │   └─ functions/
│   │         └── process_prediction_data.py
│   │  
│   └── main.py
│
├─ notebooks/
│   │   └── sage_maker_notebook.ipynb
│   │   └── test_notebook.ipynb
├─ .env
├─ .env.example
├─ .gitignore
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
├─ setup.py
└─ README.md
```

***


## Funcionalidades <a name="funcionalidades"></a>

Ao enviar via método post um JSON seguindo o formato abaixo a API retorna uma predição de qual será a classificação de cada reserva por faixa de preço.

Ao acessar as rotas estabelecidas abaixo é recebido as informações formatadas.

## Acesso ao sistema <a name="acesso-ao-sistema"></a>


### Rota → Get / 


#### Resposta:

```json
{
    "message": "projeto em produção"
}
```


### Rota → Post /api/v1/predict

#### Resposta:

```json
{
    "result": 1
}
```





<div aling="center">
	<img src="./src/public/img/howToUse.gif" width="500px"/>
</div>


***

## Como utilizar a aplicação? <a name="como-utilizar"></a>



1. Acessar a rota /api/v1/predict utilizando um software de envio de requisições (exemplo: Postman) fornecendo informações no formato dos seguintes modelos:

**IMPORTANTE**: a requisição precisa constar todas as chaves conforme indicado abaixo, caso contrário ocorrerá um erro na API. 


### Modelo 01:

```json
{
    "no_of_adults": 2,
    "no_of_children": 0,
    "no_of_weekend_nights": 1,
    "no_of_week_nights": 2,
    "type_of_meal_plan": "Meal Plan 1",
    "required_car_parking_space": 0,
    "room_type_reserved": "Room_Type 1",
    "lead_time": 224,
    "arrival_year": 2017,
    "arrival_month": 10,
    "arrival_date": 2,
    "market_segment_type": "Offline",
    "repeated_guest": 0,
    "no_of_previous_cancellations": 0,
    "no_of_previous_bookings_not_canceled":0,
    "no_of_special_requests": 0,
    "booking_status": "Not_Canceled"
}
```

#### Resposta esperada:

```json
{
    "result": 1
}
```





### Modelo 02:


```json
{
  "no_of_adults": 3,
  "no_of_children": 2,
  "no_of_weekend_nights": 4,
  "no_of_week_nights": 2,
  "type_of_meal_plan": "Meal Plan 1",
  "required_car_parking_space": 2,
  "room_type_reserved": "Room_Type 1",
  "lead_time": 224,
  "arrival_year": 2017,
  "arrival_month": 10,
  "arrival_date": 2,
  "market_segment_type": "Offline",
  "repeated_guest": 0,
  "no_of_previous_cancellations": 0,
  "no_of_previous_bookings_not_canceled":0,
  "no_of_special_requests": 0,
  "booking_status": "Not_Canceled"
}
```

#### Resposta esperada:

```json
{
    "result": 2
}
```





### Modelo 03:

```json
{
    "no_of_adults": 3,
    "no_of_children": 0,
    "no_of_weekend_nights": 2,
    "no_of_week_nights": 6,
    "type_of_meal_plan": "Meal Plan 1",
    "required_car_parking_space": 0,
    "room_type_reserved": "Room_Type 4",
    "lead_time": 85,
    "arrival_year": 2018,
    "arrival_month": 8,
    "arrival_date": 3,
    "market_segment_type": "Online",
    "repeated_guest": 0,
    "no_of_previous_cancellations": 0,
    "no_of_previous_bookings_not_canceled": 0,
    "no_of_special_requests": 1,
    "booking_status": "Not_Canceled"
}
```

#### Resposta esperada:

```json
{
    "result": 3
}
```


## Escolha de modelo <a name="escolhaModelo"></a>

Foram realizados diversos testes antes da escolha do modelo definitivo, como por exemplo RandomForest e KNN, a fim de encontrar o modelo com maior precisão.
Os modelos de teste estão localizados no notebook `test_notebook.ipynb`

### Modelo escolhido

O modelo XGBoost apresentou a melhor precisão de todos os modelos, alcançando 87% de assertividade nas previsões.


## Arquitetura do projeto <a name="arquitetura"></a>


## Testes de unidade: <a name="testes"></a>

No projeto também foram elaborados testes de unidade a fim de trazer maior qualidade ao código, usando a biblioteca `pytest`. Os testes apresentam um total de coverage de 96%.





