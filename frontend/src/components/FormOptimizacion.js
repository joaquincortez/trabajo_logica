import React, { Component } from 'react';
import SeccionForm from './SeccionForm';
import SeccionRadio from './SeccionRadio';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faIceCream, faChartLine, faBox, faBoxes, faCalculator,  } from '@fortawesome/free-solid-svg-icons'



class FormOptimizacion extends React.Component{
    constructor(props){
        super(props);
        this.cambiarEstadoPadre = this.CambiarEstadoPadre.bind(this);

    }

    CambiarEstadoPadre = () =>{
        this.props.cambiarEstado();
    }

    render(){
        return(
            <div>
                <form action =  '/resultados' method="get"  >
                    <SeccionForm titulo = "Sabores a producir" nombreTipo= "Sabor" nombreCantidad = "Demanda" iconoTitulo =  {faIceCream} iconoCantidad = {faChartLine} nombreAPI ="helados" />
                    <SeccionForm titulo = "Materias primas disponibles" nombreTipo= "Materia Prima" nombreCantidad = "Disponibilidad" iconoTitulo =  {faBox} iconoCantidad = {faBoxes} nombreAPI="materiasprima"/>
                    <SeccionRadio nombre = 'Objetivo'/>
                    <button type="submit" class="btn btn-dark" ><FontAwesomeIcon icon = {faCalculator} /> Calcular</button>
                </form>
            </div>
        );
    }
}

export default FormOptimizacion;