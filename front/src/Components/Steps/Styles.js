import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const StepContainer = styled.section`
  width: 100%;
  display: flex;
`;

export const StepList = styled.div`
  width: 150px;
  min-width: 150px;
  border-right: 1px solid ${COLORS.greyLight};
  padding: ${SIZES.medium} 0;
  height: 80vh;
`;

export const StepTitle = styled.p`
  font-size: ${SIZES.normal};
  color: ${COLORS.text};
  font-weight: 400;
  border-radius: 10px 0 0 10px;
  background-color: ${(props) =>
    props.current >= props.index ? COLORS.primaryOpacity : COLORS.greyLight};
  color: ${(props) =>
    props.current >= props.index ? COLORS.primaryLight : COLORS.grey};
  padding: ${SIZES.extraSmall} ${SIZES.small};
  margin: ${SIZES.extraSmall} 0;
  text-transform: capitalize;
  cursor: pointer;
`;

export const StepCount = styled.span`
  font-weight: 800;
`;

export const StepContent = styled.div`
  display: ${(props) => (props.isActive ? "block" : "none")};
  width: 100%;
  padding: ${SIZES.medium} ${SIZES.gigantic};
`;

export const StepButton = styled.section`
  margin-top: ${SIZES.medium};
`;
