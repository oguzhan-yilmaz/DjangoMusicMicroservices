<template>
  <div>
    <div v-for="song in user.user_songs" :key="song.id">
      {{ song.song_title }}
      <li v-for="partition in song.song_partitions" :key="partition.id">
        <ul>
          <SongPartitionComponent :song_partition=partition />
        </ul>
      </li>
      <v-divider/>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from "vuex";
import SongPartitionComponent  from "./SongPartitionComponent.vue";
export default {
  components: {
    SongPartitionComponent
  },
  methods: {
    ...mapMutations(["incrementCount", "decrementCount", "setUser"]),
    ...mapActions(["getUserFromAPI"])
  },
  computed: {
    ...mapGetters(["count", "user", "user_songs"])
  },
  created() {
    this.getUserFromAPI();
  }
};
</script>

<style>
</style>