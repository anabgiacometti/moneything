import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const ButtonContainer = styled.button`
  display: flex;
  padding: ${SIZES.extraSmall} ${SIZES.small};
  font-size: ${SIZES.normal};
  text-transform: uppercase;
  font-weight: 500;
  border-radius: 7px;
  box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;
  border: none;
  color: ${(props) => (props.disabled ? "#ccc" : COLORS.primary)};
  background-color: ${(props) =>
    props.disabled ? "#f2f2f2" : COLORS.primaryOpacity};
  transition: 100ms;
  cursor: ${(props) => (props.disabled ? "default" : "pointer")};

  &:active {
    background-color: ${(props) =>
      props.disabled ? "#f2f2f2" : COLORS.primaryLight};
    color: ${(props) => (props.disabled ? "#ccc" : "white")};
  }

  & svg {
    margin-left: 10px;
  }
`;
