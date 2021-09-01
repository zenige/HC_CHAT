<template>
  <div class="sidebar-main-container">
    <div>
      <a href="#" class="sidebar-menu-main">
        <img
          class="sidebar-menu-main-icon"
          src="~/assets/hc-libs/images/main/stable_patient.png"
          alt="stable-patient"
        />
        <div class="sidebar-menu-main-item">Stable Patient</div>
      </a>
      <a href="#" class="sidebar-menu-main">
        <img
          class="sidebar-menu-main-icon"
          src="~/assets/hc-libs/images/main/emergency_patient.png"
          alt="emergency-patient"
        />
        <div class="sidebar-menu-main-item">Emergency Patient</div>
      </a>
      <a href="#" class="sidebar-menu-main">
        <img
          class="sidebar-menu-main-icon"
          src="~/assets/hc-libs/images/main/follow_up_patient.png"
          alt="follow-up-patient"
        />
        <div class="sidebar-menu-main-item">Follow-up Patient</div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({}),
  computed: {},
  watch: {},
  beforeMount() {},
  methods: {},
}
</script>

<style lang="scss">
.sidebar-main-container {
  @media (max-width: 1200px) {
    display: none;
  }
  display: flex;
  position: fixed;
  flex-direction: column;
  border-right: 1px solid #ececec;
  width: 200px;
  background: #fff;
  border-bottom-color: rgba(0, 0, 0, 0.125);
  border-bottom: 1px solid #dddddd;
  height: 100%;
  box-sizing: border-box;
  z-index: 99;
  margin-top: 52px;
}
.sidebar-menu {
  &-main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-top: 1rem;
    cursor: pointer;
    color: #333333;
    font-weight: 600;
    &:hover {
      color: #e05582;
      background-color: #f5f5f5;
      transition: all 0.2s ease-in-out;
    }

    &-item {
      width: 100%;
      display: flex;
      justify-content: center;
      padding-left: 16px;
      height: 50px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.125);
      cursor: pointer;
      font-size: 18px;
      height: unset;
      padding: 0.35rem 1.25rem;
    }

    &-icon {
      max-width: 40px;
      max-height: 40px;
    }
  }
}
</style>
