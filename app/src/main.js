import { createApp } from 'vue'
import App from './App.vue'
import magnetic from './directives/magnetic'
import './styles/tokens.css'
import './styles/base.css'
import './styles/sections.css'
import './styles/hero-arc.css'
import './styles/cursor.css'
import './styles/theme.css'
import './styles/enter.css'

createApp(App).directive('magnetic', magnetic).mount('#app')
