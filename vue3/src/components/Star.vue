<template>
    <div class="component-6041_59162">
        <div id="6041_59162" class="Pixso-symbol-6041_59162">
            <div
                id="6041_59163"
                class="Pixso-symbol-6041_59163"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_59164">
                    <div id="6041_59164" class="Pixso-vector-6041_59164"></div>
                </slot>
            </div>
            <div
                id="6041_59165"
                class="Pixso-symbol-6041_59165"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_59166">
                    <div id="6041_59166" class="Pixso-vector-6041_59166"></div>
                </slot>
            </div>
            <div
                id="6041_59167"
                class="Pixso-symbol-6041_59167"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_59168">
                    <div id="6041_59168" class="Pixso-vector-6041_59168"></div>
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
.Pixso-symbol-6041_59162 {
}
.Pixso-symbol-6041_59163 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59164 {
    width: 87.5%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector338.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 9.38%;
}
.Pixso-symbol-6041_59165 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59166 {
    width: 90.64%;
    height: 87.51%;
    background-image: url(@/assets/images/Vector336.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.68%;
    right: 4.68%;
    top: 4.69%;
    bottom: 7.8%;
}
.Pixso-symbol-6041_59167 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59168 {
    width: 87.45%;
    height: 84.37%;
    background-image: url(@/assets/images/Vector337.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.27%;
    right: 6.28%;
    top: 6.25%;
    bottom: 9.38%;
}
</style>
