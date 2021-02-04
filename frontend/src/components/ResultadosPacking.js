import React from 'react';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class ResultadosPacking extends React.Component{

    constructor(props){
        super(props)
        this.state = {
            datos: [],
        }
    }

    usarQuery() {
        const search = window.location.href; 
        let params =  new URLSearchParams(search)
        return params;
    }

    requestResults = (data) => {
        axios
        .post("http://localhost:8000/packing/", data)
        .then(res => {
            console.log(res);
            this.setState({ datos: res.data })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        
        let capacidadCamiones = []
        let helados = [];
        let tamanos = [];
        let cantCajas = []
        console.log(" parametros es ",parametros)
        parametros[0][0] = "camion1"; //porque devuelve como primero toda la url
        let i=0;
        while(i< parametros.length && "camion".localeCompare(parametros[i][0].substring(0,6)) === 0){
            capacidadCamiones.push(parametros[i][1]);
            i++;
        }
        for(i; i<parametros.length; i+=3){
            helados.push(parametros[i][1]);
            tamanos.push(parametros[i+1][1]);
            cantCajas.push(parametros[i+2][1]);
        }

        let data = { capacidades: capacidadCamiones, helados:helados, tamanos: tamanos, cantidades: cantCajas}
        console.log("data es: ",data);
        this.requestResults(data)

    }

    render(){
        return(
            <div>
                <h1>Resultados packing</h1>
                <p>{this.state.datos}</p>
            </div>
        )
    }
}

export default ResultadosPacking;