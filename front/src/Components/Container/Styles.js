import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const ContainerContent = styled.div`
  padding: ${SIZES.large};
  margin: ${SIZES.normal} 0;
  border-bottom: 3px solid ${COLORS.primaryLight};
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.04) 0px 3px 5px;
  display: flex;
  justify-content: ${(props) => props.justifyContent || "center"};
`;
