<template>
  <div class="col-12 px-0">
    <div class="cd-tabs js-cd-tabs">
      <nav>
        <ul
          class="
            cd-tabs__navigation-2
            js-cd-navigation
            category-list
            font-tm
            my-auto
            d-flex
            justify-content-md-center justify-content-start
          "
          :class="{ 'no-active': !active }"
        >
          <li
            v-for="(tab, index) in tabs"
            :key="tab.name + activeIndex"
            @click="!tab.disabled && handleClick(index)"
          >
            <a
              v-if="tab.url && !tab.isNotShow"
              :href="tab.url"
              class="link-2 link-item p-0"
              :class="{
                active: index === activeIndex,
                'sub-tab': activeIndex !== -1,
                'sub-tab-active': activeIndex !== -1 && index === activeIndex,
                disabled: tab.disabled,
              }"
            >
              <div
                class="d-flex align-items-center justify-content-center h-100"
              >
                <span>{{ tab.name }}</span>
              </div>
            </a>
            <nuxt-link
              v-else-if="!tab.isNotShow"
              class="link-2 link-item p-0"
              :to="
                tab.path
                  ? tab.path.startsWith('/')
                    ? localePath(tab.path)
                    : tab.path
                  : ''
              "
              :class="{
                active: index === activeIndex,
                'sub-tab': activeIndex !== -1,
                'sub-tab-active': activeIndex !== -1 && index === activeIndex,
                disabled: tab.disabled,
              }"
            >
              <div
                class="d-flex align-items-center justify-content-center h-100"
              >
                <span>{{ tab.name }}</span>
              </div>
            </nuxt-link>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tabs: {
      type: Array,
      default: () => [],
    },
    activeIndex: {
      type: Number,
      default: -1,
    },
    active: {
      type: Boolean,
      default: true,
    },
  },
  created() {
    // console.log(props)
  },
  methods: {
    handleClick(index) {
      this.$emit('onChange', index)
    },
  },
}
</script>

<style lang="scss">
.cd-tabs {
  display: flex;
  justify-content: center;
  color: var(--vlearn-grey-dark);

  .no-active {
    .active-link {
      &:not(:hover) {
        color: inherit;
        border-color: var(--vlearn-white);
      }
    }
  }

  &__navigation-2 {
    a {
      white-space: nowrap;

      &:hover {
        color: var(--vlearn-primary);
        cursor: pointer;
      }
    }
  }

  .link-item {
    &.sub-tab {
      color: var(--vlearn-grey-dark);
      border-bottom: 3px solid transparent;

      &-active,
      &:hover {
        color: var(--vlearn-primary);
        border-bottom: 3px solid var(--vlearn-primary);
      }
    }

    &.disabled {
      opacity: 0.5;
      cursor: not-allowed;
      pointer-events: none;
    }
  }
}
</style>
