<template>
  <div id="app">
    <router-link class="link" :to="{ path: '/payment'}">Payment</router-link>
		<router-link class="link" :to="{ path: '/check-pay', query: { name: 'Foo' }}">Check Pay</router-link>
    <!-- <Calendar/> -->
    <router-view></router-view>
  </div>
</template>
<script>

// import Calendar from './components/calendar/Calendar.vue'
export default {
  name: 'App',
  components: {
    // Calendar,
}
}
</script>

<style scoped>
  .link{
    margin:  10px;
  }
</style>