import Section from "./components/Section";
import Tabs from "./components/Tabs"; // Importa o componente Tabs
import {
  fetchProductionByYear,
} from "./services/production";
import {
  fetchComerceByYear,
} from "./services/comerce";
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
                placeholder="Digite o ano..."
                handler={fetchProductionByYear}
              />
            ),
          },
          {
            label: "Processamento",
            content: (
              <Section
                title="Buscar Processamento"
                placeholder="Digite o ano..."
                handler={fetchProductionByYear}
              />
            ),
          },
          {
            label: "Comercialização",
            content: (
              <Section
                title="Buscar Comercialização"
                placeholder="Digite o ano..."
                handler={fetchComerceByYear}
              />
            ),
          },
          {
            label: "Importação",
            content: (
              <Section
                title="Buscar Importação"
                placeholder="Digite o ano..."
                handler={fetchProductionByYear}
              />
            ),
          },
          {
            label: "Exportação",
            content: (
              <Section
                title="Buscar Exportação"
                placeholder="Digite o ano..."
                handler={fetchProductionByYear}
              />
            ),
          }
        ]}
      />
    </div>
  );
};

export default App;
