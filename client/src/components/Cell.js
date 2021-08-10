import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { makeStyles } from '@material-ui/core/styles';

import actions from '../actions';

const getBackgroundColor = (isSelected, isPeer, isSameValue, isConflict) => {
  if (isSelected) {
    return '#3299CC';
  } else if (isPeer || isSameValue) {
    return '#82CFFD';
  } else if (isConflict) {
    return '#F7BEC0';
  } else {
    return '#FFFFFF';
  }
};

const getFontColor = (isPrefilled, isConflict) => {
  if (isConflict) {
    return '#FF0000';
  } else if (isPrefilled) {
    return '#000000';
  } else {
    return '#00FF00';
  }
};

const useStyles = makeStyles({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    cursor: 'pointer',
    aspectRatio: 1,
    background: (props) =>
      getBackgroundColor(props.isSelected, props.isPeer, props.isSameValue, props.isConflict),
    '& p': {
      color: (props) => getFontColor(props.isPrefilled, props.isConflict),
    },
  },
});

const Cell = ({ row, column, value, isPrefilled }) => {
  const board = useSelector((state) => state.board);
  const choices = useSelector((state) => state.choices);
  const selectedCell = useSelector((state) => state.selectedCell);
  const dispatch = useDispatch();

  const isPeer = (a, b) => {
    if (!a || !b) return false;
    const squareA = Math.floor(a.row / 3) * 3 + Math.floor(a.column / 3);
    const squareB = Math.floor(b.row / 3) * 3 + Math.floor(b.column / 3);
    return a.row === b.row || a.column === b.column || squareA === squareB;
  };

  const isConflict = (i, j) => {
    const { value } = board[i][j];
    if (!value) return false;
    const rowConflict = choices.rows[i][value - 1] > 1;
    const columnConflict = choices.columns[j][value - 1] > 1;
    const squareConflict =
      choices.squares[Math.floor(i / 3) * 3 + Math.floor(j / 3)][value - 1] > 1;
    return rowConflict || columnConflict || squareConflict;
  };

  const selected = !!(selectedCell && row === selectedCell.row && column === selectedCell.column);
  const peer = isPeer({ row, column }, selectedCell);
  const sameValue = !!(selectedCell && selectedCell.value && value === selectedCell.value);
  const conflict = isConflict(row, column);

  const styleProps = {
    isPrefilled,
    isSelected: selected,
    isPeer: peer,
    isSameValue: sameValue,
    isConflict: conflict,
  };

  const classes = useStyles(styleProps);

  return (
    <div
      className={classes.root}
      onClick={() => {
        dispatch(actions.selectCell(row, column, value));
      }}
    >
      <p>{value && value}</p>
    </div>
  );
};

export default Cell;
