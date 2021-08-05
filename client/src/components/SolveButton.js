import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Button } from '@material-ui/core';
import BuildIcon from '@material-ui/icons/Build';

import actions from '../actions';

const SolveButton = () => {
  const board = useSelector((state) => state.board);
  const choices = useSelector((state) => state.choices);
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
        dispatch(actions.addEntry(row, col, num));
        dispatch(actions.addChoice(row, col, num));
        solveBoard(board);
      }
    }

    if (nextEmptySpot()[0] !== -1) {
      dispatch(actions.removeEntry(row, col));
      dispatch(actions.removeChoice(row, col, board[row][col].value));
    }
  };

  return (
    <Button onClick={() => solveBoard()}>
      <BuildIcon />
    </Button>
  );
};

export default SolveButton;
