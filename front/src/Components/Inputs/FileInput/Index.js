import { useRef, useState } from "react";
import { FiUpload } from "react-icons/fi";
import { FileInputContainer, FileInputLabel } from "./Styles";

const DEFAULT_LABEL = "Escolha os arquivos";

const FileInput = ({ handleChange }) => {
  const FileUploadRef = useRef();
  const [Label, SetLabel] = useState(DEFAULT_LABEL);

  const handleClick = () => {
    FileUploadRef.current.click();
  };

  const handleFileUpload = (event) => {
    const files = event.target.files;
    const label = [...files].map((file) => file.name).join(", ");
    handleChange(files);
    SetLabel(label);
  };

  return (
    <FileInputContainer>
      <FileInputLabel onClick={handleClick}>
        <FiUpload />
        {Label}
      </FileInputLabel>
      <input
        type={"file"}
        multiple
        ref={FileUploadRef}
        onChange={handleFileUpload}
      />
    </FileInputContainer>
  );
};

export default FileInput;
