(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
  await sleep(500)
  const app = document.getElementById('app')
  return {
    appChildren: app ? app.children.length : -1,
    bodyText: document.body.innerText.slice(0, 200),
    h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : null,
    sections: document.querySelectorAll('section, .case__section').length,
  }
})()
