import Vue from "vue";
import Vuex from "vuex";
import jwtInterceptor from './shared/jwtInterceptor'

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    date:{
      date:null,
      day:'01',
      month:null,
      year:null,
      getDate:function(){
        return `${this.year}-${this.month}-${this.day}`
      }
    },
    colors:[
      {color:'primary',name:'event'},
      {color:'success',name:'event'},
      {color:'danger',name:'event'},
      {color:'warning',name:'event'},
      {color:'dark',name:'event'},
    ],
    monthNames :["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"],
    sources:[],
    currentDate:''
  },
  getters:{
    getDate(state){
      return state.date
    },
    getColors(state){
        return state.colors
    },
    getMonthNames(state){
        return state.monthNames
    },
    getSourcesList(state){
        return state.sources
    },
    getSourceById: (state) => (id) => {
      return state.sources.find(source => source.id === id)
  },
  },
  actions:{
    setDate({commit},date){
      commit('SET_DATE',date)
    },

    async loadSourceForMonth({commit},data){
      await jwtInterceptor.get('/sources/'+data.source_id+'/?date='+ data.date)
      .then((res)=>{
          commit('UPDATE_SOURCE',res.data)
      })
      .catch((err)=>{
          console.log('employees', err)
      })
    },

    async getUserSources({commit,state}){
      await jwtInterceptor.get(`/sources/?date=${state.currentDate}`)
      .then((res)=>{
          commit('SET_SOURCES',res.data)
      })
      .catch((err)=>{
          console.log('Sources', err)
      })
    },

    async checkedDay({commit}, day){
      commit('SET_CHECKED_DAY',day)
    },


    async createSource({commit}, source){
      try{
        const res = await jwtInterceptor.post('/sources/create/',source)
        commit('SET_NEW_SOURCE',res.data)
        return true;
      }catch(err){
        console.log('createEmployee error', err.response.data)
      }
    },

      ////////////// Events ///////////

      setCurrentDate({commit},newDate){
        commit('SET_CURRENT_DATE',newDate)
      },

  },
  mutations:{
    SET_DATE(state,date){
      state.date.month = date.month
      state.date.year = date.year
      state.date.date = date.date
    },
    SET_CURRENT_DATE(state,newDate){
      state.currentDate = newDate
    },
    SET_SOURCES(state,payload){
      state.sources = payload
    },

    SET_NEW_SOURCE(state, newSource){
      state.sources.push(newSource)
    },
    SET_CHECKED_DAY(state, newSource){
      state.sources.push(newSource)
    },
    UPDATE_SOURCE(state,source){
      for (let index = 0; index < state.sources.length; index++) {
        const element = state.sources[index];
        if(element.id === source.id){
            state.sources.splice(index, 1,source)
          }
      }
  },
  }
});