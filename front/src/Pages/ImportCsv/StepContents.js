import FileInput from "../../Components/Inputs/FileInput/Index";
import SelectInput from "../../Components/Inputs/SelectInput/Index";
import { SubTitle, Title } from "../../Components/PageBase/Styles";
import { SIZES } from "../../Constants/Sizes";
import {
  HeaderIcon,
  HeaderIcons,
  TableBody,
  TableContainer,
  TableHeaders,
} from "./Styles";
import { FiArrowUp, FiArrowDown } from "react-icons/fi";
import { useState } from "react";

export const OriginContent = ({ handleSubmit, selected, options }) => {
  return (
    <>
      <Title size={SIZES.large}>Qual a origem da importação?</Title>
      <SubTitle>
        Escolha abaixo a origem dos arquivos que serão importados.
      </SubTitle>
      <SelectInput
        onSelect={handleSubmit}
        selected={selected}
        options={options}
      />
    </>
  );
};

export const UploadContent = ({ origin, handleSubmit }) => {
  return (
    <>
      <Title size={SIZES.large}>
        Seleciona os arquivos do {origin} que serão importados
      </Title>
      <SubTitle>
        Escolha um ou mais arquivos para importar. Lembrando que por enquanto só
        conseguimos importar arquivos CSV.
      </SubTitle>
      <FileInput handleChange={handleSubmit} />
    </>
  );
};

export const PreviewContent = ({ transactions }) => {
  return (
    <>
      <Title size={SIZES.large}>Preview das transações importadas</Title>
      <SubTitle>
        Estas são as transaçoes que conseguimos identificar nos arquivos
        selecionados. Você pode cadastrar e vincular transações à novas
        categorias e/ou descrições antes de importa-las. Para finalizar a
        importação, verifique se as transações correspondem ao esperado e clique
        sem Salvar.
      </SubTitle>
      <Table data={transactions} />
    </>
  );
};

const Table = ({ data }) => {
  const columns = {
    date: "Data",
    payment_method: "Método",
    description: "Descrição",
    amount: "Valor",
    category: "Categoria",
    title: "Título",
  };

  const [Order, SetOrder] = useState({});

  const handleOrder = (column) => {
    SetOrder((current) => {
      const currentOrder = current[column];
      let incomingOrder = 0;
      if (!currentOrder) incomingOrder = 1;
      else if (currentOrder === 1) incomingOrder = -1;
      return { ...current, [column]: incomingOrder };
    });
  };

  const headers = (
    <tr>
      {Object.keys(columns).map((column) => (
        <th key={column} onClick={() => handleOrder(column)}>
          {columns[column]}
          <HeaderIcons>
            <HeaderIcon active={Order[column] === 1}>
              <FiArrowUp />
            </HeaderIcon>
            <HeaderIcon active={Order[column] === -1}>
              <FiArrowDown />
            </HeaderIcon>
          </HeaderIcons>
        </th>
      ))}
    </tr>
  );

  const body =
    data &&
    data.preview.map((row) => {
      return (
        <tr key={row.id_legacy}>
          {Object.keys(columns).map((column) => {
            return (
              <td title={row[column]} key={`${column}-${row.id_legacy}`}>
                {row[column] || "-"}
              </td>
            );
          })}
        </tr>
      );
    });

  return (
    <TableContainer>
      <TableHeaders>{headers}</TableHeaders>
      <TableBody>{body}</TableBody>
    </TableContainer>
  );
};
