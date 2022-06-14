<template>
    <div>
         <div class="border border-bottom-0 m-2">

            <div class="d-flex flex-column" >
                <div class="d-flex flex-row ">
                    <!-- Create new Source  -->
                    <div class="col-employee   border-bottom">
                        <CreateSource/>
                    </div>

                    <div class="d-flex flex-row w-100 justify-content-around align-items-start border-bottom" >
                        <span @click="prevMonth()" class="btn btn-info rounded-0 px-5">Prev</span>
                        <div class=" border-end   flex-grow-1 text-center" >
                             <h6 class=" text-center p-1  w-100">  {{getCurrentMonth}} {{ currentYear}} </h6>
                        </div>
                        <span @click="nextMonth()" class="btn btn-info rounded-0 px-5">Next</span>
                    </div>
                </div>
            </div>
            <!-- Source Row  -->
            <SourceRow v-for="(source,index) in getSourcesList "
                :key="index"
                :source="source"
                :daysCount="daysCount"
                :month="currentMonth"
                :year="currentYear"
            />
        </div>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import CreateSource from './CreateSource.vue';
import SourceRow from './SourceRow.vue';

    export default{
    name: "YearView",
    components: {  CreateSource, SourceRow },
    data(){
        return{
            currentMonth:null, // number of  current month selected like jun=1
            currentYear:null, // 2022
            currentDate:null,// Date Object
        }
    },


    computed:{
        ...mapGetters({
          getMonthNames:"getMonthNames", // get Month name
          getSourcesList:"getSourcesList",
          getterGetDate:'getDate' // get source list
        }),

        // return current  month selected
        getCurrentMonth(){
            if (this.currentMonth >-1 || this.currentMonth < 12){
                return this.getMonthNames[this.currentMonth]
            }
            return this.getMonthNames[0]
        },
        // return Number days of month like (March = 31 )
        daysCount(){
             return new Date(this.currentYear, this.currentMonth+1, 0).getDate();
        },

    },
    watch:{
        currentMonth(){
            this.changeCurrentDate()
        }
    },
    methods:{
        ...mapActions({
            actionGetUserSources:'getUserSources',
            actionsSetCurrentDate:'setCurrentDate',
            actionSetDate:'setDate',
        }),
        async changeCurrentDate(){
            let month = (this.currentMonth +1) < 10 ? '0'+(this.currentMonth+1):''+(this.currentMonth+1)
            let date =  `${this.currentYear}-${month}-01`
            console.log('currentDate', date)
            this.actionsSetCurrentDate(date)
            this.actionGetUserSources()
        },
        defaultMonth(){
            const date = new Date()
            this.currentMonth = date.getMonth()
            this.currentYear = date.getFullYear()
            this.currentDate = date
            let newDate={
                month:date.getMonth(),
                year:date.getFullYear(),
                date:date
            }
            this.actionSetDate(newDate)
            // return date.getMonth()
        },
        nextMonth(){
            if (this.currentMonth == 11) {
                this.currentMonth = 0
                this.currentDate.setFullYear(this.currentDate.getFullYear() + 1);
                // current year is a string like 2022
                this.currentYear = this.currentDate.getFullYear();
            } else {
                this.currentMonth +=1
            }
        },
        prevMonth(){
            if (this.currentMonth == 0) {
                this.currentMonth = 11
                this.currentDate.setFullYear(this.currentDate.getFullYear() - 1);
                // current year is a string like 2022
                this.currentYear = this.currentDate.getFullYear();
            } else {
                this.currentMonth -= 1
            }

        },
    },
    created(){
        this.defaultMonth()
        // this.changeCurrentDate()
    }
}
</script>
<style>
.day-cell:hover{
     background-color: rgb(13, 141, 41);
}
.source:hover{
     background-color: rgb(248, 248, 248);
}

.col-employee{
    /* padding: 20px 0px; */
    max-width: 200px;
    min-width: 200px;
    min-height: 35px;
}

</style>