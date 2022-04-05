import styled from "styled-components";

export const Content = styled.nav`
  background: white;
  grid-area: nav;
  color: palevioletred;
  display: grid;
  grid-template-rows: 0.075fr 1fr;
  grid-template-columns: 0.2fr 1fr;
  grid-template-areas: "logo links";
`;

export const Logo = styled.logo`
  grid-area: logo;
  background-color: red;
`;
