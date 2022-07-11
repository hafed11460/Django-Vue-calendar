<template>
  <div>
      <div class="p-2">
      <!--       <div class="col">
        <select
          size="sm"
          boundary="viewport"
          variant="outline-dark"
          :text="selectedSources.length + ' Selected options'"
          class="m-md-2"
          style="max-width: 350px !important; font-weight: 600"
        >
          <option
            :event="'hover'"
            href="javascript:void(0)"
            v-for="source in getSourceList"
            :key="source.id"
            @click.native.capture.stop
          >
            <input
              type="checkbox"
              style="margin-right: 4px; margin-left: 20px"
              v-model="massSelect"
              @click.native.stop=""
              :value="source"
            />{{ source.name }}
          </option>
        </select>
      </div> -->
      <ul class="nav justify-content-end">
        <li
          style="
            border: 2px black solid;
            width: -webkit-fit-content;
            padding: 15px;
            margin-right: 20px;
          "
        >
          <div>
            From <input  v-model="fromDate" type="date" style="margin-right: 30px" />
            To <input  v-model="toDate" type="date"  >

            <select
             v-model="color"
              size="sm"
              boundary="viewport"
              class="m-md-2"
              style="max-width: 350px !important; font-weight: 400"
            >
              <option
                :event="'hover'"
                href="javascript:void(0)"

                v-for="(color,index) in getColorsList"
                :value="index"
                :key="index"
                :class="[
                  'btn-' + color.color,
                  'text-' + color.color,
                  'index-' + index,
                ]"
                class="p-1"
              >
                {{ color.color }}
              </option>
            </select>
            <input
            type="checkbox"
            @click="selectAllSources"
            v-model="allSelected"
            style="margin-left: 20px; margin-right: 4px"
            />

            <label>Check All </label>
            <button
              @click="addSelected()"
              class="nav-link btn btn-outline-danger btn-sm rounded-0"
              style="max-width: 100px; float: left; margin-right: 30px"
              >Add Selected</button>

          </div>
          <br />
          <div class="nav justify-content col-lg-12">

            <div
              style="margin-left: 15px"
              v-for="source in getSourceList"
              :key="source.id"
            >

              <input
                 type="checkbox"
                 v-model="sourcesIds"
                 @click="selectSource"
                 :value="source.id"
                 style="margin-right: 4px"
                 />
               <label>{{ source.name }}</label>
            </div>
          </div>
          Sources selected : {{ SelectedBoxes }}

        </li>
        <li class="nav-item">
          <a
            @click="currentTab = 'YearView'"
            class="nav-link btn btn-primary rounded-0"
            >Horizontal View</a
          >
        </li>
        <li class="nav-item">
          <a
            @click="currentTab = 'HorizontView'"
            class="nav-link btn btn-success rounded-0"
            >Year view
          </a>
        </li>
      </ul>
    </div>

    <!-- <div class="p-2">
        <ul class="nav justify-content-end">
            <li class="nav-item">
                <a  @click="currentTab='YearView'" class="nav-link btn btn-primary rounded-0" >Year View</a>
            </li>
            <li class="nav-item">
                <a @click="currentTab='HorizontView'" class="nav-link btn btn-success rounded-0">Horizonta view </a>
            </li>
        </ul>
    </div> -->
    <component v-bind:is="currentTabComponent" ></component>
    <div class="p-2">
      <ul class="nav justify-content-end">
        <li class="nav-item">
          <button @click="excelDownload()" class="nav-link btn btn-outline-success rounded-0">Export file</button>
        </li>
        <li class="nav-item">
          <button @click="save()" :class="{'nav-link btn btn-outline-danger rounded-0':true,'disabled':!getterIsSave}">Save to DB</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {  mapActions, mapGetters, mapMutations } from 'vuex';
import YearView from './YearView.vue'
// import HorizontView from './HorizontView.vue'

export default {
  name: 'Calendar',
  components: {
    YearView,
    // HorizontView
  },
  data(){
        return{
            fromDate:'',
            toDate:'2022-07-10',
            color:1,
            currentTab:'YearView',
            allSelected: true,
            sourcesIds:[ 1, 2, 6, 18, 19 ],
            sourcesSelected:[],

        }
    },

  watch:{
    getCurrentDate:{
       handler(){
        this.fromDate = this.getCurrentDate
        this.toDate = this.getCurrentDate
       },
       deep:true,
    }
  },

  computed:{
     ...mapGetters({
      getCurrentDate:'getCurrentDate',
      getterIsSave:'isSave',
      getSourceList: "getSourcesList",
      getColorsList: "getColors",
    }),
     SelectedBoxes() {
     return  this.getSourceList.filter((source)=>this.sourcesIds.includes(source.id)).map(source => source.name)
    },
    currentTabComponent() {
      return  this.currentTab
    },
  },
  methods:{
    ...mapMutations({
      SET_IS_SAVE : 'SET_IS_SAVE',
      SET_RANGE_SELECTED : 'SET_RANGE_SELECTED',
    }),
    ...mapActions({
      calendarExcelDownload:'calendarExcelDownload',
      saveSources:'saveSources',
      actionGetUserSources:'getUserSources',
    }),

    selectAllSources: function() {
            this.sourcesIds = [];

            if (!this.allSelected) {
                for (let source in this.getSourceList) {
                    this.sourcesIds.push(this.getSourceList[source].id);
                }
            }
        },
        selectSource: function() {
            this.allSelected = false;
        },
       getDates (startDate, endDate) {
          const dates = []
          let currentDate = startDate
          const addDays = function (days) {
            const date = new Date(this.valueOf())
            date.setDate(date.getDate() + days)
            return date
          }
          while (currentDate <= endDate) {
            dates.push(currentDate.toISOString().substr(0, 10))
            currentDate = addDays.call(currentDate, 1)
          }
          return dates
        },
    addSelected(){
      const dates = this.getDates(new Date(this.fromDate), new Date(this.toDate))
      let events = []
      for( let i = 0; i < dates.length ; i++){
         const evnt = {
            'color':this.color,
            'date':dates[i],
          }
          events.push(evnt)
      }

        console.log(events)
        const data = {
          events:events,
          sourcesIds:this.sourcesIds
        }
        this.SET_RANGE_SELECTED(data)

      // daylist.map((v)=>v.toISOString().slice(0,10)).join("")
    },
      async excelDownload(){
              await this.calendarExcelDownload()
      },
    async save(){

      if (await this.saveSources()){
        await this.actionGetUserSources()
      }

    }

  },created(){
       this.fromDate = this.$store.state.currentDate
        // this.toDate = this.getCurrentDate
  }
}
</script>
