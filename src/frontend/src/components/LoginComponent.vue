<template >
   <div>
   <form class="login" @submit.prevent="login">
     <h1>Sign in</h1>
     <p>Demoya giriş yapmak için: username: oguzhan, password: elijah60</p>

     <label>Username</label>
     <input required v-model="form.username" type="username" placeholder="Username"/>
     <label>Password</label>
     <input required v-model="form.password" type="password" placeholder="Password"/>
     <hr/>
     <button type="submit">Login</button>
   </form>
 </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex';
export default {
    name:'signin',
    data(){
      return {
        form: {
          username : "",
          password : ""
        }
      }
    },
    methods: {
      ...mapActions(['signIn']),
      login: async function () {
       await this.signIn(this.form)
       console.log("this.token !== null", this.token !== null, this.token)
        if(this.token !== null){
          this.$router.replace({
            name:'home'
          }) 
        }
      }
    },
    computed: {
      ...mapGetters(['token']),

    }
}
</script>

<style>

</style>