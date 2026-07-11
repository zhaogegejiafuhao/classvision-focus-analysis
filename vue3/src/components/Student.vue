<template>
    <div class="component-6042_8540">
        <div id="6042_8540" class="Pixso-symbol-6042_8540">
            <div
                id="6042_8541"
                class="Pixso-symbol-6042_8541"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6042_8542">
                    <div id="6042_8542" class="Pixso-vector-6042_8542"></div>
                </slot>
            </div>
            <div
                id="6042_8547"
                class="Pixso-symbol-6042_8547"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6042_8548">
                    <div id="6042_8548" class="Pixso-vector-6042_8548"></div>
                </slot>
            </div>
            <div
                id="6042_8549"
                class="Pixso-symbol-6042_8549"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6042_8550">
                    <div id="6042_8550" class="Pixso-vector-6042_8550"></div>
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
.Pixso-symbol-6042_8540 {
}
.Pixso-symbol-6042_8541 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8542 {
    width: 81.25%;
    height: 78.17%;
    background-image: url(@/assets/images/Vector116.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.37%;
    top: 9.37%;
    bottom: 12.46%;
}
.Pixso-symbol-6042_8547 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8548 {
    width: 84.37%;
    height: 81.31%;
    background-image: url(@/assets/images/Vector114.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.82%;
    top: 7.81%;
    bottom: 10.88%;
}
.Pixso-symbol-6042_8549 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8550 {
    width: 81.25%;
    height: 78.17%;
    background-image: url(@/assets/images/Vector115.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.37%;
    top: 9.37%;
    bottom: 12.46%;
}
</style>
