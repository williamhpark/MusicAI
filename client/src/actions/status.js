export const setSolvable = (value) => {
  return {
    type: 'SET_SOLVABLE',
    payload: value,
  };
};

export const setSolved = (value) => {
  return {
    type: 'SET_SOLVED',
    payload: value,
  };
};
