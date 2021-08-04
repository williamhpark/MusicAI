export const selectCell = (row, column, value) => {
  return {
    type: 'SELECT_CELL',
    payload: {
      row,
      column,
      value,
    },
  };
};
