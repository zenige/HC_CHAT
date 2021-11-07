<template>
  <div>
    <div class="container-fulid border_top_1_f3 border_bottom_1_f3">
      <div class="container px-md-0">
        <div class="row d-flex align-items-center">
          <div class="col-12 px-0">
            <div class="">
              <div class="hori_menu">
                <nav class="scroll txt_hori_menu">
                  <a
                    v-for="(menu, index) in menus"
                    :key="index"
                    :class="[
                      'nav-item nav_item_hori_menu cursor-pointer',
                      { active: value === menu.id },
                    ]"
                    @click="$emit('input', menu.id)"
                  >
                    {{ menu.text }}
                  </a>
                </nav>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '',
    },
    menus: {
      type: Array,
      default: () => [],
    },
  },
}
</script>

<style scoped>
.hori_menu .nav-item {
  color: #888 !important;
}
.txt_hori_menu a.active,
.txt_hori_menu a:hover.active {
  color: #cc0000 !important;
  border-bottom: 3px solid !important;
}
@media (max-width: 576px) {
  a:hover,
  .hover-link:hover .card-title,
  .icon_hover:hover,
  a.active {
    color: #cc0000 !important;
  }
}
</style>
