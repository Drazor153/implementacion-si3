$(document).ready(() => {

   // $('input#rut').on('input', function () {
   //    console.log(this.value);
   // })

   $("#submit-rut").click(() => {
      const rut = $("input#rut").val();
      if (rut.length === 0) {
         alert("Ingrese un rut");
         return;
      }
      $.ajax({
         url: "/controller/ingresar-rut",
         type: "GET",
         data: { rut },
         success: (response) => {
            if (Object.keys(response).length === 0) {
               $("div.postu-detalles").text(
                  "No se ha encontrado la postulación asociada al rut"
               );
               return;
            }
            const estudios_req =JSON.parse(response.estudios_req);
            const exp_req = JSON.parse(response.exp_req)

            const datosOferta = `Propuesta: ${response.nombre}<br/>
            Estudios Requeridos: ${estudios_req.area}, nivel: ${estudios_req.nivel}<br/>
            Experiencia requerida: ${exp_req.años} <br/>
            Cargo a postular: ${response.cargo} <br/>
            Sueldo: ${response.sueldo} <br/>
            Horas laborales: ${response.horaslab}`;

            $("div.postu-detalles").html(datosOferta);
            $("input#idPostulacion").val(response.id_postulacion);
         },
      });
   });

   $("#aceptar-postu").click(() => {
      const id_postulacion = $("input#idPostulacion").val();
      $.ajax({
         url: "/controller/selecciona-opcion",
         type: "POST",
         data: { id_postulacion, estado: "Validada" },
         success: (response) => {
            console.log(response);
            console.log("YEY :D");
         },
      });
   });

   $("#rechazar-postu").click(() => {
      const id_postulacion = $("input#idPostulacion").val();
      $.ajax({
         url: "controller/selecciona-opcion",
         type: "POST",
         data: { id_postulacion, estado: "No validada" },
         success: (response) => {
            console.log(response);
            console.log("F");
         },
      });
   });
});
