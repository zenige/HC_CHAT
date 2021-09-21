<template>
  <div>
    <div
      id="main-nav-bar"
      class="
        nav-container
        fixed-top
        navbar navbar-expand-xl navbar-sm navbar-light
        justify-content-between
      "
    >
      <div class="nav-row">
        <div class="nav-icon d-flex" @click.stop="onToggleDrawer()">
          <i class="icon-menu7"></i>
        </div>
        <NuxtLink :to="'/'">
          <img
            class="nav-logo d-block"
            src="~/assets/hc-libs/images/main/logo_healthcare2.png"
            alt="vlearn-logo"
          />
        </NuxtLink>
      </div>
      <!-- <div class="nav-row">
        <template v-if="showProfile">
          <div
            class="nav-profile"
            :class="{ disabled: isDisabledProfileMenu }"
            @click.stop="onToggleVlearnProfile()"
          >
            <img :src="defaultProfileUrl" alt />
            <vlearn-profile-menu
              v-on-click-out-side="onVlearnMenuClose"
              :class="vlearnProfileCss()"
            ></vlearn-profile-menu>
          </div>
        </template>
      </div> -->
    </div>
  </div>
</template>

<script>
import { ClickOutSide } from '@/directives/ClickOutSide.js'
// import { mapState } from 'vuex'
// import defaultProfileUrl from '~/assets/hc-libs/images/main/face_default.png'
// import VlearnProfileMenu from './ProfileMenu'

export default {
  name: 'HealthcareNavbar',
  directives: {
    onClickOutSide: ClickOutSide,
  },
  components: {
    // VlearnProfileMenu,
  },
  props: {
    isDrawer: {
      type: Boolean,
      default: undefined,
    },
    // isDisabledUserMenu: {
    //   type: Boolean,
    //   default: undefined,
    // },
    // isDisabledProfileMenu: {
    //   type: Boolean,
    //   default: undefined,
    // },
    // hideUserMenu: {
    //   type: Boolean,
    //   default: false,
    // },
    // isChild: {
    //   type: Boolean,
    //   default: false,
    // },
    // isFixed: {
    //   type: Boolean,
    //   default: false,
    // },
    // showProfile: {
    //   type: Boolean,
    //   default: true,
    // },
  },
  data: () => ({
    isVlearnMenuOpen: false,
    isVlearnProfileOpen: false,
    // defaultProfileUrl,
  }),
  computed: {},
  watch: {
    // isDrawer(newVal, oldVal) {
    //   this.onVlearnMenuClose()
    // },
  },
  beforeCreate: () => ({
    // isVlearnMenuOpen: false,
    // isVlearnProfileOpen: false,
  }),
  created: () => ({}),
  methods: {
    onToggleDrawer() {
      this.$emit('onToggleDrawer', '')
    },
    // onToggleVlearnMenu() {
    //   this.isVlearnMenuOpen = !this.isVlearnMenuOpen
    //   this.isVlearnProfileOpen = false
    // },
    // onToggleVlearnProfile() {
    //   this.isVlearnProfileOpen = !this.isVlearnProfileOpen
    //   this.isVlearnMenuOpen = false
    // },
    // vlearnMenuCss() {
    //   return {
    //     'vlearn-menu-close': !this.isVlearnMenuOpen,
    //     'vlearn-menu-open': this.isVlearnMenuOpen,
    //   }
    // },
    // vlearnProfileCss() {
    //   return {
    //     'vlearn-menu-close': !this.isVlearnProfileOpen,
    //     'vlearn-menu-open': this.isVlearnProfileOpen,
    //   }
    // },
    // onVlearnMenuClose() {
    //   this.isVlearnMenuOpen = false
    //   this.isVlearnProfileOpen = false
    // },
    // openToTrueVirtual(link) {
    //   window.open(link)
    // },
  },
}
</script>

<style lang="scss">
.nav {
  &-container {
    position: fixed;
    display: flex;
    width: 100%;
    color: #444444;
    background-color: #fff;
    border-bottom: 1px solid #e5e5e5;
    height: 56px;
    justify-content: space-between;
    flex-direction: row;
    box-sizing: border-box;
    z-index: 997;
    padding: 0.5rem;
  }

  &-row {
    display: flex;
    height: 100%;
    flex-direction: row;
    width: auto;
    align-items: center;
  }

  &-icon {
    @media (max-width: 1200px) {
      display: flex !important;
    }
    display: none !important;
    align-items: center;
    justify-content: center;
    color: #888888;
    border-radius: 50%;
    height: 42px;
    width: 42px;
    cursor: pointer;

    &:hover {
      background: rgba(0, 0, 0, 0.04);
      color: #10c4cc;
    }
  }

  &-logo {
    @media (max-width: 1200px) {
      display: flex !important;
    }
    display: none !important;
    &.standalone {
      padding-left: 1rem;
    }
  }
}
</style>
