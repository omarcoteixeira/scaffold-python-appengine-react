import React from 'react';
import ReactDOM from 'react-dom';
import injectTapEventPlugin from 'react-tap-event-plugin';
import css from '../assets/stylesheets/app.scss'
import App from './App'

injectTapEventPlugin();

ReactDOM.render(<App />, document.getElementById('app'));
