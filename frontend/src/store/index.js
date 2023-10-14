import { createStore} from "vuex";
import router from '../router'

export default createStore({
    state: {
        server: 'http://localhost:8000/',
        isAuthenticated: null
    },

    getters: {
        headers () {
            return {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            }
        },
    },

    actions: {
        login ({commit, state}, response) {
            localStorage.setItem('token', response.data.access)
            localStorage.setItem('token_refresh', response.data.refresh)
            state.isAuthenticated = true
            router.push('/')
        }
    },

    mutations: {
        authenticate (state) {
            state.isAuthenticated = true
        },

        logout (state) {
            localStorage.removeItem('token')
            localStorage.removeItem('token_refresh')
            router.push('/')
            state.isAuthenticated = false
        }
    }
})