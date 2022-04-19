import styled from "styled-components";
import { COLORS } from "../../../Constants/Colors";
import { SIZES } from "../../../Constants/Sizes";

export const SelectContainer = styled.select`
  width: max-content;
  padding: ${SIZES.extraSmall} ${SIZES.small};
  border: none;
  background-color: ${COLORS.greyLight};
  color: ${COLORS.text};
  font-size: ${SIZES.normal};
  margin-top: ${SIZES.medium};
`;
