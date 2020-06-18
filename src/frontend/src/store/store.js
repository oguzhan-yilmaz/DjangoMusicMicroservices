import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    token: null,
    user: null,
    current_song: null,
  },
  getters: {
    token: (state) => state.token,
    user: (state) => state.user,
    user_songs: (state) => state.user.user_songs,
    current_song: (state) => state.current_song,
    headers: function (state){
      if (state.token){
        return {'Content-Type': 'application/json', 'Authorization':'Token ' + state.token}
      } 
      return {'Content-Type': 'application/json'}
    } 
  },
  mutations: {
    SET_TOKEN(state, token){
      state.token = token;
    },
    SET_USER(state, newUser) {
      state.user = newUser;
    },
    SET_CURRENT_SONG(state, cur_song){
      state.current_song = cur_song;
    }
  },
  actions: {
    async getUserInfo({commit, getters}){
      await axios.get('http://localhost:8000/api/users/',
        {
          headers: getters.headers
        }
        )
        .then((response) => {
          let user = {
            id: response.data.id,
            user_songs: response.data.user_songs,
            username: response.data.username
          }
          console.log('user data.', user.user_songs)

          commit('SET_USER', user)
          console.log("cursong:", user.user_songs[0])
          commit('SET_CURRENT_SONG', user.user_songs[0])
        }).catch((err) => {
          console.log(err)
        })

    },
    async signIn({ commit, getters, dispatch }, credentials){
      await axios.post('http://localhost:8000/api/auth/token/',
        { 
          username: credentials.username,
          password: credentials.password
        },
        getters.headers)
        .then(function(response){
          let token = response.data.token
          commit('SET_TOKEN', token)
          dispatch('getUserInfo')
          
        }).catch((err) => {
          console.log(err)
        })
    },

  },
});
