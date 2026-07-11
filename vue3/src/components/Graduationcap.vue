<template>
    <div class="component-6042_8449">
        <div id="6042_8449" class="Pixso-symbol-6042_8449">
            <div
                id="6042_8450"
                class="Pixso-symbol-6042_8450"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6042_8451">
                    <div id="6042_8451" class="Pixso-vector-6042_8451"></div>
                </slot>
            </div>
            <div
                id="6042_8456"
                class="Pixso-symbol-6042_8456"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6042_8457">
                    <div id="6042_8457" class="Pixso-vector-6042_8457"></div>
                </slot>
            </div>
            <div
                id="6042_8458"
                class="Pixso-symbol-6042_8458"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6042_8459">
                    <div id="6042_8459" class="Pixso-vector-6042_8459"></div>
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
.Pixso-symbol-6042_8449 {
}
.Pixso-symbol-6042_8450 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8451 {
    width: 100%;
    height: 87.49%;
    background-image: url(@/assets/images/Vector110.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 9.38%;
    bottom: 3.13%;
}
.Pixso-symbol-6042_8456 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8457 {
    width: 100%;
    height: 90.63%;
    background-image: url(@/assets/images/Vector108.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 7.81%;
    bottom: 1.56%;
}
.Pixso-symbol-6042_8458 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6042_8459 {
    width: 100%;
    height: 87.49%;
    background-image: url(@/assets/images/Vector109.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0%;
    right: 0%;
    top: 9.38%;
    bottom: 3.13%;
}
</style>
