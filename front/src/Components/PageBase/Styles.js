import styled from "styled-components";

export const Container = styled.div`
  display: grid;
  height: 100vh;
  color: white;
  grid-template-rows: 0.075fr 1fr;
  grid-template-columns: 1fr;
  grid-template-areas:
    "nav"
    "content";
  text-align: center;
`;

export const ContentBox = styled.div`
  background: white;
  grid-area: content;
`;

export const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

export const Content = styled.div``;
