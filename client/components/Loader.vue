<template>
  <div class="loader-wrapper">
    <div class="loadingio-spinner-rolling-6fwh28et5m2">
      <div class="ldio-wvkv8a4l8u">
        <div></div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.loader-wrapper {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: center;
  width: 100%;

  @keyframes ldio-wvkv8a4l8u {
    0% {
      transform: translate(-50%, -50%) rotate(0deg);
    }
    100% {
      transform: translate(-50%, -50%) rotate(360deg);
    }
  }

  .ldio-wvkv8a4l8u div {
    position: absolute;
    width: 40px;
    height: 40px;
    border: 4px solid #cccccc;
    border-top-color: transparent;
    border-radius: 50%;
  }

  .ldio-wvkv8a4l8u div {
    animation: ldio-wvkv8a4l8u 1s linear infinite;
    top: 100px;
    left: 100px;
  }

  .loadingio-spinner-rolling-6fwh28et5m2 {
    width: 200px;
    height: 200px;
    display: inline-block;
    overflow: hidden;
    background: rgba(0, 0, 0, 0);
  }

  .ldio-wvkv8a4l8u {
    width: 100%;
    height: 100%;
    position: relative;
    transform: translateZ(0) scale(1);
    backface-visibility: hidden;
    transform-origin: 0 0;
  }

  .ldio-wvkv8a4l8u div {
    box-sizing: content-box;
  }
}
</style>
