var scanner = new Instascan.Scanner({
  video: $('#qr-preview video')[0],
  mirror: false,
  backgroundScan: false,
  scanPeriod: 5
})

scanner.addListener('active', () => {
  $('#qr-preview').removeClass('inactive')
})

scanner.addListener('inactive', () => {
  $('#qr-preview').addClass('inactive')
})

scanner.addListener('scan', content => {
  scanner.stop()
  $(event_attendance_upi_id).val(content)
  $('#attendance-form').submit()
})

$('#scan').click(() => {
  Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
      scanner.start(cameras[0]).catch(e => {
        console.error(e)
      })
    } else {
      console.error('No cameras found.')
    }
  }).catch(e => {
    console.error(e)
  })
})
