const uploadButton = document.querySelector('#upload-button')
const realInput = document.querySelector('#file-upload')
const fileInfo = document.querySelector('#file-info')
const classifyButton = document.querySelector('#classify')

const MAX_LENGTH = 25

uploadButton.addEventListener('click', () => {
  realInput.click()
})

realInput.addEventListener('change', () => {
  if (realInput.value) {
    fileName = realInput.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1]

    if (fileName.length > 25) {
        fileName = fileName.slice(0, 10) + '...' + fileName.slice(-11)
    }

    fileInfo.innerHTML = fileName
    classifyButton.disabled = false
  } else {
    fileInfo.innerHTML = 'No file chosen'
  }
})
