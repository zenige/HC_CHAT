<template>
  <div>
    <b-table striped hover :items="items" :fields="fields">
      <template #cell(age)="data">
        <input type="text" v-model="data.value">
      </template>
      <template #cell(bbbbbbb)="data">
        <input type="checkbox" v-model="data.value" />
      </template>
    </b-table>  
  </div>
</template>

<script>
export default {
  data() {
      return {
        // Note 'isActive' is left out and will not appear in the rendered table
        fields: [
          {
            key: 'last_name',
            sortable: true
          },
          {
            key: 'first_name',
            sortable: true
          },
          {
            key: 'age',
            label: 'Person age',
            sortable: true,
            variant: 'danger'
          },
          {
            key: 'bbbbbbb',
            label: 'bg',
            selected: true
          }
        ],
        items: [
          { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald', bbbbbbbb: '' },
          { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw', bbbbbbbb: '' },
          { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson', bbbbbbbb: '' },
          { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney', bbbbbbbb: '' }
        ]
      }
    },
    methods: {
      onPreviewClick(value, index, item) {
    }
  }
  }
</script>

<style lang="scss">
.txt_hc_title {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
</style>
