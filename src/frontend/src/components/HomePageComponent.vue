<template>

  <div>
      <h1>Here are your songs:</h1>
      <br/>
          <div class="song_list" v-for="s in user_songs" :key="s.id">
              <SongComponent :song="s"></SongComponent>
          </div>
  </div>
</template>


<script>
import SongComponent from "./SongComponent";
import { mapGetters} from 'vuex';
export default {

    name: 'homepage',
    components: {
        SongComponent,
    },
    methods:{
        
    },
    data(){
        return {}
    },
    computed:{
        ...mapGetters(['user_songs', 'current_song'])
    }


}
</script>

<style scoped>

</style>