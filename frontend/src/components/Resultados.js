import React, { Component } from 'react';
import {useLocation} from 'react-router-dom';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class Resultados extends React.Component{

    usarQuery() {
        return new URLSearchParams(useLocation().search);
    }

    enviarRequest(sabores){
        const json = JSON.stringify(sabores);
        const res = axios.post('http://localhost:8000/calculos/', json, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    }

    hacerRequest(){
        let x;
        axios
        .post("http://localhost:8000/calculos/")
        .then(res => {x = res.data})
        .catch(err => {x = err});
        console.log("x es " +x);
        return x;
    }

    render(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let sabores = {};
        let materias = {}
        console.log(parametros);
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
        
        console.log(sabores);
        console.log(materias);
        const res = this.hacerRequest(sabores);
        console.log(res);
        return(
            <div>
                <h1>Se muestran los resultados para la url</h1>
                <p>{res}</p>
            </div>
        )
    }
}

export default Resultados;