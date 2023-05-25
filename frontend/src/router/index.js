import Vue from 'vue'
import Router from 'vue-router'
import Payment from '../view/Payment.vue'
import CheckPay from '../view/CheckPay.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',

  routes: [
    {
      path: '/',
      redirect: '/home'
    },

    {
      path: '/payment',
      component: Payment,
      props: (route) => ({ name: route.query.name })
    },

    {
      path: '/check-pay',
      component: CheckPay,
      props: (route) => ({ name: route.query.name })
    }
  ]
})
