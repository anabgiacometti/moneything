import styled from "styled-components";
import { COLORS } from "../../Constants/Colors";
import { SIZES } from "../../Constants/Sizes";

export const Content = styled.div`
  min-width: 500px;
  width: 90vw;
`;

export const TableContainer = styled.table`
  margin-top: ${SIZES.medium};
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  min-width: 900px;
`;

export const TableHeaders = styled.thead`
  border-bottom: solid 2px ${COLORS.greyLight};
  & th {
    padding: ${SIZES.small};
    color: ${COLORS.text};
    text-transform: uppercase;
    font-size: ${SIZES.small};
    font-weight: 600;
    display: table-cell;
    align-items: center;
    cursor: pointer;
    text-align: left;
  }
`;

export const HeaderIcons = styled.span`
  margin-left: 10px;
`;

export const HeaderIcon = styled.i`
  color: ${(props) => (props.active ? COLORS.primary : COLORS.grey)};
`;

export const TableBody = styled.tbody`
  & tr > td {
    font-size: ${SIZES.small};
    text-overflow: ellipsis;
    padding: ${SIZES.extraSmall};
    max-width: 1px;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
  }
`;
