var TILE_SIZE = 256
var map

function lat_to_px(lat, scale) {
  var siny = Math.sin(lat * Math.PI / 180)
  var x = TILE_SIZE * (0.5 - Math.log((1 + siny) / (1 - siny)) / (4 * Math.PI))
  return Math.floor(x * scale)
}

function px_to_lat(px, scale) {
  var x = Math.exp((TILE_SIZE * 0.5 - px / scale) * 4 * Math.PI / TILE_SIZE)
  return Math.asin((x - 1) / (x + 1)) * 180 / Math.PI
}

function resize_map () {
  var header_height = $('#ixnNav').outerHeight(true) + $('#ssigNav').outerHeight(true) + 100
  var offset = $(window).height() / 2 - header_height
  var scale = 1 << map.getZoom()

  map.setCenter({
    lat: px_to_lat(lat_to_px(event_latitude, scale) + offset, scale),
    lng: event_longitude
  })
}

$(window).resize(resize_map)

function init_map () {
  map = new google.maps.Map($('.event-map')[0], {
    center: { lat: event_latitude, lng: event_longitude },
    zoom: 15,
    disableDefaultUI: true,
    gestureHandling: 'none',
    draggableCursor: 'default;',
    zoomControl: false,
    clickableIcons: false,
    backgroundColor: '#0b4f6c',
    styles: [
        { elementType: 'labels', stylers: [{ visibility: 'off' }] },
        { featureType: 'poi', stylers: [{ visibility: 'off' }] },
        { featureType: 'transit', stylers: [{ visibility: 'off' }] },
        { elementType: 'geometry', stylers: [{ color: '#0b4f6c' }] },
        {
          featureType: 'road',
          elementType: 'geometry',
          stylers: [{ color: '#09445e' }]
        },
        {
          featureType: 'road',
          elementType: 'geometry.stroke',
          stylers: [{ color: '#0b4f6c' }]
        },
        {
          featureType: 'water',
          elementType: 'geometry',
          stylers: [{ color: '#083b51' }]
        }
      ]
  })

  var marker = new google.maps.Marker({
    position: { lat: event_latitude, lng: event_longitude },
    map: map
  })

  resize_map()
}
