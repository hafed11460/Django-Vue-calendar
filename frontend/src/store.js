import Vue from "vue";
import Vuex from "vuex";
import jwtInterceptor from './shared/jwtInterceptor'
import excelJwtInterceptor from './shared/excelJwtInterceptor'

Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    isSave: false,
    date: {
      date: null,
      day: '01',
      month: null,
      year: null,
      getDate: function () {
        return `${this.year}-${this.month}-${this.day}`
      }
    },
    colors: [
      { color: 'primary', name: 'event' },
      { color: 'success', name: 'event' },
      { color: 'danger', name: 'event' },
      { color: 'warning', name: 'event' },
      { color: 'dark', name: 'event' },
    ],
    monthNames: ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"],
    sources: [],
    currentDate: ''
  },
  getters: {
    getCurrentDate(state){
      return state.currentDate
    },
    isSave(state) {
      return state.isSave;
    },
    getDate(state) {
      return state.date
    },
    getColors(state) {
      return state.colors
    },
    getMonthNames(state) {
      return state.monthNames
    },
    getSourcesList(state) {
      return state.sources
    },
    getSourceById: (state) => (id) => {
      return state.sources.find(source => source.id === id)
    },
  },
  actions: {
    setDate({ commit }, date) {
      commit('SET_DATE', date)
    },

    async calendarExcelDownload({state}){
      await excelJwtInterceptor.get('/sources/excel/?date='+state.currentDate)
      .then ((res) => {
          const url = window.URL.createObjectURL(new Blob([res.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'week-'+state.dateSelected+'.xlsx');
          document.body.appendChild(link);
          link.click();
      })
  },
    async saveSources({ state }) {
      try {
        console.log('sources:', state.sources)
        await jwtInterceptor.post('/sources/save/', { data: { sources: state.sources, date: state.currentDate } })

        // commit('SAVE_SOURCES',res.data)
        return true;
      } catch (err) {
        console.log('Error To create source', err.response.data)
      }
    },


    async loadSourceForMonth({ commit }, data) {
      await jwtInterceptor.get('/sources/' + data.source_id + '/?date=' + data.date)
        .then((res) => {
          commit('UPDATE_SOURCE', res.data)
        })
        .catch((err) => {
          console.log('employees', err)
        })
    },

    async getUserSources({ commit, state }) {
      await jwtInterceptor.get(`/sources/?date=${state.currentDate}`)
        .then((res) => {
          commit('SET_SOURCES', res.data)
          commit('SET_IS_SAVE', false)
        })
        .catch((err) => {
          console.log('Sources', err)
        })
    },

    async checkedDay({ commit }, day) {
      commit('SET_CHECKED_DAY', day)
    },


    async createSource({ commit }, source) {
      try {
        const res = await jwtInterceptor.post('/sources/create/', source)
        commit('SET_NEW_SOURCE', res.data)
        return true;
      } catch (err) {
        console.log('Error To create source', err.response.data)
      }
    },
    async updateSource({ commit }, source) {
      try {
        const res = await jwtInterceptor.put(`/sources/${source.id}/update/`, source)
        commit('UPDATE_SOURCE', res.data)
        return true;
      } catch (err) {
        console.log('Error update Source', err.response.data)
      }
    },

    async deleteSource({ commit }, id) {
      try {
        await jwtInterceptor.delete(`/sources/${id}/delete/`)
        commit('DELETE_SOURCE', id)
        return true;
      } catch (err) {
        console.log('Error Delete Source ', err.response.data)
      }
    },

    ////////////// Events ///////////

    setCurrentDate({ commit }, newDate) {
      commit('SET_CURRENT_DATE', newDate)
    },

  },
  mutations: {
    SET_RANGE_SELECTED(state, { events, sourcesIds }) {
      // let sources = state.sources.filter((source)=>sourcesIds.includes(source.id))
      console.log('events', events)
      for (let i = 0; i < state.sources.length; i++) {
        // console.log(sources[i])
        if (sourcesIds.includes(state.sources[i].id))
          for (let j = 0; j < events.length; j++) {
            let evt = events[j]
            // console.log(evt)
            let exist = state.sources[i].events.some(function (e) {
              return e.date === evt.date
            })

            if (!exist) {
              //
              const newEvent = {
                color: evt.color,
                date: evt.date,
                state: "create",
                visible: true,
                source: state.sources[i].id

              }
              state.sources[i].events.push(newEvent)
            }
          }
      }
      state.isSave = true
      console.log('up sources', state.sources)
    },
    SET_IS_SAVE(state, isSave) {
      state.isSave = isSave
    },
    CREATE_SOURCE_DAY(state, newEvent) {
      for (let index = 0; index < state.sources.length; index++) {
        const source = state.sources[index];
        if (source.id === newEvent.source) {
          state.sources[index].events.push(newEvent)
          state.isSave = true
          break;
        }
      }
    },

    SET_DATE(state, date) {
      state.date.month = date.month
      state.date.year = date.year
      state.date.date = date.date
    },
    SET_CURRENT_DATE(state, newDate) {
      state.currentDate = newDate
    },
    SET_SOURCES(state, payload) {
      state.sources = payload
    },
    DESTROY_SOURCES(state) {
      state.sources = []
    },

    SET_NEW_SOURCE(state, newSource) {
      state.sources.push(newSource)
    },
    SET_CHECKED_DAY(state, newSource) {
      state.sources.push(newSource)
    },
    UPDATE_SOURCE(state, source) {
      for (let index = 0; index < state.sources.length; index++) {
        const element = state.sources[index];
        if (element.id === source.id) {
          state.sources.splice(index, 1, source)
          break;
        }
      }
    },
    DELETE_SOURCE(state, id) {
      for (let index = 0; index < state.sources.length; index++) {
        const element = state.sources[index];
        if (element.id === id) {
          state.sources.splice(index, 1)
          break;
        }
      }
    },
  }
});