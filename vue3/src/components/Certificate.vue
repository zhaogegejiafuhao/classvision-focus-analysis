<template>
    <div class="component-6042_8343">
        <div id="6042_8343" class="Pixso-symbol-6042_8343">
            <div
                id="6042_8344"
                class="Pixso-symbol-6042_8344"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6042_8345">
                    <div id="6042_8345" class="Pixso-vector-6042_8345"></div>
                </slot>
            </div>
            <div
                id="6042_8350"
                class="Pixso-symbol-6042_8350"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6042_8351">
                    <div id="6042_8351" class="Pixso-vector-6042_8351"></div>
                </slot>
            </div>
            <div
                id="6042_8352"
                class="Pixso-symbol-6042_8352"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6042_8353">
                    <div id="6042_8353" class="Pixso-vector-6042_8353"></div>
                </slot>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
const props = defineProps({
    Format: { type: String },
    Weight: { type: String }
});
</script>
<style>
.Pixso-symbol-6042_8343 {
}
.Pixso-symbol-6042_8344 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8345 {
    width: 87.49%;
    height: 75.02%;
    background-image: url(@/assets/images/Vector104.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 3.13%;
    top: 15.63%;
    bottom: 9.35%;
}
.Pixso-symbol-6042_8350 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8351 {
    width: 90.63%;
    height: 79.7%;
    background-image: url(@/assets/images/Vector102.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 1.56%;
    top: 14.06%;
    bottom: 6.24%;
}
.Pixso-symbol-6042_8352 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8353 {
    width: 87.49%;
    height: 75.02%;
    background-image: url(@/assets/images/Vector103.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 3.13%;
    top: 15.63%;
    bottom: 9.35%;
}
</style>
