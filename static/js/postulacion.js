$(document).ready(function() {
   $('.item-oferta').on('click', function() {
      $('.item-oferta').removeClass('oferta-active');
      $(this).addClass('oferta-active');
      
      const idOferta = $(this).data('idoferta');
      $.ajax({
         url: '/selecciona_oferta',
         type: 'GET',
         data: {idOferta},
         success: (response) => {
            const lista_postulaciones = response.data
            // console.log(response.data);
            $('#lista-candidatos').empty();
            lista_postulaciones.forEach(candidato => {
               let li = $('<li></li>').text(candidato);
               li.addClass('item-candidato');
               $('#lista-candidatos').append(li)
            });
         }
      })
      console.log(idOferta);
   })
})