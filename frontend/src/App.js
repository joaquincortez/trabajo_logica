import React from 'react';
import NavBar from './components/NavBar';
import FormOptimizacion from './components/FormOptimizacion';
import Resultados from './components/Resultados';
import './css/optimizacion.css';
import 'bootstrap/dist/css/bootstrap.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCode }  from '@fortawesome/free-solid-svg-icons';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
} from "react-router-dom";


function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <div className = 'container'>
          <Switch>
            <div className="jumbotron jumbotron-fluid">
              <div className="container">
              <h1 className="display-4"><FontAwesomeIcon icon={faCode} />Optimización lineal</h1>
                <p className="lead">Optimización de la producción semanal de helados.</p>
                <hr></hr>
                <Switch>
                  <Route path = '/' exact><FormOptimizacion /></Route>
                  <Route path = '/resultados' ><Resultados /></Route>
                </Switch>
              </div>
            </div>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
