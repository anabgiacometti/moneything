import React from "react";
import NavBar from "../NavBar/Index.js";
import {
  Container,
  Content,
  ContentBox,
} from "./Styles.js";

const PageBase = ({ children }) => {
  return (
    <Container>
      <NavBar />
      <ContentBox>
        <Content>{children}</Content>
      </ContentBox>
    </Container>
  );
};

export default PageBase;
