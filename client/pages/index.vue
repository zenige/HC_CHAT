<template>
  <div class="container">
    <Loader v-if="!isLoading" />
    <div v-else class="hc_navbar">
      <div class="container fitscreen" style="padding: 2rem 0">
        <div class="row d-flex align-items-center">
          <div class="col-8 col-md-4">
            <div class="border_search_gray form-group-feedback-right">
              <div class="input-group">
                <span class="input-group-append"
                  ><span
                    class="
                      input-group-text input-group-text-search-border
                      rounded-left
                    "
                    ><i class="icon-search4 txt_grey mr-2"></i></span
                ></span>
                <b-form-input
                  v-model="filter"
                  type="search"
                  class="
                    form-control
                    rounded-right
                    form-control-search-border
                    h2dot5
                  "
                  style="margin-right: 1rem"
                  placeholder="Search for a word..."
                >
                </b-form-input>
                <div
                  class="form-control-feedback"
                  :disabled="!filter"
                  @click="filter = null"
                  style="cursor: pointer"
                >
                  <i class="icon-cross3 txt_grey" style="height: 22px"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4 col-md-8 text-right">
            <button
              @click="openTrainWordModal()"
              class="hcb-btn btn btn_hcb_green btn-block"
            >
              Train word
            </button>
            <button
              @click="openDeleteWordModal()"
              class="hcb-btn btn btn_hcb_red btn-block"
            >
              Delete
            </button>
          </div>
        </div>
        <div class="col-md-12" style="padding-top: 2rem; padding-bottom: 1rem">
          <div class="row d-flex align-items-center">
            <div class="txt_hc_head_total">
              Total words
              <span class="txt_vla_grey">({{ rows }})</span>
            </div>
          </div>
        </div>
        <div class="col-md-12">
          <div class="row d-flex align-items-center justify-content-center">
            <b-table
              responsive
              id="newWord-table"
              :items="newWordData"
              :fields="fields"
              :per-page="0"
              :current-page="currentPage"
              :tbody-tr-class="selectedRowClass"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
            >
              <template #head(selected)>
                <div class="d-flex align-items-center">
                  <b-form-checkbox v-model="selectAll"></b-form-checkbox>
                  <span>Select All</span>
                </div>
              </template>
              <template #cell(selected)="data">
                <b-form-checkbox v-model="data.item.selected">
                </b-form-checkbox>
              </template>
              <template #cell(question)="data">
                <div
                  v-if="data.item.editable === false"
                  class="d-flex justify-content-start"
                >
                  <div class="word-data-text">
                    {{ data.item.question }}
                  </div>
                </div>
                <div v-if="data.item.editable === true">
                  <b-form-textarea
                    autofocus
                    v-model="changedQuestionData[data.index]"
                    rows="3"
                    max-rows="6"
                    no-auto-shrink
                  />
                </div>
              </template>
              <template #cell(answer)="data">
                <div v-if="data.item.editable === false">
                  <div class="word-data-text">
                    {{ data.item.answer }}
                  </div>
                </div>
                <b-form-textarea
                  autofocus
                  v-if="data.item.editable === true"
                  v-model="changedAnswerData[data.index]"
                  rows="3"
                  max-rows="6"
                  no-auto-shrink
                />
              </template>
              <template #cell(confident)="data">
                <div class="d-flex justify-content-end">
                  {{ data.item.confident }}
                </div>
              </template>
              <template #head(count)>
                <div class="d-flex justify-content-end">Count</div>
              </template>
              <template #cell(count)="data">
                <div class="d-flex justify-content-end">
                  {{ data.item.count }}
                </div>
              </template>
              <template #head(action)>
                <div class="d-flex justify-content-center">Action</div>
              </template>
              <template #cell(action)="data">
                <div
                  v-if="data.item.editable === false"
                  class="d-flex justify-content-center"
                >
                  <button
                    @click="editWord(data)"
                    class="hcb-btn-light btn btn_hcb_blue_light btn-block"
                  >
                    Edit
                  </button>
                </div>
                <div
                  class="row d-flex justify-content-center align-items-center"
                  v-if="data.item.editable === true"
                >
                  <button
                    @click="saveWord(data)"
                    class="hcb-btn-light btn btn_hcb_green_light mr-2 btn-block"
                  >
                    Save
                  </button>
                  <div @click="cancleEditWord(data)" class="txt_grey_cancel">
                    Cancel
                  </div>
                </div>
              </template>
            </b-table>
            <div style="margin-top: 0.5rem">
              <b-pagination
                v-model="currentPage"
                :total-rows="totalNewWord"
                :per-page="perPage"
                aria-controls="newWord-table"
                first-number
                last-number
                align="center"
                class="myPaginattion"
              ></b-pagination>
            </div>
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
    </div>
  </div>
