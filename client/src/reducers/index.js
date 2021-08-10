import { combineReducers } from 'redux';

import boardReducer from './board';
import choicesReducer from './choices';
import selectedCellReducer from './selectedCell';
import statusReducer from './status';

const rootReducer = combineReducers({
  board: boardReducer,
  choices: choicesReducer,
  selectedCell: selectedCellReducer,
  status: statusReducer,
});

export default rootReducer;
