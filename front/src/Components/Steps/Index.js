import { useEffect, useState } from "react";
import Button from "../../Components/Button/Index";
import { FiArrowRight } from "react-icons/fi";
import {
  StepButton,
  StepContainer,
  StepContent,
  StepCount,
  StepList,
  StepTitle,
} from "./Styles";

const Steps = ({ steps }) => {
  const [ActiveStep, SetActiveStep] = useState(0);

  const handleStepChange = (selectedIndex) => {
    const isMovingBack = selectedIndex < ActiveStep;
    const isMovingFoward = selectedIndex > ActiveStep;
    const currentStepIsValid = steps[ActiveStep].isValid();
    const isLastStep = selectedIndex > steps.length;

    if ((isMovingFoward && currentStepIsValid && !isLastStep) || isMovingBack) {
      SetActiveStep(selectedIndex);
    }

    if (currentStepIsValid && steps[ActiveStep].onSubmit) {
      steps[ActiveStep].onSubmit();
    }
  };

  return (
    <StepContainer>
      <StepList>
        {steps.map((step, index) => {
          return (
            <StepTitle
              key={`step-${index}`}
              current={ActiveStep}
              index={index}
              onClick={() => handleStepChange(index)}
            >
              <StepCount>{index + 1}</StepCount> {step.title}
            </StepTitle>
          );
        })}
      </StepList>

      {steps.map((step, index) => (
        <StepContent
          isActive={ActiveStep === index}
          key={`step-content-${index}`}
        >
          {step.content}
          <StepButton>
            <Button
              disabled={!steps[index].isValid()}
              onClick={() => handleStepChange(ActiveStep + 1)}
            >
              Continuar <FiArrowRight />
            </Button>
          </StepButton>
        </StepContent>
      ))}
    </StepContainer>
  );
};

export default Steps;
