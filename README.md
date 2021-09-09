# 🧩 Sudoku Solver

An application that converts any image of a standard 9X9 Sudoku board from Google Images into a digital board that can be filled and edited from the site's interface.

The machine learning model to recognize the digits within the images fed to it was developed using PyTorch and trained using the MNIST dataset, and the borders of the board were differentiated during the extraction of the cells using OpenCV.

The "Solve" fucntionality (for when the user wants the board to solve itself) was implemented using a backtracking algorithm. Here's the relevant code snippet:

```
const board = useSelector((state) => state.board); // A 2-D array representing the Sudoku board
const choices = useSelector((state) => state.choices); // A hash table tracking how many times each digit appears in each row, column, and square
const dispatch = useDispatch();

const nextEmptySpot = () => {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j].value === null) return [i, j];
    }
  }
  return [-1, -1];
};

const isSafe = (row, column, value) => {
  return (
    choices.rows[row][value - 1] === 0 &&
    choices.columns[column][value - 1] === 0 &&
    choices.squares[Math.floor(row / 3) * 3 + Math.floor(column / 3)][value - 1] === 0
  );
};

const solveBoard = () => {
  const [row, col] = nextEmptySpot();

  // There are no more empty spots
  if (row === -1) {
    return;
  }

  for (let num = 1; num <= 9; num++) {
    if (isSafe(row, col, num)) {
      dispatch(actions.selectCell(row, col, num));
      dispatch(actions.addEntry(row, col, num));
      dispatch(actions.addChoice(row, col, num));
      solveBoard(board); // Call the function recursively
    }
  }

  if (nextEmptySpot()[0] !== -1) {
    dispatch(actions.selectCell(row, col, board[row][col].value));
    dispatch(actions.removeEntry(row, col));
    dispatch(actions.removeChoice(row, col, board[row][col].value));
  }
};
```
