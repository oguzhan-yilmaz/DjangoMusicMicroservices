<template>
<div class="song">
  <h3>TITLE: {{song.song_title.toUpperCase()}} </h3>
  <p>BPM:{{song.bpm}}</p><p> KEY: {{song.key}} {{song.key_scale}}</p>
  <audio controls>
  <source :src="song.url" type="audio/wav">
  </audio>
</div>
</template>




<script>
export default {
  name: "SongComponent",
  props: {
      song:{},
  },
  computed:{

  }
}
</script>

<style scoped>

</style>