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

- **200 OK: Requisição bem sucedida**
- **400 Bad Request: A requisição está incorreta em seus valores.**
- **500 Internal Server Error: Ocorreu um erro interno no servidor, não foi possível conectar ao site da Embrapa.**

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

#### Imports Wine Scraping (/api/imports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de importação de vinhos

#### Processing Wine Scraping (/api/processing/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de processamento de vinhos

#### Production Wine Scraping (/api/production/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de produção de vinhos
  
