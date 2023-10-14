<script>
import {defineComponent} from "vue";
import {mapActions, mapGetters, mapState} from "vuex";
export default defineComponent({
  data() {
    return {
      username: '',
      password: ''
    }
  },

  computed: {
    ...mapState(['server']),
    ...mapGetters(['headers'])
  },

  methods: {
    ...mapActions(['login']),

    loginRequest() {
      this.axios.post(`${this.server}api/token/`,
          {
            username: this.username,
            password: this.password,
          },
          this.headers)
          .then((response) => {
            this.login(response)
          })
          .catch((error) => {
            console.log(error)
          })
    }
  }
})
</script>

<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="loginRequest">
      <div>
        <label for="username">Username</label>
        <input v-model="username" type='text' id="username" />
      </div>
      <div>
        <label for="password">Password</label>
        <input v-model="password" type="text" id="password" />
      </div>
      <button type="submit">Login</button>
      <router-link to="/registration">Registration</router-link>
    </form>
  </div>
</template>

<style scoped>
</style>