import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import NumberButton from './NumberButton';
import SolveButton from './SolveButton';

const useStyles = makeStyles({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
});

const NumberButtonRow = () => {
  const classes = useStyles();

  const buttons = [];
  for (let i = 1; i < 10; i++) {
    buttons.push(<NumberButton value={i} />);
  }
  buttons.push(<NumberButton value={null} />);
  buttons.push(<SolveButton />);

  return <div className={classes.root}>{buttons}</div>;
};

export default NumberButtonRow;
