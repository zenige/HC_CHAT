<template>
  <div>
    <div class="row">
      <div class="col-md-12 pb_me-4 my-3">
        <div class="row d-flex align-items-center">
          <div class="col-8 col-md-4 pb_me-4">
            <div
              class="
                form-group
                mb-0
                border_search_gray
                form-group-feedback form-group-feedback-right
              "
            >
              <div class="input-group">
                <span class="input-group-append"
                  ><span
                    class="
                      input-group-text input-group-text-search-border
                      rounded-left
                    "
                    ><i class="icon-search4 txt_grey"></i></span
                ></span>
                <input
                  v-model="filter"
                  type="search"
                  class="
                    my-auto
                    form-control
                    txt_black
                    rounded-right
                    form-control-search-border
                    h2dot5
                  "
                  style="margin-right: 1rem"
                  placeholder="Type a word..."
                />
                <div class="form-control-feedback" @click="filter = ''">
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4 col-md-8 pb_me-4 text-right">
            <button
              @click="onAddNewWord()"
              class="login__btn-submit hcb-btn btn btn_hcb_green btn-block"
              style="height: 2.5rem"
            >
              Add Word
            </button>
            <button
              @click="onDeleteWord()"
              class="login__btn-submit hcb-btn btn btn_hcb_red btn-block"
              style="height: 2.5rem"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 pb_me-4 my-3">
        <div class="row d-flex align-items-center">
          <div class="txt_hc_content">
            Total words
            <span class="txt_vla_grey">({{ trainedWords.length }})</span>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 pb_me-4">
        <div class="row d-flex align-items-center">
          <!-- <v-data-table
            v-model="selected"
            :headers="headers"
            :items="desserts"
            :single-select="singleSelect"
            :items-per-page="selectedgg"
            hide-default-footer
            item-key="name"
            show-select
            class="elevation-1"
          >
          </v-data-table> -->
          <b-table
            striped
            hover
            id="my-table"
            :items="trainedWords"
            :per-page="perPage"
            :current-page="currentPage"
            :fields="fields"
            :filter="filter"
          >
            <template #cell(first_name)="data">
              <div v-if="data.item.editable === false">
                <div>
                  {{ data.item.first_name }}
                </div>
              </div>
              <b-form-input
                autofocus
                v-if="data.item.editable === true"
                v-model="data.item.first_name"
                @keyup.enter="
                  data.item.editable = false
                  $emit('update')
                "
              />
            </template>
            <template #cell(last_name)="data">
              <div v-if="data.item.editable === false">
                <div>
                  {{ data.item.last_name }}
                </div>
              </div>
              <b-form-input
                autofocus
                v-if="data.item.editable === true"
                v-model="data.item.last_name"
                @keyup.enter="
                  data.item.editable = false
                  $emit('update')
                "
              />
            </template>
            <template #cell(selected)="data">
              <input type="checkbox" v-model="data.item.selected" />
            </template>
            <template #head(selected)>
              <input type="checkbox" v-model="selectAll" />
              <span>Select All</span>
            </template>

            <template #cell(actions)="data">
              <b-button
                v-if="data.item.editable === false"
                variant="primary"
                @click="data.item.editable = true"
                >Edit</b-button
              >
              <b-button
                v-if="data.item.editable === true"
                variant="danger"
                @click="data.item.editable = false"
                >Cancle</b-button
              >
              <b-button
                v-if="data.item.editable === true"
                variant="success"
                @click="data.item.editable = false"
                >Save</b-button
              >
            </template>
          </b-table>
          <div class="mt-3">
            <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              first-text="First"
              prev-text="<"
              next-text=">"
              last-text="Last"
              aria-controls="my-table"
            ></b-pagination>
          </div>
        </div>
        <!-- <b-form-select v-model="selectedgg" @change="perpage(selectedgg)" :options="options"></b-form-select> -->
      </div>
    </div>

    <DeleteWordModal
      :isOpen="isShowDeleteWordModal"
      :onCancel="closeDeleteWordModal"
      :onDelete="onDeleteWord"
    ></DeleteWordModal>
    <TrainWordModal
      :isOpen="isShowTrainWordModal"
      :onCancel="closeTrainWordModal"
      :onDelete="onTrainWord"
    ></TrainWordModal>
  </div>
