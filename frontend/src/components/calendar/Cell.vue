<template>
    <div @click="showMenu()" class=" border-left cell flex-fill "
        :class="event != null ? 'active':''" role="button">
        <div class="btn-grou ">
            <span
                class="btn btn-default w-100  rounded-0 p-1 "
                :class="event != null? 'btn-'+ getColors[event.color].color:''"
                data-toggle="dropdown" aria-expanded="false">
                {{day}}
            </span>
            <ul class="dropdown-menu p-0 bg-light">
                <li  v-for="(color,index) in getColors " :key="index"
                    @click="checkedDay(index)" class=" d-flex flex-row  border-bottom" >
                    <div class="p-1 text-left flex-grow-1">{{color.name}}</div>
                    <div :class="['btn-'+color.color, 'text-'+color.color , 'index-'+index ]" class="p-1">Color</div>
                </li>
                <li  @click="remove()" class=" d-flex flex-row border-bottom" >
                    <div class="p-1 text-left flex-grow-1">Remove</div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import jwtInterceptor from '../../shared/jwtInterceptor'

export default {
    name:'Cell',
    props:{
        event:Object,
        day:Number,
        source_id:Number,
        fullDate:String,
    },
    data(){
        return{
            showmenu:false,
        }
    },
    computed:{
        ...mapGetters({
            getColors:'getColors',
            getSourceById:'getSourceById',
        })
    },
    methods:{
        ...mapActions({
            loadSourceForMonth:'loadSourceForMonth',
        }),
        showMenu(){
            this.showmenu = ! this.showmenu
        },
        async checkedDay(color){
            const data = {
                    date:this.fullDate,
                    color:color,
                    source:this.source_id
                }

            if(this.event !=null){
                try{
                    await jwtInterceptor.put('/sources/event/'+this.event.id+'/update/',data)
                    this.event.color = color
                }catch(err){
                    this.err = err.response.data
                }
            }else{
                try{
                    await jwtInterceptor.post('/sources/event/create/',data)
                }catch(err){
                    console.log(err)
                }
            }
            this.showmenu = ! this.showmenu
            this.loadSourceForMonth({
                source_id:this.source_id,
                date:this.fullDate
            })
        },
        async remove(){
            try{
                 await jwtInterceptor.delete(`/sources/event/${this.event.id}/delete/`)
                 this.loadSourceForMonth({
                    source_id:this.source_id,
                    date:this.fullDate
                })
                this.showmenu = ! this.showmenu
            }catch(err){
                console.log(err)
            }
        }
    }
}
</script>

<style scoped>
.cell{
    /* max-width: 35px; */
    min-width: 35px;
}
.menu{
    width: 150px;
    min-width: 150px;
    max-width: 250px;
}
.active{
    background-color: rgba(66, 85, 194, 0.801);
}
.hour-cell{
    width:5%;
}

.hour-cell:hover{
    background-color: cornflowerblue;
    cursor: pointer;
}
</style>