import styled from "styled-components";
import { COLORS } from "../../constants/colors";

export const NavContent = styled.nav`
  background: white;
  grid-area: nav;
  display: flex;
  align-items: center;
  padding: 0 2em;
  z-index: 1;
  box-shadow: rgba(17, 17, 26, 0.1) 0px 1px 0px;
`;

export const NavLogo = styled.div`
  flex-grow: 1;
  display: flex;

  a {
    color: ${COLORS.primary};
    font-size: 1.25em;
    transition: 100ms;
  }

  a:hover {
    color: ${COLORS.primaryLight};
  }
`;

export const NavConfig = styled.div`
  margin-right: 1em;
`;

export const NavConfigIcon = styled.a`
  color: #bbb;
  background-color: #f2f2f2;
  padding: 0.5em;
  border-radius: 10px;
  display: flex;
  align-items: center;
  cursor: pointer;
  justify-content: center;
  transition: 200ms;
`;

export const NavUserInfo = styled.div`
  color: ${COLORS.primary};
  background-color: ${COLORS.primaryOpacity};
  padding: 0.5em 0.75em;
  border-radius: 10px;
  cursor: pointer;
`;

export const NavUserName = styled.span`
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 190px;
`;

export const NavUserInfoContent = styled.div`
  position: absolute;
  margin-top: 12px;
  border-radius: 10px;
  display: grid;
  height: 0;
  overflow: hidden;
  transition: 200ms;
  transition-delay: 100ms;
  width: calc(190px - 2em + 0.75em * 2);
  margin-left: calc(((190px + 0.75em * 2) - (190px + 0.75em)) * -1);
  background-color: white;
  padding: 0em 1em;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;

  ${NavUserInfo}:hover & {
    transition-delay: 0s;
    height: calc(30px * 2);
    padding: 1em 1em;
  }
`;

export const NavLink = styled.a`
  color: #bbb;
  font-size: 0.9em;
  text-align: left;
  border-bottom: 1px solid #eee;
  height: 30px;
  margin-bottom: 15px;

  &:last-of-type {
    border-bottom: none;
  }
`;
