<template>
  <div :class="drawerMenuClass()">
    <div class="side-menu-nav">
      <div class="nav-icon" @click.stop="onSetHideDrawer()">
        <i class="icon-cross2"></i>
      </div>
    </div>
    <div v-for="item in menus" :key="item.name" @click.stop="onSetHideDrawer()">
      <NuxtLink v-if="item.isEnable" :to="item.link" class="side-menu-main">
        <div class="side-menu-main-item">{{ item.name }}</div>
      </NuxtLink>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VlearnSideMenu',
  props: ['isDrawer'],
  data: () => ({
    isOpen: false,
    menus: [],
  }),
  computed: {},
  watch: {
    isDrawer(newVal) {
      this.isOpen = newVal
    },
    workspace() {
      this.setMenuBasePathLink()
    },
    user() {
      this.setMenuBasePathLink()
    },
  },
  beforeMount() {
    this.setMenuBasePathLink()
  },
  methods: {
    drawerMenuClass() {
      return {
        'side-menu-container-close': !this.isOpen,
        'side-menu-container-open': this.isOpen,
      }
    },
    onSetHideDrawer() {
      this.$emit('onHideDrawer', this.isOpen)
    },
    setMenuBasePathLink() {
      this.menus = [
        {
          name: 'Stable Patient',
          link: '#',
          isEnable: true,
        },
        {
          name: 'Emergency Patient',
          link: '#',
          isEnable: true,
        },
        {
          name: 'Follow up Patient',
          link: '#',
          isEnable: true,
        },
      ]
    },
  },
}
</script>

<style lang="scss">
.side-menu {
  @mixin container {
    display: flex;
    position: absolute;
    flex-direction: column;
    border-right: 1px solid #ececec;
    width: 270px;
    background: #fff;
    color: #444444;
    border-bottom-color: rgba(0, 0, 0, 0.125);
    border-bottom: 1px solid #dddddd;
    height: 100%;
    flex-direction: column;
    box-sizing: border-box;
    box-shadow: 0.25rem 0 1rem rgba(0, 0, 0, 0.35);
    z-index: 99;
  }
  &-container-open {
    @include container();
  }

  &-container-close {
    @include container();
    margin-left: -300px;
  }

  &-nav {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 52px;
    background: #f5f5f5;
    width: 100%;
    border-bottom: 1px solid rgba(0, 0, 0, 0.125);
    .back-icon {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 42px;
      width: 42px;
    }
  }

  &-main {
    display: flex;
    flex-direction: column;

    &-item {
      display: flex;
      flex-direction: row;
      align-items: center;
      padding-left: 16px;
      height: 50px;
      color: #666;
      border-bottom: 1px solid rgba(0, 0, 0, 0.125);
      cursor: pointer;

      &:hover {
        color: #333;
        background-color: #f5f5f5;
        transition: all 0.2s ease-in-out;
      }
    }
  }
}
.side-menu-main-item {
  color: #000;
  font-size: 18px;
  height: unset;
  padding: 0.35rem 1.25rem;
}
@media only screen and (max-width: 1200px) {
  .side-menu {
    &-container-open {
      box-shadow: 0.25rem 0 1rem rgba(0, 0, 0, 0.35);
      z-index: 999;
      transition: all 0.2s linear;
    }

    &-container-close {
      box-shadow: 0.25rem 0 1rem rgba(0, 0, 0, 0.35);
      z-index: 999;
      transition: all 0.2s linear;
    }
  }
}
</style>
