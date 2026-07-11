<template>
    <div class="component-6041_60354">
        <div id="6041_60354" class="Pixso-symbol-6041_60354">
            <div
                id="6041_60355"
                class="Pixso-symbol-6041_60355"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_60356">
                    <div id="6041_60356" class="Pixso-vector-6041_60356"></div>
                </slot>
            </div>
            <div
                id="6041_60361"
                class="Pixso-symbol-6041_60361"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_60362">
                    <div id="6041_60362" class="Pixso-vector-6041_60362"></div>
                </slot>
            </div>
            <div
                id="6041_60363"
                class="Pixso-symbol-6041_60363"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_60364">
                    <div id="6041_60364" class="Pixso-vector-6041_60364"></div>
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
.Pixso-symbol-6041_60354 {
}
.Pixso-symbol-6041_60355 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60356 {
    width: 87.5%;
    height: 71.87%;
    background-image: url(@/assets/images/Vector365.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 9.38%;
    bottom: 18.75%;
}
.Pixso-symbol-6041_60361 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60362 {
    width: 90.62%;
    height: 75.02%;
    background-image: url(@/assets/images/Vector363.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 7.81%;
    bottom: 17.17%;
}
.Pixso-symbol-6041_60363 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60364 {
    width: 87.5%;
    height: 71.89%;
    background-image: url(@/assets/images/Vector364.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 9.37%;
    bottom: 18.74%;
}
</style>
