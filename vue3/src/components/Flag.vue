<template>
    <div class="component-6041_61777">
        <div id="6041_61777" class="Pixso-symbol-6041_61777">
            <div
                id="6041_61778"
                class="Pixso-symbol-6041_61778"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_61779">
                    <div id="6041_61779" class="Pixso-vector-6041_61779"></div>
                </slot>
            </div>
            <div
                id="6041_61784"
                class="Pixso-symbol-6041_61784"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_61785">
                    <div id="6041_61785" class="Pixso-vector-6041_61785"></div>
                </slot>
            </div>
            <div
                id="6041_61786"
                class="Pixso-symbol-6041_61786"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_61787">
                    <div id="6041_61787" class="Pixso-vector-6041_61787"></div>
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
.Pixso-symbol-6041_61777 {
}
.Pixso-symbol-6041_61778 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61779 {
    width: 75.01%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector335.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 9.36%;
    top: 12.5%;
    bottom: 9.38%;
}
.Pixso-symbol-6041_61784 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61785 {
    width: 78.13%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector333.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 7.81%;
    top: 10.94%;
    bottom: 7.81%;
}
.Pixso-symbol-6041_61786 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_61787 {
    width: 74.99%;
    height: 78.11%;
    background-image: url(@/assets/images/Vector334.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.63%;
    right: 9.38%;
    top: 12.51%;
    bottom: 9.38%;
}
</style>
