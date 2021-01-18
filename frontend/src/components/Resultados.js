import React, { Component } from 'react';
import {useLocation} from 'react-router-dom';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class Resultados extends React.Component{

    constructor(props){
        super(props)
        this.state = {
          datosHelado: [],
          datosMateria: [],
        }
    }

    usarQuery() {
        const search = window.location.href; // could be '?foo=bar'
        let params =  new URLSearchParams(search)
        return params;
    }

    enviarRequest(sabores){
        const json = JSON.stringify(sabores);
        const res = axios.post('http://localhost:8000/calculos/', json, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    }

    requestHelado = (info) => {
        axios
        .post("http://localhost:8000/calculoshelado/", info)
        .then(res => {
            console.log(res);
            this.setState({ datosHelado: Object.keys(res.data).map((key) => [key, res.data[key]]) })})
        .catch(err => {console.log(err)});
    }

    requestMateria = (info) => {
        axios
        .post("http://localhost:8000/calculosmateria/", info)
        .then(res => {
            console.log(res);
            this.setState({ datosMateria: Object.keys(res.data).map((key) => [key, res.data[key]]) })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let helados = {};
        let materias = {}
        parametros[0][0] = "sabor1"; //porque devuelve como primero toda la url
        console.log("parametros son", parametros);
        let i =0;
        for(i; i<parametros.length-1; i+=2){
            console.log("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0)
            if("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0){
                console.log('entro');
                helados[parametros[i][1]] = parametros[i+1][1];
                console.log(parametros[i][1] + " " + parametros[i+1][1])
            }
            else
                break;
        }

        for(i; i<parametros.length -1; i+=2){
            console.log('aca');
            materias[parametros[i][1]] = parametros[i+1][1];
        }
        
        console.log("sabores son", helados);
        console.log("materias son",materias);
        const resHelado = this.requestHelado(helados);
        console.log(resHelado);
        const resMateria = this.requestMateria(materias);
        console.log(resMateria);
    }

    render(){  
        console.log(this.state.datosMateria);
        return(
            <div>
                {console.log("Renderizando...")}
                <h2>Presupuesto en helados</h2>
                {this.state.datosHelado.map(elem => 
                    <li>Total en {elem[0]} es ${elem[1]}</li>
                    )}
                <h2>Presupuesto en materias primas</h2>
                {this.state.datosMateria.map(elem => 
                    <li>Total en {elem[0]} es ${elem[1]}</li>
                    )}
            </div>
        )
    }
}

export default Resultados;