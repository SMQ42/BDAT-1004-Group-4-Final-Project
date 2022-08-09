<template>
  <div id="app">
    <chartsPage msg="charts page"/>
  </div>
</template>

<script>
import chartsPage from './components/chartsPage.vue'

export default {
  name: 'App',
  components: {
    chartsPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
