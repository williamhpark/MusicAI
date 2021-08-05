const solvedReducer = (state = {}, action) => {
  switch (action.type) {
    case 'SET_SOLVABLE':
      return {
        ...state,
        solvable: action.payload,
      };
    case 'SET_SOLVED':
      return {
        ...state,
        solved: action.payload,
      };
    default:
      return state;
  }
};

export default solvedReducer;
