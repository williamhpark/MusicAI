export const initBoard = (board) => {
  return {
    type: 'INIT_BOARD',
    payload: board,
  };
};

export const addEntry = (row, column, value) => {
  return {
    type: 'ADD_ENTRY',
    payload: {
      row,
      column,
      value,
    },
  };
};

export const removeEntry = (row, column) => {
  return {
    type: 'REMOVE_ENTRY',
    payload: {
      row,
      column,
    },
  };
};
