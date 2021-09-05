const VideoCard = Vue.component('video-card', {
    template: '#video-card-template',
    delimiters: ['[[', ']]'],
    props: ['id', 'thumbnail', 'title', 'date'],
})

const Home = Vue.component('home', {
    components: {VideoCard},
    template: '#home-template',
})

const Channels = Vue.component('channels', {
    template: '#channels-template',
})

const routes = [
    { name: 'Home', component: Home, path: '/', },
    { name: 'Channels', component: Channels, path: '/channels/', },
]

const router = new VueRouter({
    mode: 'history',
    routes: routes,
})

const app = new Vue({
    router,
    vuetify: new Vuetify(),
}).$mount('#app');