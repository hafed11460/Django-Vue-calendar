<template>
    <div class="border">
        <div class="d-flex flex-row" v-for="(hour,index) in 24 " :key="index">
            c
        </div>
        <!-- <Cell  v-for="(hour,index) in 24 " :key="index"></Cell> -->
    </div>
</template>

<script>

// import Cell from './Cell.vue'

export default {
    name:'DayRowCell',
    components:{
        // Cell,
    },
    data(){
        return{

        }
    },
}
</script>

<style>


</style>