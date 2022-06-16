<template>
    <div>
        <span @click="showForm()" class="btn btn-light rounded-0 d-block">
         <i class="fas  fa-lg fa-plus-square text-success"></i> Add </span>
        <div v-show="showfrom" class="" >
        <form @submit.prevent="createSource()">
        <div class=" position-absolute p-2 py-1 bg-white  border shadow" >
        <div class="modal-dialog modal-md my-0">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">New Source </h5>
                    <button @click="showForm()" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <div class="modal-body">
                    <div class="form-group">
                        <label for="recipient-name" class="col-form-label">Source Name *</label>
                         <input v-model.trim="form.name" type="text" class="form-control" >
                    </div>
                    <div class="form-group">
                        <label for="message-text" class="col-form-label">Description </label>
                        <textarea class="form-control" id="message-text"></textarea>
                    </div>
                </div>

                <div class="modal-footer">
                    <button @click="showForm()" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">Create</button>
                </div>
            </div>
        </div>
        </div>
        </form>
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