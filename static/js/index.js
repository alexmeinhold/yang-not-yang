const uploadButton = document.querySelector('#upload-button')
const realInput = document.querySelector('#file-upload')
const fileInfo = document.querySelector('#file-info')

uploadButton.addEventListener('click', () => {
  realInput.click()
})

realInput.addEventListener('change', () => {
  if (realInput.value) {
    fileInfo.innerHTML = realInput.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1]
  } else {
    fileInfo.innerHTML = 'No file chosen'
  }
})
