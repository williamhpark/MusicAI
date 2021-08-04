import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Board from './Board';
import NumberButtonRow from './NumberButtonRow';

const useStyles = makeStyles({
  root: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
});

const Game = () => {
  // const [board, setBoard] = useState(); // [ [ { value, prefilled }, ... ], ... ]
  // const [choices, setChoices] = useState(); // { rows: [ [ ... ], ... ], columns: [ [ ... ], ... ], squares: [ [ ... ], ... ] }
  // const [selectedCell, setSelectedCell] = useState(); // { row, column, value }

  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Board />
      <NumberButtonRow />
    </div>
  );
};

export default Game;
