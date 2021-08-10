const selectedCellReducer = (state = null, action) => {
  switch (action.type) {
    case 'SELECT_CELL':
      return action.payload;
    default:
      return state;
  }
};

export default selectedCellReducer;
