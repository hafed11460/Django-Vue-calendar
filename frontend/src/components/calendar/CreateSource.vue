<template>
    <div>
         <span @click="showForm()" class="btn btn-success rounded-0 d-block">Add</span>
        <div v-show="showfrom" class="position-relative" >
            <div class="position-absolute border p-2 py-4 ml-1 bg-light from">
            <form @submit.prevent="createSource()">
                <div class="form-group">
                    <label for="formGroupExampleInput">Source Name</label>
                    <input v-model.trim="form.name" type="text" class="form-control" >
                </div>
                <div class="d-flex justify-content-between">
                    <button type="submit" class="btn btn-primary">Add</button>
                    <span @click="showForm()"  class="btn btn-primary">Close</span>
                </div>
            </form>
        </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
    export default{
        name:'CreateSource',
        data(){
            return {
                form:{
                    name:'',
                },
                showfrom:false,
            }
        },
        computed:{
             ...mapGetters({
          getSourcesList:"getSourcesList",
        }),
        },
        methods:{
            ...mapActions({
             actionCreateSource:'createSource',
        }),
            initForm(){
                this.form.name = ''
            },
            showForm(){
                this.showfrom = !this.showfrom
            },
            async createSource(){
                const data = {
                        name:this.form.name,
                        user:1
                    }
                if(await this.actionCreateSource(data)){
                    this.showfrom = !this.showfrom
                    this.initForm()
                }
            },
        }

    }
</script>

<style scoped>
.from {
    min-width: 350px;
}
</style>