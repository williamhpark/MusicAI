import { combineReducers } from 'redux';

import boardReducer from './board';
import choicesReducer from './choices';
import selectedCellReducer from './selectedCell';

const rootReducer = combineReducers({
  board: boardReducer,
  choices: choicesReducer,
  selectedCell: selectedCellReducer,
});

export default rootReducer;
