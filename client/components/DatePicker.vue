<template>
  <div class="date-picker input-group border-gray border rounded hc_navbar">
    <input
      v-if="value == 'Invalid Date'"
      required
      type="text"
      class="form-control pickadate-accessibility"
      :placeholder="placeholder"
      :value="''"
    />
    <input
      v-else
      type="text"
      required
      class="form-control pickadate-accessibility"
      :placeholder="placeholder"
      :value="value"
    />
    <span class="input-group-prepend">
      <span class="input-group-text"
        ><i class="icon-calendar22 txt_grey"></i
      ></span>
    </span>
  </div>
</template>

<script>
import jQuery from 'jquery'

if (process.client) {
  window.jQuery = jQuery

  require('../assets/hc-libs/js/plugins/pickers/pickadate/picker.date')
}

export default {
  props: ['value', 'placeholder'],
  watch: {
    value(newValue) {
      jQuery('.pickadate-accessibility').val(newValue)
    },
  },
  mounted() {
    const selector = jQuery('.pickadate-accessibility')

    selector.pickadate({
      labelMonthNext: 'Go to the next month',
      labelMonthPrev: 'Go to the previous month',
      labelMonthSelect: 'Pick a month from the dropdown',
      labelYearSelect: 'Pick a year from the dropdown',
      selectMonths: true,
      selectYears: 100,
      format: 'd mmmm, yyyy',
      max: true,
    })

    selector.change((event) => {
      this.$emit('change', event)

      this.$emit('input', event.target.value)
    })
  },
}
</script>

<style lang="scss">
.date-picker {
  .pickadate-accessibility {
    &::placeholder {
      color: #999999;
    }
  }
}

.rounded {
  border-radius: 8px !important;
}
</style>
