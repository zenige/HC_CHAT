<template>
    <div>
        <h1>2222</h1>
    </div>
</template>
<script>
import Vue from 'vue'
export default {
mounted(){
       Vue.loadScript('https://static.line-scdn.net/liff/edge/2/sdk.js')
      .then(() => {
        // Script is loaded, do something
        liff
          .init({
            liffId: '1655993001-QLqyKnVe',
          })
          .then(() => {
                   liff.sendMessages([
          {
            type: 'text',
            text: 'Hello, World!'
          }
        ])
          .then(() => {
            console.log('message sent');
          })
          .catch((err) => {
            console.log('error', err);
          });
            console.log('PASS')
          })
      })
      .catch((err) => {
        console.log('f', err)
        // Failed to fetch script
      })
}
}
</script>