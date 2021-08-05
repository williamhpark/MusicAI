import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Board from './Board';
import ButtonRow from './ButtonRow';

const useStyles = makeStyles({
  root: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
});

const Game = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Board />
      <ButtonRow />
    </div>
  );
};

export default Game;
