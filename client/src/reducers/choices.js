const createEmptyMatrix = () => {
  return new Array(9).fill(0).map(() => new Array(9).fill(0));
};

const INITIAL_STATE = {
  rows: createEmptyMatrix(),
  columns: createEmptyMatrix(),
  squares: createEmptyMatrix(),
};

const choicesReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case 'INIT_CHOICES':
      return action.payload;
    case 'ADD_CHOICE':
      return {
        rows: state.rows.map((row, i) => {
          if (i === action.payload.row) {
            return row.map((value, j) => {
              if (j === action.payload.value) {
                return value + 1;
              }
              return value;
            });
          }
          return row;
        }),
        columns: state.columns.map((column, i) => {
          if (i === action.payload.column) {
            return column.map((value, j) => {
              if (j === action.payload.value) {
                return value + 1;
              }
              return value;
            });
          }
          return column;
        }),
        squares: state.squares.map((square, i) => {
          if (
            i ===
            Math.floor(action.payload.row / 3) * 3 + Math.floor(action.payload.column / 3)
          ) {
            return square.map((value, j) => {
              if (j === action.payload.value) {
                return value + 1;
              }
              return value;
            });
          }
          return square;
        }),
      };
    case 'REMOVE_CHOICE':
      return {
        rows: state.rows.map((row, i) => {
          if (i === action.payload.row) {
            return row.map((value, j) => {
              if (j === action.payload.value && value > 0) {
                return value - 1;
              }
              return value;
            });
          }
          return row;
        }),
        columns: state.columns.map((column, i) => {
          if (i === action.payload.column) {
            return column.map((value, j) => {
              if (j === action.payload.value && value > 0) {
                return value - 1;
              }
              return value;
            });
          }
          return column;
        }),
        squares: state.squares.map((square, i) => {
          if (
            i ===
            Math.floor(action.payload.column / 3) * 3 + Math.floor(action.payload.column / 3)
          ) {
            return square.map((value, j) => {
              if (j === action.payload.value && value > 0) {
                return value - 1;
              }
              return value;
            });
          }
          return square;
        }),
      };
    default:
      return state;
  }
};

export default choicesReducer;
