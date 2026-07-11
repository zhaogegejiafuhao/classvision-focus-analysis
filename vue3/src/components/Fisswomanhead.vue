<template>
    <div class="component-1_12">
        <div id="1_12" class="Pixso-symbol-1_12">
            <slot name="slot_1_13">
                <div id="1_13" class="Pixso-vector-1_13"></div>
            </slot>
            <slot name="slot_1_14">
                <div id="1_14" class="Pixso-vector-1_14"></div>
            </slot>
        </div>
    </div>
</template>
<script lang="ts" setup></script>
<style>
.Pixso-symbol-1_12 {
    width: 24px;
    height: 24px;
    overflow: hidden;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-1_13 {
    width: 100.01%;
    height: 100.02%;
    background-image: url(@/assets/images/Vector3.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: -0.01%;
    top: -0.02%;
    bottom: 0%;
}
.Pixso-vector-1_14 {
    width: 12.5%;
    height: 12.5%;
    background-image: url(@/assets/images/Vector2.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 54.17%;
    right: 33.33%;
    top: 41.66%;
    bottom: 45.84%;
}
</style>
