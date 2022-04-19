import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const Container = styled.div`
  display: grid;
  height: 100vh;
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr;
  grid-template-areas:
    "nav"
    "content";
`;

export const ContentBox = styled.div`
  background-color: rgba(0, 0, 0, 0.01);
  padding: ${SIZES.large} ${SIZES.extraLarge};
  grid-area: content;
`;

export const Content = styled.div`
  display: flex;
  justify-content: center;
`;

export const Title = styled.h1`
  font-size: ${(props) => props.size || SIZES.medium};
  font-weight: 600;
  color: ${COLORS.text};
`;

export const SubTitle = styled.p`
  font-size: ${(props) => props.size || SIZES.normal};
  font-weight: 400;
  color: ${COLORS.grey};
`;

export const Input = styled.input``;
