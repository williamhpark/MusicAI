import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

import actions from '../actions';
import Cell from './Cell';

const useStyles = makeStyles({
  root: {
    border: '5px solid black',
    width: '900px',
    height: '900px',
    margin: '20px',
    background: '#000000',
  },
  board: {
    display: 'grid',
    gridTemplateColumns: 'repeat(9, 100px)',
    gridTemplateRows: 'repeat(9, 100px)',
    // gridGap: '1px',
  },
  // row: {
  //   '&:nth-child(3)': {
  //     marginRight: '5px',
  //   },
  // },
  // column: {
  //   '&:nth-child(3)': {
  //     marginBottom: '5px',
  //   },
  // },
});

const Board = () => {
  const board = useSelector((state) => state.board);
  const dispatch = useDispatch();

  const classes = useStyles();

  const generateBoard = (puzzle) => {
    // Initial count object to keep track of conflicts per number value
    const rows = new Array(9).fill(0).map(() => new Array(9).fill(0));
    const columns = new Array(9).fill(0).map(() => new Array(9).fill(0));
    const squares = new Array(9).fill(0).map(() => new Array(9).fill(0));
    const result = puzzle.map((row, i) =>
      row.map((cell, j) => {
        if (cell) {
          rows[i][cell - 1] += 1;
          columns[j][cell - 1] += 1;
          squares[Math.floor(i / 3) * 3 + Math.floor(j / 3)][cell - 1] += 1;
        }
        return {
          value: puzzle[i][j] > 0 ? puzzle[i][j] : null,
          prefilled: !!puzzle[i][j],
        };
      })
    );
    dispatch(actions.initBoard(result));
    dispatch(actions.initChoices({ rows, columns, squares }));
  };

  useEffect(() => {
    const validBoard = [
      [3, 3, 4, 6, 7, 8, 9, 1, null],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],

      [8, 5, 9, 7, null, 1, 4, 2, 3],
      [4, 2, null, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],

      [9, 6, 1, 5, 3, null, 2, 8, 4],
      [2, null, 7, 4, 1, 9, 6, 3, null],
      [3, 4, 5, 2, 8, 6, 1, 7, 7],
    ];
    generateBoard(validBoard);
  }, []);

  return (
    <div className={classes.root}>
      {board.length > 0 && (
        <div className={classes.board}>
          {board.map((row, i) => (
            <div key={`row-${i}`} className={classes.row}>
              {row.map((cell, j) => {
                return (
                  <div key={`column-${j}`} className={classes.column}>
                    <Cell row={i} column={j} value={cell.value} isPrefilled={cell.prefilled} />
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Board;
