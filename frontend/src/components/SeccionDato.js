import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';

class SeccionDato extends React.Component{
    constructor(props){
        super(props);
        this.render = this.render.bind(this);
    }
    render(){
        return(
            <div className="form-group row">
                <div className="col-9 text-center">
                    <select name = {this.props.nombre + this.props.nro}  className="custom-select" id="inputGroupSelect01">
                        <option id="-1" value="-1" >Seleccionar opción</option>
                        {this.props.datos.map(dato => (<option id={dato.id} value= {dato.id}>{dato.nombre}</option>))}
                    </select>
                </div>
                <div className="col-3 text-center">
                    <div className="input-group">
                        <input name = {"cant" + this.props.nombre + this.props.nro} type="number" className="form-control" aria-label="Demanda en kg"></input>
                        <div className="input-group-append">
                            <span className="input-group-text">kg</span>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default SeccionDato;