import * as boardActions from './board';
import * as choicesActions from './choices';
import * as selectedCellActions from './selectedCell';
import * as statusActions from './status';

const actions = {
  ...boardActions,
  ...choicesActions,
  ...selectedCellActions,
  ...statusActions,
};

export default actions;
