import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
// import { makeStyles } from '@material-ui/core/styles';
import { Button } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';

import actions from '../actions';

// const useStyles = makeStyles({
//   root: {
//     borderRadius: '50%',
//   },
// });

const NumberButton = ({ value }) => {
  const selectedCell = useSelector((state) => state.selectedCell);
  const dispatch = useDispatch();

  //   const classes = useStyles();

  const addEntryToBoard = () => {
    if (selectedCell && value !== selectedCell.value) {
      dispatch(actions.removeEntry(selectedCell.row, selectedCell.column));
      dispatch(actions.removeChoice(selectedCell.row, selectedCell.column, selectedCell.value));
      dispatch(actions.selectCell(selectedCell.row, selectedCell.column, null));
      if (value !== null) {
        dispatch(actions.addEntry(selectedCell.row, selectedCell.column, value));
        dispatch(actions.addChoice(selectedCell.row, selectedCell.column, value));
        dispatch(actions.selectCell(selectedCell.row, selectedCell.column, value));
      }
    }
  };

  return (
    <Button onClick={() => addEntryToBoard()}>
      {value !== null ? value : <DeleteIcon fontSize="small" />}
    </Button>
  );
};

export default NumberButton;
