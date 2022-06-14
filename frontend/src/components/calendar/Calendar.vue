<template>
  <div>
    <div class="p-2">
        <ul class="nav justify-content-end">
            <li class="nav-item">
                <a  @click="currentTab='YearView'" class="nav-link btn btn-primary rounded-0" >Year View</a>
            </li>
            <li class="nav-item">
                <a @click="currentTab='HorizontView'" class="nav-link btn btn-success rounded-0">Horizonta view </a>
            </li>
        </ul>
    </div>
    <component v-bind:is="currentTabComponent" ></component>
  </div>
</template>

<script>
import YearView from './YearView.vue'
import HorizontView from './HorizontView.vue'

export default {
  name: 'Calendar',
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
