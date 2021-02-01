import React from 'react';

class SelectJob extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            datos: [],
        }
    }

    render(){
        return(
            <div>
                <select name = {this.props.nombre} className="custom-select mr-sm-2" id="inlineFormCustomSelect">
                    <option>Elegir sabor a producir...</option>
                    {this.props.datos.map(dato => (<option name={this.props.nombre} key = {dato.id} id={dato.id} value= {dato.id}>{dato.nombre}</option>))}
                </select>

            </div>
            
        )
    }
}

export default SelectJob;