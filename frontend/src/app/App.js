import React from 'react';
import { Router, Route, hashHistory } from 'react-router'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {lightBlue500} from 'material-ui/styles/colors';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import AppBar from 'material-ui/AppBar';

import Home from './components/Home'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import User from './components/User'

const muiTheme = getMuiTheme({
  palette: {
    accent1Color: lightBlue500,
  },
});

const App = () => (
    <MuiThemeProvider muiTheme={muiTheme}>
      <div>
        <AppBar
          style={{ margin: 0 }}
          title="project-name-should-be-here"
          iconClassNameRight="muidocs-icon-navigation-expand-more"
        />
        <Router history={hashHistory}>
          <Route path="/" component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/user" component={User} />
        </Router>
      </div>
    </MuiThemeProvider>
);

export default App;
