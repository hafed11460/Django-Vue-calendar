import Vue from "vue";

import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    monthNames :["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"],
  },
  getters:{
    getMonthNames(state){
        return state.monthNames
    },
  },
});