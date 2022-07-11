<template>
  <div
    @click="showMenu()"
    class="border-left cell flex-fill"
    :class="isVisible ? 'active' : ''"
    role="button"
  >
    <div class="btn-grou">
      <span
        class="btn btn-default w-100 rounded-0 p-1"
        :class="isVisible ? 'btn-' + getColors[event.color].color : ''"
        data-toggle="dropdown"
        aria-expanded="false"
      >
        {{ day }}
      </span>
      <ul class="dropdown-menu p-0 bg-light">
        <li
          v-for="(color, index) in getColors"
          :key="index"
          @click="checkedDay(index)"
          class="d-flex flex-row border-bottom"
        >
          <div class="p-1 text-left flex-grow-1">{{ color.name }}</div>
          <div
            :class="[
              'btn-' + color.color,
              'text-' + color.color,
              'index-' + index,
            ]"
            class="p-1"
          >
            Color
          </div>
        </li>
        <li @click="remove()" class="d-flex flex-row border-bottom">
          <div class="p-1 text-left flex-grow-1">Remove</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
// import jwtInterceptor from '../../shared/jwtInterceptor'

export default {
  name: "Cell",
  props: {
    event: Object,
    day: Number,
    source_id: Number,
    fullDate: String,
  },
  data() {
    return {
      showmenu: false,
    };
  },
  computed: {
    ...mapGetters({
      getColors: "getColors",
      getSourceById: "getSourceById",
    }),
    isVisible() {
      if (this.event != null) {
        if (this.event.visible) {
          return true;
        } else {
          return false;
        }
      }
      return false;
    },
  },
  methods: {
    ...mapMutations({
      CREATE_SOURCE_DAY: "CREATE_SOURCE_DAY",
      UPDATE_SOURCE_DAY: "UPDATE_SOURCE_DAY",
      REMOVE_SOURCE_DAY: "REMOVE_SOURCE_DAY",
      SET_IS_SAVE: "SET_IS_SAVE",
    }),
    ...mapActions({
      loadSourceForMonth: "loadSourceForMonth",
    }),
    showMenu() {
      this.showmenu = !this.showmenu;
    },

    createNewEvent(color) {
      try {
        const data = {
          date: this.fullDate,
          color: color,
          source: this.source_id,
          state: "create",
          visible: true,
        };

        this.CREATE_SOURCE_DAY(data);
      } catch (err) {
        console.log(err);
      }
    },
    updateEvent(color) {
      try {
        this.event.state = "update";
        this.event.visible = true;
        this.event.color = color;
        this.SET_IS_SAVE(true)
      } catch (err) {
        this.err = err.response.data;
      }
    },
    changeColor(color){
        this.event.color = color;
    },

    async checkedDay(color) {
      if (this.event != null) {
        if ("origin" in this.event) {
          this.updateEvent(color);
        } else {
          this.changeColor(color);
        }
      } else {
        this.createNewEvent(color);
      }
      this.showmenu = !this.showmenu;
    },
    async remove() {
      try {
        this.event.state = "delete";
        this.event.visible = false;
        this.SET_IS_SAVE(true)
        this.showmenu = !this.showmenu;
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style scoped>
.cell {
  /* max-width: 35px; */
  min-width: 35px;
}
.menu {
  width: 150px;
  min-width: 150px;
  max-width: 250px;
}
/* .active{
    background-color: rgba(66, 85, 194, 0.801);
} */
.hour-cell {
  width: 5%;
}

.hour-cell:hover {
  background-color: cornflowerblue;
  cursor: pointer;
}
</style>