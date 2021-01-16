import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';
import OpcionRadio from './OpcionRadio';

class SeccionRadio extends React.Component{
    render(){
        return(
            <div class="seccionForm">
                <fieldset class="form-group">
                    <div class="row">
                        <legend class="col-form-label col-sm-2 pt-0">{this.props.nombre}</legend>
                        <div class="col-sm-10">
                            <OpcionRadio nombre='Maximizar ganancias'/>
                            <OpcionRadio nombre='Maximizar produccion'/>
                            <OpcionRadio nombre='Minimizar costos'/>
                            <OpcionRadio nombre='Minimizar perdidas'/>
                        </div>
                    </div>
                </fieldset>
          </div>
        );
    }
}

export default SeccionRadio;
