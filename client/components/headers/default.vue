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
        <img
          class="nav-logo d-block"
          src="~/assets/hc-libs/images/main/logo_healthcare.png"
          alt="vlearn-logo"
        />
      </div>
      <div class="nav-row">
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

        <!-- <div class="nav-icon-menu" @click.stop="onToggleVlearnMenu()">
          <i class="icon-grid2"></i>
          <vlearn-v-menu
            v-on-click-out-side="onVlearnMenuClose"
            :class="vlearnMenuCss()"
          ></vlearn-v-menu>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
// import { ClickOutSide } from '@/directives/ClickOutSide.js'
import { mapState } from 'vuex'
import defaultProfileUrl from '~/assets/hc-libs/images/main/face_default.png'
import VlearnProfileMenu from './ProfileMenu'
// import VlearnVMenu from './VirtualWorldMenu'

export default {
  name: 'VlearnNavBar',
  // directives: {
  //   onClickOutSide: ClickOutSide,
  // },
  components: {
    // VlearnVMenu,
    VlearnProfileMenu,
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
    isDisabledProfileMenu: {
      type: Boolean,
      default: undefined,
    },
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
    showProfile: {
      type: Boolean,
      default: true,
    },
  },
  data: () => ({
    isVlearnMenuOpen: false,
    isVlearnProfileOpen: false,
    defaultProfileUrl,
  }),
  computed: {},
  watch: {
    isDrawer(newVal, oldVal) {
      this.onVlearnMenuClose()
    },
  },
  beforeCreate: () => ({
    isVlearnMenuOpen: false,
    isVlearnProfileOpen: false,
  }),
  created: () => ({}),
  methods: {
    onToggleDrawer() {
      this.$emit('onToggleDrawer', '')
    },
    onToggleVlearnMenu() {
      this.isVlearnMenuOpen = !this.isVlearnMenuOpen
      this.isVlearnProfileOpen = false
    },
    onToggleVlearnProfile() {
      this.isVlearnProfileOpen = !this.isVlearnProfileOpen
      this.isVlearnMenuOpen = false
    },
    vlearnMenuCss() {
      return {
        'vlearn-menu-close': !this.isVlearnMenuOpen,
        'vlearn-menu-open': this.isVlearnMenuOpen,
      }
    },
    vlearnProfileCss() {
      return {
        'vlearn-menu-close': !this.isVlearnProfileOpen,
        'vlearn-menu-open': this.isVlearnProfileOpen,
      }
    },
    onVlearnMenuClose() {
      this.isVlearnMenuOpen = false
      this.isVlearnProfileOpen = false
    },
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
    border-bottom-color: rgba(0, 0, 0, 0.125);
    border-bottom: 1px solid #dddddd;
    height: 54px;
    justify-content: space-between;
    flex-direction: row;
    box-sizing: border-box;
    z-index: 998;

    &.fixed {
      position: fixed;
    }
  }

  &-logo {
    display: flex;
    max-width: 200px;
    padding-top: 12px;

    &.standalone {
      padding-left: 20px;
    }
  }

  &-row {
    display: flex;
    height: 100%;
    flex-direction: row;
    width: auto;
    align-items: center;
  }

  &-row-reverse {
    display: flex;
    height: 100%;
    flex-direction: row-reverse;
    width: auto;
    align-items: center;
  }

  &-icon {
    margin-left: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #888888;
    border-radius: 50%;
    height: 42px;
    width: 42px;
    cursor: pointer;

    &:hover {
      background: rgba(0, 0, 0, 0.04);
      color: #cc338b;
    }

    &.disabled {
      cursor: not-allowed;
      pointer-events: none;
    }
  }

  &-icon-menu {
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    margin-right: 5px;
    margin-left: 5px;
    color: #888888;
    border-radius: 50%;
    cursor: pointer;

    &:hover {
      background: rgba(0, 0, 0, 0.04);
      color: #cc338b;
    }
  }

  &-profile {
    display: flex;
    height: 42px;
    width: 42px;
    padding: 5px;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    cursor: pointer;

    & > img {
      display: flex;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 1px solid #f2f2f2;
      object-fit: cover;
    }

    &:hover {
      background: rgba(0, 0, 0, 0.04);
    }

    &.disabled {
      cursor: not-allowed;
      pointer-events: none;
    }
  }
}
.vlearn-menu {
  &-open {
    display: flex;
  }
  &-close {
    display: none;
  }
}

.navbar-light {
  color: #444444;
  background-color: #fff;
  border-bottom-color: rgba(0, 0, 0, 0.125);
  border-bottom: 1px solid #dddddd;
}

.navbar {
  padding: 0;
}
</style>
