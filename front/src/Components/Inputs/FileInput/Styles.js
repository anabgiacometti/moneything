import styled from "styled-components";
import { COLORS } from "../../../Constants/Colors";
import { SIZES } from "../../../Constants/Sizes";

export const FileInputContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: ${SIZES.medium};

  input {
    display: none;
  }
`;

export const FileInputLabel = styled.label`
  color: ${COLORS.text};
  display: flex;
  align-items: center;
  cursor: pointer;

  svg {
    margin-right: 15px;
    font-size: ${SIZES.large};
    color: ${COLORS.primary};
  }
`;
