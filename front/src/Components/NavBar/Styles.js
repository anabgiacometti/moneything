import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const NavContent = styled.nav`
  background: white;
  grid-area: nav;
  display: flex;
  align-items: center;
  padding: 0 ${SIZES.gigantic};
  z-index: 1;
  box-shadow: rgba(17, 17, 26, 0.1) 0px 1px 0px;
`;

export const NavLogo = styled.div`
  flex-grow: 1;
  display: flex;

  a {
    color: ${COLORS.primary};
    font-size: ${SIZES.medium};
    transition: 100ms;
  }

  a:hover {
    color: ${COLORS.primaryLight};
  }
`;

export const NavConfig = styled.div`
  margin-right: ${SIZES.normal};
`;

export const NavConfigIcon = styled.a`
  color: #bbb;
  background-color: #f2f2f2;
  padding: ${SIZES.extraSmall};
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
  padding: ${SIZES.extraSmall} ${SIZES.small};
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
  padding: 0em ${SIZES.normal};
  box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;

  ${NavUserInfo}:hover & {
    transition-delay: 0s;
    height: calc(30px * 2 + ${SIZES.normal});
    padding: ${SIZES.normal} ${SIZES.normal};
  }

  hr {
    height: 1px;
    background-color: #eee;
    border: none;
    margin: 0.5em ${SIZES.normal};
  }
`;

export const NavLink = styled.a`
  color: #bbb;
  font-size: ${SIZES.small};
  text-align: left;
  height: 30px;
  display: flex;
  align-items: center;

  &:hover {
    color: ${COLORS.primary}
  }
`;
