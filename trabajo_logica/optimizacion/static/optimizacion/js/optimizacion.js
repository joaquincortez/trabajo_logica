$("#agregarSabor").on("click", () =>{
    $("#seccionSabores").append("<div id = \"otroSabor\" class=\"form-group row\"> " + $("#otroSabor").html() + "</div>");
})

$("#agregarMateriaPrima").on("click", () =>{
    $("#seccionMaterias").append("<div id = \"otraMateriaPrima\" class=\"form-group row\"> " + $("#otraMateriaPrima").html() + "</div>");
})