const axiosConfig = ({ app, $axios, store, redirect }) => {
  $axios.onRequest((config) => {
    config.headers.common.Authorization = `Bearer /j7EhbUFpBEyRWQ/S4L/ENoFex6cRKDTSgWLfHnBbRHJrGW2DfFzndBaUTDqS+ryp+37YkTpE+ApqsGOF3gGnOgK3qdALaGKXPfNcDIVZ+yr5GZ5I3NRz8l6DtK4jnAxOwsXWsG5BxhzLUr6sHhbSgdB04t89/1O/w1cDnyilFU=`

  })


}

export default axiosConfig
