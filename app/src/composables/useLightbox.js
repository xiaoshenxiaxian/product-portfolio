import { ref } from 'vue'

const project = ref(null)
let returnFocus = null

export function useLightbox() {
  function open(next) {
    returnFocus = document.activeElement
    project.value = next
  }

  function close() {
    project.value = null
    if (returnFocus && typeof returnFocus.focus === 'function') {
      returnFocus.focus()
    }
    returnFocus = null
  }

  return { project, open, close }
}
