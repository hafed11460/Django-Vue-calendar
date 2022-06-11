<template>
    <div>
         <div class="border m-2">
            <div class="d-flex flex-column" >
                <div class="d-flex flex-row ">
                    <div class="col-employee   border-bottom">
                        <span class="btn btn-success rounded-0 d-block">Add</span>
                    </div>
                    <div class="d-flex flex-row w-100 justify-content-around align-items-start border-bottom" >
                        <span @click="prevMonth()" class="btn btn-info rounded-0">Prev</span>
                        <div class=" border-end   flex-grow-1 text-center" >
                                {{getCurrentMonth}} {{ currentYear}}
                        </div>
                        <span @click="nextMonth()" class="btn btn-info rounded-0">Next</span>
                    </div>
                </div>
            </div>
            <div class="d-flex flex-column" v-for="(day,index) in 5 " :key="index">
                <div class="d-flex flex-row">
                    <div class="col-employee px-2 border-bottom border-end">
                        <div class="d-flex flex-row ps-1">
                            <p class="ms-2 mt-2"> Source {{ day }} </p>
                        </div>
                    </div>
                    <div class="d-flex flex-row bd-highlight border-bottom border-right flex-grow-1">
                        <Cell v-for="(day,index) in daysCount " :key="index" :day="day"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Cell from './Cell.vue';
import {mapGetters} from 'vuex'

    export default{
    name: "YearView",
    components: { Cell },
    data(){
        return{
            currentMonth:null,
            currentYear:null,
            currentDate:null,
        }
    },
    computed:{
        ...mapGetters({
          getMonthNames:"getMonthNames",
        }),
        getCurrentMonth(){
            if (this.currentMonth >-1 || this.currentMonth < 12){
                return this.getMonthNames[this.currentMonth]
            }
                return this.getMonthNames[0]
        },
        daysCount(){
             return new Date(this.currentYear, this.currentMonth+1, 0).getDate();
        }
    },
    methods:{
        defaultMonth(){
            const date = new Date()
            this.currentMonth = date.getMonth()
            this.currentYear = date.getFullYear()
            this.currentDate = date
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
                console.log(this.currentMonth)
            }
        },
        prevMonth(){
            if (this.currentMonth == 0) {
                this.currentMonth = 11
                this.currentDate.setFullYear(this.currentDate.getFullYear() - 1);
                // current year is a string like 2022
                this.currentYear = this.currentDate.getFullYear();
            } else {
                this.currentMonth -=1
            }
        },
    },
    created(){
        this.defaultMonth()
    }
}
</script>
<style scoped>
.day-cell:hover{
     background-color: rgb(13, 141, 41);
}

.col-employee{
    /* padding: 20px 0px; */
    max-width: 200px;
    min-width: 200px;
    min-height: 35px;
}

</style>