import React from 'react';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';

const style = {
    margin: 0,
    top: 'auto',
    right: 20,
    bottom: 20,
    left: 'auto',
    position: 'fixed',
};

const App = () => (
    <div>
      <FloatingActionButton style={style}>
        <ContentAdd />
      </FloatingActionButton>
    </div>
);

export default App;
