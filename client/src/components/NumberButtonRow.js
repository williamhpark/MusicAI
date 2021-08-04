import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import NumberButton from './NumberButton';

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
    buttons.push(<NumberButton value={i}></NumberButton>);
  }
  buttons.push(<NumberButton value={null}></NumberButton>);

  return <div className={classes.root}>{buttons}</div>;
};

export default NumberButtonRow;
