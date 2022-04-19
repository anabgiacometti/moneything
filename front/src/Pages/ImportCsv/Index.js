import axios from "axios";
import Steps from "../../Components/Steps/Index";
import { Content } from "./Styles";
import { useEffect, useState } from "react";
import { ENDPOINTS } from "../../Constants/Endpoints";
import { OriginContent, PreviewContent, UploadContent } from "./StepContents";

const ORIGIN_OPTIONS = { nubank: "Nubank" };

const ImportCSV = () => {
  const [UploadedFiles, SetUploadedFiles] = useState(null);
  const [Origin, SetOrigin] = useState("");
  const [Transactions, SetTransactions] = useState(null);

  useEffect(() => {
    SetUploadedFiles(null);
  }, [Origin]);

  const IMPORT_STEPS = [
    {
      title: "Origem",
      content: (
        <OriginContent
          handleSubmit={SetOrigin}
          selected={Origin}
          options={ORIGIN_OPTIONS}
        />
      ),
      isValid: () => !!Origin,
    },
    {
      title: "Arquivos",
      content: (
        <UploadContent
          origin={ORIGIN_OPTIONS[Origin]}
          handleSubmit={(files) => SetUploadedFiles(files[0])}
        />
      ),
      isValid: () => UploadedFiles,
      onSubmit: () => handleImport(true),
    },
    {
      title: "Preview",
      content: <PreviewContent transactions={Transactions} />,
      isValid: () => UploadedFiles,
    },
  ];

  const handleImport = (isPreview) => {
    const formData = new FormData();
    formData.append("files", UploadedFiles);
    axios
      .post(`${ENDPOINTS.transactions.import}?origin=${Origin}`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((res) => {
        console.log(res.data);
        SetTransactions(res.data);
      });
  };

  return (
    <Content>
      <Steps steps={IMPORT_STEPS} />
    </Content>
  );
};

export default ImportCSV;
