import React from 'react';
import Encabezado from './Encabezado';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faCalendarAlt, faPlus, faCalculator } from '@fortawesome/free-solid-svg-icons';
import SelectJob from './SelectJob'
import axios from 'axios';
import '../css/optimizacion.css';

class Scheduling extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            datos: [],
            selects: [1,2],
        }

    }

    AgregarSelect = ()=>{
        let nuevoSelect = this.state.selects.length + 1;
        this.setState( prevState => ({selects: prevState.selects.concat([nuevoSelect])}))
      }
    cargarItems(){
        axios
        .get("http://localhost:8000/api/helados/")
        .then(res => this.setState({ datos: res.data }))
        .catch(err => console.log(err));
    }

    componentDidMount(){
        this.cargarItems();
    }

    render(){
        return(
            <div>
                <Encabezado titulo = "Scheduling" descripcion = "Optimizar el orden a la hora de utilizar maquinas para realizar tareas." icono = {faCalendarAlt} />
                <form action =  '/scheduling' method="get" >
                    <h2>Elegir helados a producir en orden.</h2>
                    <div className = "scheduling">
                        {this.state.selects.map(select => <SelectJob nombre={"sabor" + select} key = {select.id} datos = {this.state.datos}/> )}
                        <button type="button" className="btn btn-secondary" id="agregarHelado" onClick = {this.AgregarSelect}><FontAwesomeIcon icon={faPlus}/> Agregar helado</button>
                    </div>
                    <button type="submit" className="btn btn-dark" ><FontAwesomeIcon icon = {faCalculator} /> Calcular</button>
                </form>
            </div>
        )
    }
}

export default Scheduling;