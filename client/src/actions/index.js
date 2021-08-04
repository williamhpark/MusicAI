import * as boardActions from './board';
import * as choicesActions from './choices';
import * as selectedCellActions from './selectedCell';

const actions = {
  ...boardActions,
  ...choicesActions,
  ...selectedCellActions,
};

export default actions;
