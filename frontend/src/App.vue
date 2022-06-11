<template>
  <div id="app">
    <div class="p-2">
        <ul class="nav justify-content-end">
            <li class="nav-item">
                <a  @click="currentTab='YearView'" class="nav-link btn btn-primary rounded-0" >Year View</a>
            </li>
            <li class="nav-item">
                <a @click="currentTab='HorizontView'" class="nav-link btn btn-success rounded-0" href="#">Horizonta view </a>
            </li>
        </ul>
    </div>
    <component v-bind:is="currentTabComponent" ></component>
  </div>
</template>

<script>
import YearView from './components/YearView.vue'
import HorizontView from './components/HorizontView.vue'
// import Nav from './components/Nav.vue'

export default {
  name: 'App',
  components: {
    YearView,
    HorizontView
},
  data(){
        return{
            currentTab:'YearView'
        }
    },
  computed:{
    currentTabComponent() {
      return  this.currentTab
    }
  }

}
</script>

<!-- <style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->
