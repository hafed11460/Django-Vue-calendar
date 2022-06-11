<template>
    <div @click="showMenu()" class=" border-right cell "
        :class="active ? 'active':''" role="button">
        <div class="btn-grou ">
            <span
                class="btn btn-default w-100  rounded-0 p-1 "
                :class="active?color:''"
                data-toggle="dropdown" aria-expanded="false">
                {{day}}
            </span>
            <ul class="dropdown-menu p-0 bg-light">
                <li @click="checked('btn-primary')" class=" d-flex flex-row  border-bottom" >
                    <div class="p-1 text-left flex-grow-1">Event</div>
                    <div class="p-1 bg-primary text-primary">Color</div>
                </li>
                <li  @click="checked('btn-success')" class=" d-flex flex-row border-bottom" >
                    <div class="p-1 text-left flex-grow-1">Event</div>
                    <div class="p-1 bg-success text-success">Color</div>
                </li>
                <li  @click="checked('btn-danger')" class=" d-flex flex-row border-bottom" >
                    <div class="p-1 text-left flex-grow-1">Event</div>
                    <div class="p-1 bg-danger text-danger">Color</div>
                </li>
                <li  @click="remove()" class=" d-flex flex-row border-bottom" >
                    <div class="p-1 text-left flex-grow-1">Remove</div>
                    <div class="p-1 bg-default text-default">Color</div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>

export default {
    name:'Cell',
    props:{
        day:Number,
    },
    data(){
        return{
            color:'',
            active:false,
            showmenu:false,
        }
    },
    methods:{
        showMenu(){
            this.showmenu = ! this.showmenu
        },
        checked(color){
            this.showmenu = ! this.showmenu
            this.active = true;
            this.color = color
        },
        remove(){
            this.showmenu = ! this.showmenu
            this.active = false;
            this.color = ''
        }
    }

}
</script>

<style scoped>
.cell{
    max-width: 35px;
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