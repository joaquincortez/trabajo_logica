import React, { Component } from 'react';
import {useLocation} from 'react-router-dom';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class Resultados extends React.Component{

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

    enviarRequest(sabores){
        const json = JSON.stringify(sabores);
        const res = axios.post('http://localhost:8000/calculos/', json, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    }

    hacerRequest = (info) => {
        axios
        .post("http://localhost:8000/calculos/", info)
        .then(res => {
            console.log(res);
            this.setState({ datos: res.data })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let sabores = {};
        let materias = {}
        parametros[0][0] = "sabor1"; //porque devuelve como primero toda la url
        console.log("parametros son", parametros);
        let i =0;
        for(i; i<parametros.length-1; i+=2){
            console.log("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0)
            if("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0){
                console.log('entro');
                sabores[parametros[i][1]] = parametros[i+1][1];
                console.log(parametros[i][1] + " " + parametros[i+1][1])
            }
            else
                break;
        }

        for(i; i<parametros.length -1; i+=2){
            console.log('aca');
            materias[parametros[i][1]] = parametros[i+1][1];
        }
        
        console.log("sabores son", sabores);
        console.log("materias son",materias);
        const res = this.hacerRequest(sabores);
        console.log(res);
        this.hacerRequest(sabores)
    }

    render(){  
        return(
            <div>
                {console.log("Renderizando...")}
                <h1>Se muestran los resultados para la url</h1>
                <p> datos son {this.state.datos}</p>
            </div>
        )
    }
}

export default Resultados;