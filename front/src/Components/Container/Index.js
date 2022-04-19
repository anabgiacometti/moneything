import { ContainerContent } from "./Styles";

const Container = ({ children, justifyContent }) => {
  return (
    <ContainerContent justifyContent={justifyContent}>
      {children}
    </ContainerContent>
  );
};

export default Container;
