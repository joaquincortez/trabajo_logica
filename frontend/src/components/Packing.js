import React from 'react';
import Encabezado from './Encabezado';
import {faBoxes} from '@fortawesome/free-solid-svg-icons';

class Packing extends React.Component{
    render(){
        return(
            <Encabezado titulo = "Packing" descripcion = "Optimizar el espacio." icono = {faBoxes} />
        )
    }
}

export default Packing;