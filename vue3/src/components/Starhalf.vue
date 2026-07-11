<template>
    <div class="component-6041_60387">
        <div id="6041_60387" class="Pixso-symbol-6041_60387">
            <div
                id="6041_60388"
                class="Pixso-symbol-6041_60388"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_60389">
                    <div id="6041_60389" class="Pixso-vector-6041_60389"></div>
                </slot>
            </div>
            <div
                id="6041_60394"
                class="Pixso-symbol-6041_60394"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_60395">
                    <div id="6041_60395" class="Pixso-vector-6041_60395"></div>
                </slot>
            </div>
            <div
                id="6041_60396"
                class="Pixso-symbol-6041_60396"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_60397">
                    <div id="6041_60397" class="Pixso-vector-6041_60397"></div>
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
.Pixso-symbol-6041_60387 {
}
.Pixso-symbol-6041_60388 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60389 {
    width: 87.48%;
    height: 84.36%;
    background-image: url(@/assets/images/Vector347.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.27%;
    right: 6.25%;
    top: 6.25%;
    bottom: 9.39%;
}
.Pixso-symbol-6041_60394 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60395 {
    width: 90.63%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector345.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.68%;
    right: 4.69%;
    top: 4.69%;
    bottom: 7.81%;
}
.Pixso-symbol-6041_60396 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60397 {
    width: 87.5%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector346.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 9.38%;
}
</style>
