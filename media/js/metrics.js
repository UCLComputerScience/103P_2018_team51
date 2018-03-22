const DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

var default_settings = {
  interpolate: d3.curveLinear,
  full_width: true,
  height: 300,
  y_accessor: 'total',
  transition_on_update: false
}

function createGraph(name, title) {
  var settings = Object.assign({}, default_settings, {
    title: title,
    target: '#' + name,
  })

  d3.json(`data/${name}/week.json`, data => {
    data = MG.convert.date(data, 'date', DATE_FORMAT)
    settings.data = data
    MG.data_graphic(settings)
  })

  $(`#${name}-controls button`).click(function () {
    $(this).addClass('active').siblings().removeClass('active')

    var period = $(this).data('period')
    d3.json(`data/${name}/${period}.json`, data => {
      data = MG.convert.date(data, 'date', DATE_FORMAT)
      settings.data = data
      MG.data_graphic(settings)
    })
  })
}
