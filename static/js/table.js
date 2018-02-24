var $items = $('#datas');

$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/planets/?page=1',
    success: function(datas) {
        $.each(datas.results, function(i, data){
         $items.append('<tr><td>' + data.name + '</td>' +
                          '<td>' + data.diameter + ' km' + '</td>' +
                          '<td>' + data.climate + '</td>' +
                          '<td>' + data.terrain + '</td>' +
                          '<td>' + data.surface_water + ' %'+ '</td>' +
                          '<td>' + data.population + '</td></tr>'
            );
        })
    }
});