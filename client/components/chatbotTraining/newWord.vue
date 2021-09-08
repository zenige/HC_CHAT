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
              @click="openTrainWordModal()"
              class="login__btn-submit hcb-btn btn btn_hcb_green btn-block"
              style="height: 2.5rem"
            >
              Train
            </button>
            <button
              @click="openDeleteWordModal()"
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
            <span class="txt_vla_grey">({{ newWordData.length }})</span>
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
            :items="newWordData"
            :per-page="perPage"
            :current-page="currentPage"
            :fields="fields"
            :filter="filter"
          >
            <template #cell(word)="data">
              <div v-if="data.item.editable === false">
                <div>
                  {{ data.item.word }}
                </div>
              </div>
              <b-form-input
                autofocus
                v-if="data.item.editable === true"
                v-model="data.item.word"
                @keyup.enter="
                  data.item.editable = false
                  $emit('update')
                "
              />
            </template>
            <template #cell(answer)="data">
              <div v-if="data.item.editable === false">
                <div>
                  {{ data.item.answer }}
                </div>
              </div>
              <b-form-input
                autofocus
                v-if="data.item.editable === true"
                v-model="data.item.answer"
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

    <TrainWordModal
      :isOpen="isShowTrainWordModal"
      :onCancel="closeTrainWordModal"
      :onDelete="onTrainWord"
    ></TrainWordModal>
    <DeleteWordModal
      :isOpen="isShowDeleteWordModal"
      :onCancel="closeDeleteWordModal"
      :onDelete="onDeleteWord"
    ></DeleteWordModal>
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
  props: {},
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
      trainSelected: [],
      fields: [
        {
          key: 'selected',
          label: 'Select',
        },
        {
          key: 'question',
          label: 'Word',
          sortable: true,
        },
        {
          key: 'answer',
          label: 'Answer',
          sortable: true,
        },
        {
          key: 'confident',
          label: 'Confident',
          sortable: true,
        },
        {
          key: 'count',
          label: 'Count',
          sortable: true,
        },
        {
          key: 'actions',
          label: '',
          sortable: false,
        },
      ],
      newWordData: [],
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
      this.newWordData.map(function (item) {
        item.selected = value
        return item
      })
    },
    currentPage(value) {
      this.getNewWordData(value, this.perPage, 'question')
    },
  },
  async mounted() {
    await this.getNewWordData(1, 2, 'question')
  },
  computed: {
    rows() {
      return this.newWordData.length
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
    async onTrainWord() {
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.post('train/trained/many', this.trainSelected)
      this.onDeleteWord()
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
    onDeleteWord() {
      let selectedRow = this.newWordData.filter(
        (item) => item.selected === true
      )
      this.newWordData = this.newWordData.filter(
        (item) => !selectedRow.includes(item)
      )
    },
    async getNewWordData(page, limit, orderBy) {
      let { data } = await this.$axios.get(
        `train/training?pages=${page}&limit=${limit}&order_by=${orderBy}`
      )
      this.newWordData = data.map((item) => {
        return {
          answer: item.answer,
          time: item.time,
          count: item.count,
          confident: item.confident,
          question: item.question,
          id: item.id,
          selected: false,
          editable: false,
        }
      })
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
