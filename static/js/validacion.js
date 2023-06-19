$(document).ready(() => {
   $("#submit-rut").click(() => {
      const rut = $("input#rut").val();
      if (rut.length === 0) {
         alert("Ingrese un rut");
         return;
      }
      $.ajax({
         url: "/buscar-postulacion",
         type: "GET",
         data: { rut },
         success: (response) => {
            const lista = response.data[0];
            if (lista === undefined) {
               $("div.postu-detalles").text(
                  "No se ha encontrado la postulación asociada al rut"
               );
               return;
            }
            $("div.postu-detalles").text(lista.join());
            $("input#idPostulacion").val(lista[0]);
         },
      });
   });

   $("#aceptar-postu").click(() => {
      const id_postulacion = $("input#idPostulacion").val();
      $.ajax({
         url: "selecciona-opcion",
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
         url: "selecciona-opcion",
         type: "POST",
         data: { id_postulacion, estado: "No validada" },
         success: (response) => {
            console.log(response);
            console.log("F");
         },
      });
   });
});
