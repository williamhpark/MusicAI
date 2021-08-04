export const initChoices = (choices) => {
  return {
    type: 'INIT_CHOICES',
    payload: choices,
  };
};

export const addChoice = (row, column, value) => {
  return {
    type: 'ADD_CHOICE',
    payload: {
      row,
      column,
      value: value - 1,
    },
  };
};

export const removeChoice = (row, column, value) => {
  return {
    type: 'REMOVE_CHOICE',
    payload: {
      row,
      column,
      value: value - 1,
    },
  };
};
