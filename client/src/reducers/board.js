const boardReducer = (state = [], action) => {
  switch (action.type) {
    case 'INIT_BOARD':
      return action.payload;
    case 'ADD_ENTRY':
      return state.map((row, i) => {
        if (i === action.payload.row) {
          return row.map((cell, j) => {
            if (j === action.payload.column) {
              cell.value = action.payload.value;
            }
            return cell;
          });
        }
        return row;
      });
    case 'REMOVE_ENTRY':
      return state.map((row, i) => {
        if (i === action.payload.row) {
          return row.map((cell, j) => {
            if (j === action.payload.column) {
              cell.value = null;
            }
            return cell;
          });
        }
        return row;
      });
    default:
      return state;
  }
};

export default boardReducer;