</template>

<script>
const ASCENDING = 'ASCENDING'
const DESCENDING = 'DESCENDING'

export default {
  components: {
    DeleteWordModal: () => import('~/components/modals/DeleteWordModal.vue'),
    TrainWordModal: () => import('~/components/modals/TrainWordModal.vue'),
    Loader: () => import('~/components/Loader.vue'),
  },
  props: {},
  data() {
    return {
      sortBy: 'question',
      sortDesc: false,
      filter: null,
      isLoading: false,
      isShowDeleteWordModal: false,
      isShowTrainWordModal: false,
      edit: false,
      selectAll: false,
      selectedRow: {},
      perPage: 10,
      currentPage: 1,
      trainSelected: [],
      deleteSelected: [],
      totalNewWord: 0,
      changedQuestionData: [],
      changedAnswerData: [],
      fields: [
        {
          key: 'selected',
          label: 'Select',
          thClass: 'newWordthSelect-Class',
          tdClass: 'newWordtdSelect-Class',
        },
        {
          key: 'question',
          label: 'Question',
          sortable: true,
          thClass: 'newWordthQuestion-Class',
          tdClass: 'newWordtdQuestion-Class',
        },
        {
          key: 'answer',
          label: 'Answer',
          sortable: true,
          thClass: 'newWordthAnswer-Class',
          tdClass: 'newWordtdAnswer-Class',
        },
        {
          key: 'confident',
          label: 'Confident',
          sortable: true,
          thClass: 'newWordthConfident-Class',
          tdClass: 'newWordtdConfident-Class',
        },
        {
          key: 'count',
          label: 'Count',
          sortable: true,
          thClass: 'newWordthCount-Class',
          tdClass: 'newWordtdCount-Class',
        },
        {
          key: 'action',
          label: 'Action',
          sortable: false,
          thClass: 'newWordthAction-Class',
          tdClass: 'newWordtdAction-Class',
        },
      ],
      newWordData: [],
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
      if (!this.filter) {
        this.perPage = 10
        this.getNewWordData(
          this.filter,
          value,
          this.perPage,
          this.sortBy,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      }
    },
    filter(value) {
      if (value) {
        this.currentPage = 1
        this.perPage = this.newWordData.length
        setTimeout(() => {
          this.getNewWordData(
            value,
            this.currentPage,
            this.perPage,
            this.sortBy,
            this.sortDesc ? DESCENDING : ASCENDING
          )
        }, 250)
      } else if (!value) {
        this.currentPage = 1
        this.perPage = 10
        this.getNewWordData(
          value,
          this.currentPage,
          this.perPage,
          this.sortBy,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      }
    },
    sortBy(value) {
      console.log(value)
      if (value) {
        this.getNewWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          value,
          this.sortDesc ? DESCENDING : ASCENDING
        )
      } else if (!value) {
        this.getNewWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          'question',
          this.sortDesc ? DESCENDING : ASCENDING
        )
        this.sortBy = 'question'
      }
    },
    sortDesc(value) {
      if (!value) {
        this.getNewWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          this.sortBy,
          ASCENDING
        )
      } else if (value) {
        this.getNewWordData(
          this.filter,
          this.currentPage,
          this.perPage,
          this.sortBy,
          DESCENDING
        )
      }
    },
  },
  async mounted() {
    await this.getNewWordData(
      this.filter,
      this.currentPage,
      this.perPage,
      this.sortBy,
      ASCENDING
    )
    this.isLoading = true
  },
  computed: {
    rows() {
      return this.totalNewWord
    },
    sortData() {
      if (this.sortDesc === false) {
        return ASCENDING
      } else {
        return DESCENDING
      }
    },
  },
  methods: {
    selectedRowClass(item) {
      if (item.selected === true) return 'row-selected'
    },
    openDeleteWordModal() {
      this.deleteSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      if (this.deleteSelected.length >= 1) {
        this.isShowDeleteWordModal = true
      } else {
        ;(this.isShowDeleteWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeDeleteWordModal() {
      this.selectAll = false
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
      this.trainSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      if (this.trainSelected.length >= 1) {
        this.isShowTrainWordModal = true
      } else {
        ;(this.isShowTrainWordModal = false),
          this.$bvToast.toast('Please select any word', {
            variant: 'danger',
            toaster: 'b-toaster-bottom-left',
            noCloseButton: true,
          })
      }
    },
    closeTrainWordModal() {
      this.isShowTrainWordModal = false
    },
    async onDeleteWord() {
      this.deleteSelected = this.newWordData.filter(
        (item) => item.selected === true
      )
      await this.$axios.delete('train/training/delete/many', {
        data: this.deleteSelected,
      })
      await this.getNewWordData(
        this.filter,
        this.currentPage,
        10,
        'question',
        ASCENDING
      )
      this.selectAll = false
    },
    editWord(data) {
      this.changedQuestionData[data.index] = data.item.question
      this.changedAnswerData[data.index] = data.item.answer
      data.item.editable = true
    },
    cancleEditWord(data) {
      data.item.editable = false
    },
    async saveWord(data) {
      if (
        this.changedQuestionData[data.index] &&
        this.changedAnswerData[data.index]
      ) {
        data.item.question = this.changedQuestionData[data.index]
        data.item.answer = this.changedAnswerData[data.index]
        await this.$axios.patch('train/training/' + data.item.id, {
          question: data.item.question,
          answer: data.item.answer,
        })
        data.item.editable = false
      } else {
        this.$bvToast.toast('Please fill all required fields', {
          variant: 'danger',
          toaster: 'b-toaster-bottom-left',
          noCloseButton: true,
        })
      }
    },
    async getNewWordData(filter, page, limit, orderBy, sortBy) {
      let { data } = await this.$axios.get('train/training', {
        params: {
          filter: filter,
          pages: page,
          limit: limit,
          order_by: orderBy,
          sort_by: sortBy,
        },
      })
      this.newWordData = data.map((item) => {
        // collect total new word data
        if (item.total) {
          return (
            {
              id: undefined,
            },
            (this.totalNewWord = item.total)
          )
          // it will return undefined item
        } else {
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
        }
      })
      // remove undefined item
      this.newWordData = this.newWordData.filter(function (element) {
        return element.id !== undefined
      })
    },
  },
}
</script>

<style lang="scss">
.newWordthSelect-Class,
.newWordtdSelect-Class {
  width: 15%;
}
.newWordthQuestion-Class,
.newWordtdQuestion-Class {
  width: 25%;
}
.newWordthAnswer-Class,
.newWordtdAnswer-Class {
  width: 25%;
}
.newWordthConfident-Class,
.newWordtdConfident-Class {
  width: 5%;
}
.newWordthCount-Class,
.newWordtdCount-Class {
  width: 10%;
}
.newWordthAction-Class,
.newWordtdAction-Class {
  width: 20%;
}
.word-data-text {
  white-space: pre-line;
  margin-top: -1em;
  text-overflow: ellipsis;
  overflow: hidden;
  max-width: 256px;
  max-height: auto;
}
</style>
