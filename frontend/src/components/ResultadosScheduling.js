import React from 'react';
import axios from "axios";
import Encabezado from './Encabezado';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class ResultadosScheduling extends React.Component{

    constructor(props){
        super(props)
        this.state = {
            datos: [],
        }
    }

    usarQuery() {
        const search = window.location.href; // could be '?foo=bar'
        let params =  new URLSearchParams(search)
        return params;
    }

    requestResults = (hel) => {
        axios
        .post("http://localhost:8000/scheduling/", {helados: hel})
        .then(res => {
            console.log(res);
            this.setState({ datos: res.data })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let id_helados = [];
        console.log(" parametros es ",parametros)
        if(parametros != null){
            parametros[0][0] = "sabor1"; //porque devuelve como primero toda la url
            for (let i=0; i<parametros.length; i++){
                console.log(parametros[i])
                id_helados.push(parametros[i][1])
            }
            console.log("id helados es",id_helados);
            this.requestResults(id_helados);
        }

    }

    render(){
        return(
            <div>
                <h1>Resultados scheduling</h1>
                <p>{this.state.datos}</p>
            </div>
        )
    }
}

export default ResultadosScheduling;