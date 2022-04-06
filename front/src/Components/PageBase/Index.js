import React from "react";
import { Link } from "react-router-dom";
import NavBar from "../NavBar/Index.js";
import {
  Container,
  Content,
  SideBar,
  ContentBox,
} from "./Styles.js";

const PageBase = () => {
  return (
    <Container>
      <NavBar>NavBar</NavBar>
      <ContentBox>
        <Content>Content</Content>
      </ContentBox>
    </Container>
  );
};

export default PageBase;
