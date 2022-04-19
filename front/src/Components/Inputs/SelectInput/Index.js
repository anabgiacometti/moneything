import { SelectContainer } from "./Styles";

const SelectInput = ({ options, onSelect }) => {
  return (
    <SelectContainer
      defaultValue={""}
      onChange={(e) => onSelect(e.target.value)}
    >
      <option disabled value={""}>
        Escolha
      </option>
      {Object.keys(options).map((option) => (
        <option key={option} value={option}>
          {options[option]}
        </option>
      ))}
    </SelectContainer>
  );
};

export default SelectInput;
