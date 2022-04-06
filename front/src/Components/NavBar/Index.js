import React from "react";
import {
  NavContent,
  NavLogo,
  NavLink,
  NavUserInfo,
  NavConfig,
  NavConfigIcon,
  NavUserName,
  NavUserInfoContent,
} from "./Styles.js";
import { FiUser, FiLogOut, FiChevronDown, FiUpload } from "react-icons/fi";

const NavBar = () => {
  return (
    <NavContent>
      <NavLogo>
        <a href="/">Money Thing</a>
      </NavLogo>
      <NavConfig>
        <NavConfigIcon href="/import-csv">
          <FiUpload />
        </NavConfigIcon>
      </NavConfig>
      <NavUserInfo>
        <NavUserName>
          Ana Flávia Bortoli <FiChevronDown />
        </NavUserName>
        <NavUserInfoContent>
          <NavLink href="/import-csv">
            <FiUser style={{ marginRight: "5px" }} />
            Minha Conta
          </NavLink>
          <NavLink href="/import-csv">
            <FiLogOut style={{ marginRight: "5px" }} />
            Sair
          </NavLink>
        </NavUserInfoContent>
      </NavUserInfo>
    </NavContent>
  );
};

export default NavBar;
