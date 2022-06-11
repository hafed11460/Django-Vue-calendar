<template>
    <div>
         <div class="border m-2">
            <div class="d-flex flex-column" >
                <div class="d-flex flex-row">
                    <div class="col-employee border-bottom border">
                        Add
                    </div>
                    <!-- <div class="hour-cell border-end border-bottom p-2 flex-grow-1" v-for="(hour,index) in gettersGetHourShiftChoices" :key="index">
                        {{hour[1]}}
                    </div> -->
                    <!-- <div class="hour-cell border-end border-bottom py-2 px-1  flex-grow-1"
                     v-for="(hour,index) in gettersGetHourHeader" :key="index">
                        {{ hour }}
                    </div> -->
                </div>
            </div>
            <div class="d-flex flex-column" v-for="(day,index) in 5 " :key="index">
                <div class="d-flex flex-row">
                    <div class="col-employee px-2 border-bottom border-end">
                        <div class="d-flex flex-row ps-1">
                            <p class="ms-2 mt-2"> Source {{ day }} </p>
                        </div>
                    </div>
                    <div class="d-flex flex-row bd-highlight border-bottom">
                        <Cell v-for="(day,index) in 30 " :key="index" :day="day"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Cell from './Cell.vue';

    export default{
    name: "YearView",
    components: { Cell }
}
</script>
<style scoped>
.day-cell:hover{
     background-color: rgb(13, 141, 41);
}
.row-hour-cell{
    position: relative;
    box-sizing: content-box;
    /* height: 100px; */
}
.row-hour-cell:hover{
    background-color: lemonchiffon;
}

.hour-range:hover{
    left:5.55%;
}
.col-employee{
    /* padding: 20px 0px; */
    max-width: 200px;
    min-width: 200px;
    min-height: 50px;
}

.hour-cell{
    width:5.55%;
}

</style>