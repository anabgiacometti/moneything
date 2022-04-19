import { ButtonContainer } from "./Styles";

const Button = ({ children, disabled, onClick }) => {
  return (
    <ButtonContainer disabled={disabled} onClick={onClick}>
      {children}
    </ButtonContainer>
  );
};

export default Button;
