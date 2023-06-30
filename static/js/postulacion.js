$(document).ready(function() {
   $('.item-oferta').on('click', function() {
      $('.item-oferta').removeClass('oferta-active');
      $(this).addClass('oferta-active');
      
      const idOferta = $(this).data('idoferta');
      $.ajax({
         url: '/controller/selecciona_oferta',
         type: 'GET',
         data: {idOferta},
         success: (response) => {
            const lista_candidatos = response.data
            // console.log(response.data);
            $('#lista-candidatos').empty();
            lista_candidatos.forEach(candidato => {
               // console.log(typeof candidato['fecha'])
               var fecha = new Date(candidato['fecha']);

               var fechaFormateada = (fecha.getDate() + 1) + "/" + (fecha.getMonth() + 1) + "/" + fecha.getFullYear();

               // console.log(new Date())

               let li = $('<li></li>').text(`${candidato['nombre']}, ${fechaFormateada}, ${candidato['estado']}`);
               li.addClass('item-candidato');
               $('#lista-candidatos').append(li)
            });
         }
      })
      // console.log(idOferta);
   })
})