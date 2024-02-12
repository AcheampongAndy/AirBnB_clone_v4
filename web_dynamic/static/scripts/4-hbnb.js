$(document).ready(function () {
  let aList = [];
  let amenities = {};
  $('.amenities-list').change(function (event) {
    let amenityId = $(this).attr('data-id');
    let amenityName = $(this).attr('data-name');

    if (event['target']['checked']) {
      amenities[amenityId] = amenityName;
	  aList.push(amenityName);
    } else {
      delete amenities[amenityId];
	  aList.splice(aList.indexOf(amenityName), 1);
    }
    $('.amenities h4').text(aList);
  });

  let aData = {'amenities': []};

  $('.popover li input[type=checkbox]').on('change', function (event) {
    let amenityId = event.target.dataset.id;
    let ischecked = $(this).is(':checked');
    if (ischecked) aData['amenities'].push(amenityId);
    else aData['amenities'].splice(aData['amenities'].indexOf(amenityId), 1);

	$('.places').empty();
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/places_search/',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify(aData),
      success: function (data) {
        for (let i = 0; i < data.length; ++i) {
          let html = '<article><div class="title"><h2>' + data[i].name + '</h2><div class="price_by_night">' + data[i].price_by_night + '</div></div><div class="information"><div class="max_guest"><i class="fa fa-users fa-3x" aria-hidden="true"></i><br />' + data[i].max_guest + ' Guests</div><div class="number_rooms"><i class="fa fa-bed fa-3x" aria-hidden="true"></i><br />' + data[i].number_rooms + ' Bedrooms</div><div class="number_bathrooms"><i class="fa fa-bath fa-3x" aria-hidden="true"></i><br />' + data[i].number_bathrooms + ' Bathroom</div></div><div class="user"></div><div class="description">' + data[i].description + '</div></article>';
          $('.places').append(html);
        }
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
      }
    });
  });

  $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5001/api/v1/status/',
    success: function (data) {
      $('#api_status').addClass('available');
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(jqXHR);
      console.log(textStatus);
      console.log(errorThrown);
    },
    dataType: 'json'
  });

  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5001/api/v1/places_search/',
    dataType: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: function (data) {
      for (let i = 0; i < data.length; ++i) {
        let html = '<article><div class="title"><h2>' + data[i].name + '</h2><div class="price_by_night">' + data[i].price_by_night + '</div></div><div class="information"><div class="max_guest"><i class="fa fa-users fa-3x" aria-hidden="true"></i><br />' + data[i].max_guest + ' Guests</div><div class="number_rooms"><i class="fa fa-bed fa-3x" aria-hidden="true"></i><br />' + data[i].number_rooms + ' Bedrooms</div><div class="number_bathrooms"><i class="fa fa-bath fa-3x" aria-hidden="true"></i><br />' + data[i].number_bathrooms + ' Bathroom</div></div><div class="user"></div><div class="description">' + data[i].description + '</div></article>';
        $('.places').append(html);
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log(jqXHR);
      console.log(textStatus);
      console.log(errorThrown);
    }
  });
});
