import Section from "./components/Section";
import Tabs from "./components/Tabs"; // Importa o componente Tabs
import { fetchProductionByYear } from "./services/production";
import { fetchComerceByYear } from "./services/comerce";
import { fetchImportsByYear } from "./services/imports";
import { fetchExportsByYear } from "./services/exports";
import "./App.css";

const App = () => {
  return (
    <div className="container">
      <h1>Consulta aos dados da Embrapa</h1>

      {/* Configuração das Abas */}
      <Tabs
        tabs={[
          {
            label: "Produção",
            content: (
              <Section
                title="Buscar Produção por Ano"
                inputs={[
                  { name: "year", placeholder: "Digite o ano", type: "number" } // Input para ano
                ]}
                handler={fetchProductionByYear}
              />
            ),
          },
          {
            label: "Processamento por Ano e Classificação",
            content: (
              <Section
                title="Buscar Processamento por Ano e Classificação"
                inputs={[
                  { name: "year", placeholder: "Digite o ano", type: "number" },
                  {
                    name: "classification",
                    type: "select",
                    options: [
                      { value: "subopt_01", label: "Viníferas" },
                      { value: "subopt_02", label: "Americanas e híbridas" },
                      { value: "subopt_03", label: "Uvas de mesa" },
                      { value: "subopt_04", label: "Sem classificação" },
                    ],
                  },
                ]}
                handler={fetchComerceByYear}
              />
            ),
          },
          {
            label: "Comercialização",
            content: (
              <Section
                title="Buscar Comercialização por Ano"
                inputs={[
                  { name: "year", placeholder: "Digite o ano", type: "number" } // Input para ano
                ]}
                handler={fetchComerceByYear}
              />
            ),
          },
          {
            label: "Importação",
            content: (
              <Section
                title="Buscar Importação por Ano"
                inputs={[
                  { name: "year", placeholder: "Digite o ano", type: "number" },
                  {
                    name: "classification",
                    type: "select",
                    options: [
                      { value: "subopt_01", label: "Vinhos de Mesa" },
                      { value: "subopt_02", label: "Espumantes" },
                      { value: "subopt_03", label: "Uvas Frescas" },
                      { value: "subopt_04", label: "Uvas passas" },
                      { value: "subopt_05", label: "Sucos de Uva" }
                    ],
                  },
                ]}
                handler={fetchImportsByYear}
              />
            ),
          },
          {
            label: "Exportação",
            content: (
              <Section
                title="Buscar Produção por Ano"
                inputs={[
                  { name: "year", placeholder: "Digite o ano", type: "number" }, // Input para ano
                  {
                    name: "classification",
                    type: "select",
                    options: [
                      { value: "subopt_01", label: "Vinhos de Mesa" },
                      { value: "subopt_02", label: "Espumantes" },
                      { value: "subopt_03", label: "Uvas Frescas" },
                      { value: "subopt_04", label: "Sucos de Uva" },
                    ],
                  },
                ]}
                handler={fetchExportsByYear}
              />
            ),
          }
        ]}
      />
    </div>
  );
};

export default App;
