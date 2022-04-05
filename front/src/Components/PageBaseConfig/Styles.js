import styled from "styled-components";

export const Container = styled.div`
  display: grid;
  height: 100vh;
  color: white;
  grid-template-rows: 0.075fr 1fr;
  grid-template-columns: 0.2fr 1fr;
  grid-template-areas:
    "nav nav"
    "sidebar content";
  text-align: center;
`;

export const SideBar = styled.div`
  background: #9aaab7;
  grid-area: sidebar;
`;

export const ContentBox = styled.div`
  background: #a6b8b9;
  grid-area: content;
`;

export const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

export const Content = styled.div``;
