import { createApp } from 'vue'
import CasePage from './CasePage.vue'
import magnetic from './directives/magnetic'
import './styles/tokens.css'
import './styles/base.css'
import './styles/sections.css'
import './styles/story.css'
import './styles/case.css'
import './styles/cursor.css'
import './styles/theme.css'

const slug = document.documentElement.dataset.case || ''
createApp(CasePage, { slug }).directive('magnetic', magnetic).mount('#app')