</template>

<script>
export default {
  components: {
    DeleteWordModal: () =>
      import('~/components/chatbotTraining/DeleteWordModal.vue'),
    TrainWordModal: () =>
      import('~/components/chatbotTraining/TrainWordModal.vue'),
  },

  data() {
    return {
      isShowDeleteWordModal: false,
      isShowTrainWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      filter: '',
      perPage: 10,
      currentPage: 1,
      fields: [
        {
          key: 'selected',
          label: 'Select',
        },
        {
          key: 'first_name',
          label: 'First name',
          sortable: true,
        },
        {
          key: 'last_name',
          label: 'Last name',
          sortable: true,
        },
        {
          key: 'age',
          label: 'Person age',
          sortable: true,
        },
        {
          key: 'actions',
          label: '',
          sortable: false,
        },
      ],
      trainedWords: [
        {
          age: 40,
          first_name: 'Dickerson',
          last_name: 'Macdonald',
          selected: false,
          editable: false,
        },
        {
          age: 21,
          first_name: 'Larsen',
          last_name: 'Shaw',
          selected: false,
          editable: false,
        },
        {
          age: 89,
          first_name: 'Geneva',
          last_name: 'Wilson',
          selected: false,
          editable: false,
        },
        {
          age: 38,
          first_name: 'Jami',
          last_name: 'Carney',
          selected: false,
          editable: false,
        },
      ],
      // Note 'isActive' is left out and will not appear in the rendered table
      // headers: [
      //   {
      //     text: 'Dessert (100g serving)',
      //     align: 'start',
      //     value: 'name',
      //   },
      //   { text: 'Calories', value: 'calories' },
      //   { text: 'Fat (g)', value: 'fat' },
      //   { text: 'Carbs (g)', value: 'carbs' },
      //   { text: 'Protein (g)', value: 'protein' },
      //   { text: 'Iron (%)', value: 'iron' },
      // ],
      // desserts: [
      //   {
      //     name: 'Frozen Yogurt',
      //     calories: 159,
      //     fat: 6.0,
      //     carbs: 24,
      //     protein: 4.0,
      //     iron: '1%',
      //   },
      //   {
      //     name: 'Ice cream sandwich',
      //     calories: 237,
      //     fat: 9.0,
      //     carbs: 37,
      //     protein: 4.3,
      //     iron: '1%',
      //   },
      // ],
      // selected: [],
      // options: [
      //   { value: 5, text: '5' },
      //   { value: 10, text: '10' },
      // ],
      // selectedgg: '',
    }
  },
  watch: {
    selectAll(value) {
      this.trainedWords.map(function (item) {
        item.selected = value
        return item
      })
    },
  },
  computed: {
    rows() {
      return this.trainedWords.length
    },
  },
  methods: {
    onPreviewClick(value, index, item) {},

    onDeleteWord() {
      console.log('delete word')
    },
    openDeleteWordModal() {
      this.isShowDeleteWordModal = true
    },
    closeDeleteWordModal() {
      this.isShowDeleteWordModal = false
    },
    openTrainWordModal() {
      this.isShowTrainWordModal = true
    },
    closeTrainWordModal() {
      this.isShowTrainWordModal = false
    },
    onEdit() {
      this.edit = !this.edit
    },
    onAddNewWord() {
      this.trainedWords.push({
        age: 0,
        first_name: '',
        last_name: '',
        selected: false,
        editable: false,
      })
    },
    onDeleteWord() {
      let selectedRow = this.trainedWords.filter(
        (item) => item.selected === true
      )
      this.trainedWords = this.trainedWords.filter(
        (item) => !selectedRow.includes(item)
      )
    },
  },
}
</script>

<style lang="scss">
.hcb-btn {
  height: 40px;
  margin-top: 0 !important;
  max-width: 120px !important;
}

.txt_hc_title {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 36px;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}

.txt_hc_content {
  font-family: 'TrueTextBOnline-Bold';
  font-size: 24px;
  font-weight: 600;
  font-style: normal;
  line-height: 1rem;
  color: #333333;
}
</style>
