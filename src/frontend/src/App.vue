<template lang='html'>
  <div id="app">
    <h1>MICROSERVICES APPLICATION: MUSIC SERVING</h1>
    <hr/>
    <NavigationComponent></NavigationComponent>
    <router-view/>
    
  </div>
</template>

<script>

import NavigationComponent from '@/components/NavigationComponent'

export default {
  name: 'App',
  components: {
    NavigationComponent
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.song_list {
  width:100%

}

.song {
  width: 50%;
  margin: 0 auto;
  border: 1px solid gray;

}

.audio {
    width:100%;
    margin: 0 auto;
}
</style>
