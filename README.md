### Descrição do Projeto

Este projeto apresenta um aplicativo que integra as tecnologias Flask e React para oferecer funcionalidades avançadas relacionadas a dados de vinhos coletados do site da Embrapa. Por meio de endpoints que realizam scraping e análise de dados, a aplicação proporciona uma extração personalizada, flexível e eficiente de informações vitivinícolas, realizando buscas gerais ou aceitando parâmetros opcionais como ano e categoria. Sorbe a estrutura dessa API, o projeto está hospedado no Vercel para o front-end e no Render para o back-end.

### Links Úteis

- **Site da Embrapa: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01**
- **Frontend: https://projeto-fiap-coral.vercel.app/**
- **Backend: https://projeto-fiap.onrender.com/**
- **Swagger: https://projeto-fiap.onrender.com/apidocs**

### Estrutura do Projeto

#### Diagrama

![Diagrama em branco (1)](https://github.com/user-attachments/assets/effda8a5-569b-407d-853f-3c6bd32e20f6)

#### Requisitos

- **Python 3.8+**  
- **Node.js 14+**  
- **npm** or **yarn**


##### Códigos de Status HTTP:

- **200 Sucesso - Informações sobre os vinhos retornadas.**
- **400 Requisição inválida - Ano informado fora do período aceitado**
- **500 Erro interno no servidor - Falha durante o processo de web scraping.**

### Endpoints

#### Comerce Wine Scraping (/api/comerce/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de comercialização de vinhos

Exemplo requisição dados de 2020:
```
https://projeto-fiap.onrender.com/api/comerce/?year=2020
```
Exemplo retorno dados de 2020:
```
{
  "message": "[{'Produto': 'VINHO DE MESA', 'Quantidade (L.)': '215.557.931'}, {'Produto': 'Tinto', 'Quantidade (L.)': '189.573.423'}, {'Produto': 'Rosado', 'Quantidade (L.)': '1.394.901'}, {'Produto': 'Branco', 'Quantidade (L.)': '24.589.607'}, {'Produto': 'VINHO FINO DE MESA', 'Quantidade (L.)': '24.310.834'}, {'Produto': 'Tinto', 'Quantidade (L.)': '18.202.453'}, {'Produto': 'Rosado', 'Quantidade (L.)': '993.248'}, {'Produto': 'Branco', 'Quantidade (L.)': '5.115.133'}, {'Produto': 'VINHO FRIZANTE', 'Quantidade (L.)': '2.557.585'}, {'Produto': 'VINHO ORGÂNICO', 'Quantidade (L.)': '10.718'}, {'Produto': 'VINHO ESPECIAL', 'Quantidade (L.)': '-'}, {'Produto': 'Tinto', 'Quantidade (L.)': '-'}, {'Produto': 'Rosado', 'Quantidade (L.)': '-'}, {'Produto': 'Branco', 'Quantidade (L.)': '-'}, {'Produto': 'ESPUMANTES', 'Quantidade (L.)': '22.610.762'}, {'Produto': 'Espumante  Moscatel', 'Quantidade (L.)': '9.298.571'}, {'Produto': 'Espumante', 'Quantidade (L.)': '13.311.450'}, {'Produto': 'Espumante Orgânico', 'Quantidade (L.)': '742'}, {'Produto': 'SUCO DE UVAS', 'Quantidade (L.)': '144.889.668'}, {'Produto': 'Suco Natural Integral', 'Quantidade (L.)': '114.453.657'}, {'Produto': 'Suco Adoçado', 'Quantidade (L.)': '-'}, {'Produto': 'Suco Reprocessado/reconstituido', 'Quantidade (L.)': '22.066.742'}, {'Produto': 'Suco Orgânico', 'Quantidade (L.)': '553.391'}, {'Produto': 'Outros sucos de uvas', 'Quantidade (L.)': '7.815.879'}, {'Produto': 'SUCO DE UVAS CONCENTRADO', 'Quantidade (L.)': '22.422.414'}, {'Produto': 'OUTROS PRODUTOS COMERCIALIZADOS', 'Quantidade (L.)': '26.547.242'}, {'Produto': 'Outros vinhos (sem informação detalhada)', 'Quantidade (L.)': '192.057'}, {'Produto': 'Agrin (fermentado, acetico misto)', 'Quantidade (L.)': '-'}, {'Produto': 'Aguardente de vinho 50°gl', 'Quantidade (L.)': '866'}, {'Produto': 'Alcool vinico', 'Quantidade (L.)': '6.640'}, {'Produto': 'Bagaceira (graspa)', 'Quantidade (L.)': '7.610'}, {'Produto': 'Base champenoise champanha', 'Quantidade (L.)': '8.772'}, {'Produto': 'Base charmat champanha', 'Quantidade (L.)': '123'}, {'Produto': 'Base espumante moscatel', 'Quantidade (L.)': '23.703'}, {'Produto': 'Bebida de uva', 'Quantidade (L.)': '354.511'}, {'Produto': 'Borra líquida', 'Quantidade (L.)': '22.975'}, {'Produto': 'Borra seca', 'Quantidade (L.)': '146.260'}, {'Produto': 'Brandy (conhaque)', 'Quantidade (L.)': '7.966'}, {'Produto': 'Cooler', 'Quantidade (L.)': '6.260.381'}, {'Produto': 'Coquetel com vinho', 'Quantidade (L.)': '205.664'}, {'Produto': 'Destilado de vinho', 'Quantidade (L.)': '200'}, {'Produto': 'Filtrado doce', 'Quantidade (L.)': '2.415.338'}, {'Produto': 'Jeropiga', 'Quantidade (L.)': '1.267'}, {'Produto': 'Mistelas', 'Quantidade (L.)': '1.201'}, {'Produto': 'Mosto concentrado', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto de uva', 'Quantidade (L.)': '48.044'}, {'Produto': 'Mosto sulfitado', 'Quantidade (L.)': '-'}, {'Produto': 'Nectar de uva', 'Quantidade (L.)': '3.319.597'}, {'Produto': 'Outros produtos', 'Quantidade (L.)': '2.543.754'}, {'Produto': 'Polpa de uva', 'Quantidade (L.)': '1.129.453'}, {'Produto': 'Preparado líquido para refresco', 'Quantidade (L.)': '11.366'}, {'Produto': 'Refrigerante +50% suco', 'Quantidade (L.)': '144.945'}, {'Produto': 'Sangria', 'Quantidade (L.)': '11.017'}, {'Produto': 'Vinagre balsamico', 'Quantidade (L.)': '248.771'}, {'Produto': 'Vinagre duplo', 'Quantidade (L.)': '1.075.579'}, {'Produto': 'Vinagre simples', 'Quantidade (L.)': '6.049.584'}, {'Produto': 'Vinho acetificado', 'Quantidade (L.)': '1.879.227'}, {'Produto': 'Vinho base para espumantes', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho composto', 'Quantidade (L.)': '63.625'}, {'Produto': 'Vinho licoroso', 'Quantidade (L.)': '362.340'}, {'Produto': 'Vinho leve', 'Quantidade (L.)': '396'}, {'Produto': 'Vinho gaseificado', 'Quantidade (L.)': '4.012'}, {'Produto': 'Total', 'Quantidade (L.)': '458.907.154'}]"
}
```

#### Exports Wine Scraping (/api/exports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de exportação de vinhos
Exemplo requisição dados de 2019 e classificação 'subopt_03':
```
https://projeto-fiap.onrender.com/api/exports/?year=2019&classification=subopt_03
```
Exemplo retorno dados de 2019 e classificação 'subopt_03':
```
{
  "message": "[{'Países': 'Africa do Sul', 'Quantidade (Kg)': '8', 'Valor (US$)': '30'}, {'Países': 'Alemanha, República Democrática', 'Quantidade (Kg)': '1.863.097', 'Valor (US$)': '3.480.290'}, {'Países': 'Angola', 'Quantidade (Kg)': '75', 'Valor (US$)': '145'}, {'Países': 'Antígua e Barbuda', 'Quantidade (Kg)': '190', 'Valor (US$)': '580'}, {'Países': 'Arabia Saudita', 'Quantidade (Kg)': '167.731', 'Valor (US$)': '271.231'}, {'Países': 'Argélia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Argentina', 'Quantidade (Kg)': '1.186.878', 'Valor (US$)': '1.758.528'}, {'Países': 'Áustria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bahamas', 'Quantidade (Kg)': '2.869', 'Valor (US$)': '9.184'}, {'Países': 'Bahrein', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bangladesh', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Barbados', 'Quantidade (Kg)': '110', 'Valor (US$)': '354'}, {'Países': 'Barein', 'Quantidade (Kg)': '958', 'Valor (US$)': '3.353'}, {'Países': 'Bélgica', 'Quantidade (Kg)': '176.918', 'Valor (US$)': '336.252'}, {'Países': 'Belize', 'Quantidade (Kg)': '20', 'Valor (US$)': '48'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '228', 'Valor (US$)': '1.047'}, {'Países': 'Bolívia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bósnia', 'Quantidade (Kg)': '52', 'Valor (US$)': '67'}, {'Países': 'Brasil', 'Quantidade (Kg)': '18', 'Valor (US$)': '62'}, {'Países': 'Bulgária', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Burquina Faso', 'Quantidade (Kg)': '10', 'Valor (US$)': '37'}, {'Países': 'Cabo Verde', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Camarões', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Camores', 'Quantidade (Kg)': '20', 'Valor (US$)': '75'}, {'Países': 'Canadá', 'Quantidade (Kg)': '24.565', 'Valor (US$)': '220.025'}, {'Países': 'Catar', 'Quantidade (Kg)': '81', 'Valor (US$)': '298'}, {'Países': 'Cayman, Ilhas', 'Quantidade (Kg)': '216', 'Valor (US$)': '638'}, {'Países': 'Chile', 'Quantidade (Kg)': '189', 'Valor (US$)': '457'}, {'Países': 'China', 'Quantidade (Kg)': '1.113', 'Valor (US$)': '3.171'}, {'Países': 'Chipre', 'Quantidade (Kg)': '2.173', 'Valor (US$)': '6.326'}, {'Países': 'Cingapura', 'Quantidade (Kg)': '7.081', 'Valor (US$)': '23.803'}, {'Países': 'Cocos (Keeling), Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cook, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Colômbia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Congo', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Coreia do Norte', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Coreia do Sul', 'Quantidade (Kg)': '270', 'Valor (US$)': '620'}, {'Países': 'Costa do Marfim', 'Quantidade (Kg)': '16', 'Valor (US$)': '34'}, {'Países': 'Coveite', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Croácia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Curaçao', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Dinamarca', 'Quantidade (Kg)': '56.095', 'Valor (US$)': '130.520'}, {'Países': 'Djibuti', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Egito', 'Quantidade (Kg)': '20', 'Valor (US$)': '97'}, {'Países': 'Emirados Árabes Unidos', 'Quantidade (Kg)': '240.422', 'Valor (US$)': '697.259'}, {'Países': 'Eslovênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Espanha', 'Quantidade (Kg)': '1.094.483', 'Valor (US$)': '2.089.713'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '6.117.999', 'Valor (US$)': '16.239.149'}, {'Países': 'Falkland (Ilhas Malvinas)', 'Quantidade (Kg)': '20', 'Valor (US$)': '69'}, {'Países': 'Faroé, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Filipinas', 'Quantidade (Kg)': '594', 'Valor (US$)': '1.849'}, {'Países': 'Finlândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'França', 'Quantidade (Kg)': '3.091', 'Valor (US$)': '12.062'}, {'Países': 'Gabão', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Gana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Georgia', 'Quantidade (Kg)': '26.928', 'Valor (US$)': '56.010'}, {'Países': 'Gibraltar', 'Quantidade (Kg)': '231', 'Valor (US$)': '755'}, {'Países': 'Grécia', 'Quantidade (Kg)': '2.650', 'Valor (US$)': '7.171'}, {'Países': 'Guadalupe', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiana Francesa', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guine Equatorial', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Honduras', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '18.566', 'Valor (US$)': '118.440'}, {'Países': 'Ilha de Man', 'Quantidade (Kg)': '150', 'Valor (US$)': '440'}, {'Países': 'Ilhas Virgens', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Índia', 'Quantidade (Kg)': '560', 'Valor (US$)': '1.634'}, {'Países': 'Indonésia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Irã', 'Quantidade (Kg)': '509', 'Valor (US$)': '1.013'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '514.814', 'Valor (US$)': '1.113.084'}, {'Países': 'Islândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Itália', 'Quantidade (Kg)': '154', 'Valor (US$)': '387'}, {'Países': 'Japão', 'Quantidade (Kg)': '721', 'Valor (US$)': '2.182'}, {'Países': 'Jérsei', 'Quantidade (Kg)': '24', 'Valor (US$)': '58'}, {'Países': 'Jordânia', 'Quantidade (Kg)': '265', 'Valor (US$)': '171'}, {'Países': 'Letônia', 'Quantidade (Kg)': '30', 'Valor (US$)': '55'}, {'Países': 'Líbano', 'Quantidade (Kg)': '85', 'Valor (US$)': '177'}, {'Países': 'Libéria', 'Quantidade (Kg)': '9.242', 'Valor (US$)': '29.430'}, {'Países': 'Líbia', 'Quantidade (Kg)': '20', 'Valor (US$)': '44'}, {'Países': 'Lituânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '7', 'Valor (US$)': '19'}, {'Países': 'Macedônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Malásia', 'Quantidade (Kg)': '20', 'Valor (US$)': '58'}, {'Países': 'Malta', 'Quantidade (Kg)': '4.094', 'Valor (US$)': '11.635'}, {'Países': 'Marrocos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Marshall, Ilhas', 'Quantidade (Kg)': '9.668', 'Valor (US$)': '30.841'}, {'Países': 'Martinica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Mauricio', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Mauritânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Mexico', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Mônaco', 'Quantidade (Kg)': '20', 'Valor (US$)': '29'}, {'Países': 'Mongólia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Montenegro', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nigéria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Noruega', 'Quantidade (Kg)': '277.423', 'Valor (US$)': '638.830'}, {'Países': 'Omã', 'Quantidade (Kg)': '60', 'Valor (US$)': '193'}, {'Países': 'Países Baixos', 'Quantidade (Kg)': '19.526.035', 'Valor (US$)': '36.061.578'}, {'Países': 'Palau', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Panamá', 'Quantidade (Kg)': '8.349', 'Valor (US$)': '25.288'}, {'Países': 'Paquistão', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Paraguai', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Pitcairn', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Polônia', 'Quantidade (Kg)': '20', 'Valor (US$)': '53'}, {'Países': 'Porto Rico', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Portugal', 'Quantidade (Kg)': '945', 'Valor (US$)': '3.146'}, {'Países': 'Quirguistão', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '13.501.346', 'Valor (US$)': '29.677.591'}, {'Países': 'Republica Dominicana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Romênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Rússia,  Federação da', 'Quantidade (Kg)': '48.084', 'Valor (US$)': '101.082'}, {'Países': 'Samoa Americana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'São Cristóvão e Névis', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'São Tomé e Príncipe', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'São Vicente e Granadinas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Serra Leoa', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Senegal', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Singapura', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Sri Lanka', 'Quantidade (Kg)': '32', 'Valor (US$)': '80'}, {'Países': 'Suécia', 'Quantidade (Kg)': '72.036', 'Valor (US$)': '156.611'}, {'Países': 'Suíça', 'Quantidade (Kg)': '472', 'Valor (US$)': '3.661'}, {'Países': 'Suriname', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tailândia', 'Quantidade (Kg)': '879', 'Valor (US$)': '3.629'}, {'Países': 'Taiwan', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tanzânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Togo', 'Quantidade (Kg)': '13', 'Valor (US$)': '52'}, {'Países': 'Trindade e Tobago', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Turcas e Caicos, ilhas', 'Quantidade (Kg)': '10', 'Valor (US$)': '23'}, {'Países': 'Turquia', 'Quantidade (Kg)': '485', 'Valor (US$)': '1.399'}, {'Países': 'Tuvalu', 'Quantidade (Kg)': '6', 'Valor (US$)': '23'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '81.440', 'Valor (US$)': '98.329'}, {'Países': 'Vanuatu', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Venezuela', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Vietnã', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Provisão de Navios e Aeronaves', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '45.054.003', 'Valor (US$)': '93.432.574'}]"
}
```

#### Imports Wine Scraping (/api/imports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de importação de vinhos
Exemplo requisição dados de 2018 e classificação 'subopt_01':
```
https://projeto-fiap.onrender.com/api/imports/?year=2018&classification=subopt_01
```
Exemplo retorno dados de 2018 e classificação 'subopt_01':
```
{
  "message": "[{'Países': 'Africa do Sul', 'Quantidade (Kg)': '1.127.053', 'Valor (US$)': '3.574.371'}, {'Países': 'Alemanha', 'Quantidade (Kg)': '142.971', 'Valor (US$)': '516.975'}, {'Países': 'Argélia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Arábia Saudita', 'Quantidade (Kg)': '563', 'Valor (US$)': '3.249'}, {'Países': 'Argentina', 'Quantidade (Kg)': '15.221.318', 'Valor (US$)': '52.817.642'}, {'Países': 'Armênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Austrália', 'Quantidade (Kg)': '3.518', 'Valor (US$)': '21.664'}, {'Países': 'Áustria', 'Quantidade (Kg)': '513.995', 'Valor (US$)': '1.567.866'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bélgica', 'Quantidade (Kg)': '163', 'Valor (US$)': '1.201'}, {'Países': 'Bolívia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bósnia-Herzegovina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Brasil', 'Quantidade (Kg)': '18.040', 'Valor (US$)': '121.806'}, {'Países': 'Bulgária', 'Quantidade (Kg)': '16.166', 'Valor (US$)': '17.550'}, {'Países': 'Canada', 'Quantidade (Kg)': '301', 'Valor (US$)': '17.418'}, {'Países': 'Chile', 'Quantidade (Kg)': '51.104.825', 'Valor (US$)': '144.731.210'}, {'Países': 'China', 'Quantidade (Kg)': '5', 'Valor (US$)': '472'}, {'Países': 'Coreia do Sul, República', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Croácia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cuba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Emirados Árabes Unidos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Eslovênia', 'Quantidade (Kg)': '20.976', 'Valor (US$)': '68.521'}, {'Países': 'Eslováquia', 'Quantidade (Kg)': '10.800', 'Valor (US$)': '17.938'}, {'Países': 'Espanha', 'Quantidade (Kg)': '5.595.268', 'Valor (US$)': '19.353.631'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '548.655', 'Valor (US$)': '2.584.781'}, {'Países': 'França', 'Quantidade (Kg)': '4.653.789', 'Valor (US$)': '22.688.105'}, {'Países': 'Geórgia', 'Quantidade (Kg)': '8.164', 'Valor (US$)': '20.416'}, {'Países': 'Geórgia do Sul e Sandwich do Sul, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Grécia', 'Quantidade (Kg)': '41.601', 'Valor (US$)': '135.185'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hungria', 'Quantidade (Kg)': '23.742', 'Valor (US$)': '113.405'}, {'Países': 'Indonésia', 'Quantidade (Kg)': '36', 'Valor (US$)': '210'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '107', 'Valor (US$)': '954'}, {'Países': 'Israel', 'Quantidade (Kg)': '40.354', 'Valor (US$)': '182.017'}, {'Países': 'Itália', 'Quantidade (Kg)': '10.154.564', 'Valor (US$)': '34.857.594'}, {'Países': 'Japão', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Iugoslávia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Líbano', 'Quantidade (Kg)': '19.742', 'Valor (US$)': '150.044'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '5', 'Valor (US$)': '42'}, {'Países': 'Macedônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Marrocos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'México', 'Quantidade (Kg)': '134', 'Valor (US$)': '804'}, {'Países': 'Moldávia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Montenegro', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Noruega', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nova Zelândia', 'Quantidade (Kg)': '130.854', 'Valor (US$)': '686.193'}, {'Países': 'Países Baixos (Holanda)', 'Quantidade (Kg)': '283', 'Valor (US$)': '8.719'}, {'Países': 'Panamá', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Peru', 'Quantidade (Kg)': '77', 'Valor (US$)': '653'}, {'Países': 'Porto Rico', 'Quantidade (Kg)': '47', 'Valor (US$)': '404'}, {'Países': 'Portugal', 'Quantidade (Kg)': '17.698.831', 'Valor (US$)': '53.237.413'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '4.126', 'Valor (US$)': '51.034'}, {'Países': 'Republica Dominicana', 'Quantidade (Kg)': '2', 'Valor (US$)': '13'}, {'Países': 'Romênia', 'Quantidade (Kg)': '13.719', 'Valor (US$)': '9.695'}, {'Países': 'Rússia', 'Quantidade (Kg)': '17.483', 'Valor (US$)': '66.160'}, {'Países': 'San Marino', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Sérvia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Síria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suazilândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suíça', 'Quantidade (Kg)': '559', 'Valor (US$)': '7.647'}, {'Países': 'Tcheca, República', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tunísia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Turquia', 'Quantidade (Kg)': '1.591', 'Valor (US$)': '1.245'}, {'Países': 'Ucrânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '2.836.574', 'Valor (US$)': '8.467.846'}, {'Países': 'Não consta na tabela', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Não declarados', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Outros', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '109.971.001', 'Valor (US$)': '346.102.093'}]"
}
```
#### Processing Wine Scraping (/api/processing/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de processamento de vinhos
Exemplo requisição dados de 2017 e classificação 'subopt_02':
```
https://projeto-fiap.onrender.com/api/processing/?year=2017&classification=subopt_02
```
Exemplo retorno dados de 2020:
```
{
  "message": "[{'Países': 'África do Sul', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Alemanha', 'Quantidade (Kg)': '4.824', 'Valor (US$)': '28.799'}, {'Países': 'Angola', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Antigua e Barbuda', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Antilhas Holandesas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Argentina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Aruba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Australia', 'Quantidade (Kg)': '595', 'Valor (US$)': '2.276'}, {'Países': 'Bahamas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bangladesh', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Barbados', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Belgica', 'Quantidade (Kg)': '450', 'Valor (US$)': '2.646'}, {'Países': 'Benin', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bolívia', 'Quantidade (Kg)': '1.668', 'Valor (US$)': '21.056'}, {'Países': 'Bósnia-Herzegovina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bulgaria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cabo Verde', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Camarões', 'Quantidade (Kg)': '4.138', 'Valor (US$)': '16.077'}, {'Países': 'Canada', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Catar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cayman, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Chile', 'Quantidade (Kg)': '25.439', 'Valor (US$)': '231.696'}, {'Países': 'China', 'Quantidade (Kg)': '11.646', 'Valor (US$)': '35.671'}, {'Países': 'Chipre', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cingapura', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Colombia', 'Quantidade (Kg)': '595', 'Valor (US$)': '2.600'}, {'Países': 'Coreia do Sul, Republica da', 'Quantidade (Kg)': '442', 'Valor (US$)': '1.470'}, {'Países': 'Costa Rica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cuba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Curaçao', 'Quantidade (Kg)': '991', 'Valor (US$)': '5.808'}, {'Países': 'Dinamarca', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Dominica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'El Salvador', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Emirados Arabes Unidos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Equador', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Espanha', 'Quantidade (Kg)': '5.013', 'Valor (US$)': '64.735'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '22.605', 'Valor (US$)': '170.620'}, {'Países': 'Estonia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Falkland (Malvinas)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Filipinas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Filânldia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'França', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Gana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Gibraltar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Granada', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Grécia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guatemala', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiana', 'Quantidade (Kg)': '4', 'Valor (US$)': '61'}, {'Países': 'Guiné Equatorial', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiné-Bissau', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Haiti', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Honduras', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '450', 'Valor (US$)': '2.705'}, {'Países': 'Hungria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Ilha de Man', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Índia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Iraque', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Islândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Itália', 'Quantidade (Kg)': '1.467', 'Valor (US$)': '8.382'}, {'Países': 'Japão', 'Quantidade (Kg)': '48.604', 'Valor (US$)': '133.203'}, {'Países': 'Jordânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Letônia', 'Quantidade (Kg)': '158', 'Valor (US$)': '2.426'}, {'Países': 'Líbano', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Libéria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '360', 'Valor (US$)': '1.825'}, {'Países': 'Maldivas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Malta', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Marshall, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Montenegro', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'México', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nicarágua', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nigéria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Noruega', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nova Zelândia', 'Quantidade (Kg)': '196', 'Valor (US$)': '1.021'}, {'Países': 'Países Baixos (Holanda)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Panamá', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Paraguai', 'Quantidade (Kg)': '80.951', 'Valor (US$)': '255.320'}, {'Países': 'Peru', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Polônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Porto Rico', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Portugal', 'Quantidade (Kg)': '756', 'Valor (US$)': '11.568'}, {'Países': 'Quênia', 'Quantidade (Kg)': '100', 'Valor (US$)': '1.512'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '27.700', 'Valor (US$)': '101.672'}, {'Países': 'Republica Dominicana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Republica Tcheca', 'Quantidade (Kg)': '207', 'Valor (US$)': '942'}, {'Países': 'Rússia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Serra Leoa', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Singapura', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suécia', 'Quantidade (Kg)': '298', 'Valor (US$)': '1.136'}, {'Países': 'Suíça', 'Quantidade (Kg)': '1.890', 'Valor (US$)': '16.884'}, {'Países': 'Suriname', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tailândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Taiwan (Formosa)', 'Quantidade (Kg)': '1.507', 'Valor (US$)': '6.574'}, {'Países': 'Tcheca, República', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Trinidade e Tobago', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Turquia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '13.237', 'Valor (US$)': '48.581'}, {'Países': 'Vanuatu', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Venezuela', 'Quantidade (Kg)': '455', 'Valor (US$)': '2.205'}, {'Países': 'Vietnã', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Outros(1)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '256.746', 'Valor (US$)': '1.179.471'}]"
}
```
#### Production Wine Scraping (/api/production/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de produção de vinhos
Exemplo requisição dados de 2020:
```
https://projeto-fiap.onrender.com/api/production/?year=2016
```
Exemplo retorno dados de 2020:
```
{
  "message": "[{'Produto': 'VINHO DE MESA', 'Quantidade (L.)': '86.319.015'}, {'Produto': 'Tinto', 'Quantidade (L.)': '75.279.191'}, {'Produto': 'Branco', 'Quantidade (L.)': '10.727.099'}, {'Produto': 'Rosado', 'Quantidade (L.)': '312.725'}, {'Produto': 'VINHO FINO DE MESA (VINIFERA)', 'Quantidade (L.)': '18.070.626'}, {'Produto': 'Tinto', 'Quantidade (L.)': '8.774.847'}, {'Produto': 'Branco', 'Quantidade (L.)': '8.705.066'}, {'Produto': 'Rosado', 'Quantidade (L.)': '590.713'}, {'Produto': 'SUCO', 'Quantidade (L.)': '42.210.389'}, {'Produto': 'Suco de uva integral', 'Quantidade (L.)': '31.117.869'}, {'Produto': 'Suco de uva concentrado', 'Quantidade (L.)': '11.092.520'}, {'Produto': 'Suco de uva adoçado', 'Quantidade (L.)': '-'}, {'Produto': 'Suco de uva orgânico', 'Quantidade (L.)': '-'}, {'Produto': 'Suco de uva reconstituído', 'Quantidade (L.)': '-'}, {'Produto': 'DERIVADOS', 'Quantidade (L.)': '53.950.314'}, {'Produto': 'Espumante', 'Quantidade (L.)': '1.500'}, {'Produto': 'Espumante moscatel', 'Quantidade (L.)': '100.000'}, {'Produto': 'Base espumante', 'Quantidade (L.)': '-'}, {'Produto': 'Base espumante moscatel', 'Quantidade (L.)': '1.325.700'}, {'Produto': 'Base Champenoise champanha', 'Quantidade (L.)': '740.395'}, {'Produto': 'Base Charmat champanha', 'Quantidade (L.)': '250.280'}, {'Produto': 'Bebida de uva', 'Quantidade (L.)': '3.474'}, {'Produto': 'Polpa de uva', 'Quantidade (L.)': '1.620.430'}, {'Produto': 'Mosto simples', 'Quantidade (L.)': '49.770.993'}, {'Produto': 'Mosto concentrado', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto de uva com bagaço', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto dessulfitado', 'Quantidade (L.)': '-'}, {'Produto': 'Mistelas', 'Quantidade (L.)': '-'}, {'Produto': 'Néctar de uva', 'Quantidade (L.)': '-'}, {'Produto': 'Licorosos', 'Quantidade (L.)': '-'}, {'Produto': 'Compostos', 'Quantidade (L.)': '-'}, {'Produto': 'Jeropiga', 'Quantidade (L.)': '-'}, {'Produto': 'Filtrado', 'Quantidade (L.)': '-'}, {'Produto': 'Frisante', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho leve', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho licoroso', 'Quantidade (L.)': '24.200'}, {'Produto': 'Brandy', 'Quantidade (L.)': '-'}, {'Produto': 'Destilado', 'Quantidade (L.)': '-'}, {'Produto': 'Bagaceira', 'Quantidade (L.)': '1.000'}, {'Produto': 'Licor de bagaceira', 'Quantidade (L.)': '-'}, {'Produto': 'Vinagre', 'Quantidade (L.)': '5.000'}, {'Produto': 'Borra líquida', 'Quantidade (L.)': '24.975'}, {'Produto': 'Borra seca', 'Quantidade (L.)': '82.367'}, {'Produto': 'Vinho Composto', 'Quantidade (L.)': '-'}, {'Produto': 'Pisco', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho orgânico', 'Quantidade (L.)': '-'}, {'Produto': 'Espumante orgânico', 'Quantidade (L.)': '-'}, {'Produto': 'Destilado alcoólico simples de bagaceira', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho acidificado', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto parcialmente fermentado', 'Quantidade (L.)': '-'}, {'Produto': 'Outros derivados', 'Quantidade (L.)': '-'}, {'Produto': 'Total', 'Quantidade (L.)': '200.550.344'}]"
}
```
