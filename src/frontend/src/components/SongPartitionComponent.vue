<template>
  <div>Partiton: {{start_min}}:{{start_sec}}-{{end_min}}:{{end_sec}}</div>
</template>

<script>
export default {
  name: "SongPartitionComponent",
  props: {
      song_partition: {
          type: Object
      }
  },
  computed: {
    start_min() {
      return Math.floor(this.$props.song_partition.start_idx / 44100 / 60);
    },
    start_sec() {
      return Math.floor(this.song_partition.start_idx, 44100) % 60;
    },
    end_min() {
      return Math.floor(this.song_partition.end_idx / 44100 / 60);
    },
    end_sec() {
      return Math.floor(this.song_partition.end_idx, 44100) % 60;
    }
  }
};
</script>

<style>
</style>