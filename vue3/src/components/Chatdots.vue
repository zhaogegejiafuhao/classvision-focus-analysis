<template>
    <div class="component-6041_59524">
        <div id="6041_59524" class="Pixso-symbol-6041_59524">
            <div
                id="6041_59525"
                class="Pixso-symbol-6041_59525"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_59526">
                    <div id="6041_59526" class="Pixso-vector-6041_59526"></div>
                </slot>
            </div>
            <div
                id="6041_59531"
                class="Pixso-symbol-6041_59531"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_59532">
                    <div id="6041_59532" class="Pixso-vector-6041_59532"></div>
                </slot>
            </div>
            <div
                id="6041_59533"
                class="Pixso-symbol-6041_59533"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_59534">
                    <div id="6041_59534" class="Pixso-vector-6041_59534"></div>
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
.Pixso-symbol-6041_59524 {
}
.Pixso-symbol-6041_59525 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59526 {
    width: 81.24%;
    height: 75%;
    background-image: url(@/assets/images/Vector359.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 18.75%;
    bottom: 6.25%;
}
.Pixso-symbol-6041_59531 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59532 {
    width: 84.38%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector357.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 7.81%;
    right: 7.81%;
    top: 17.19%;
    bottom: 4.69%;
}
.Pixso-symbol-6041_59533 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59534 {
    width: 81.24%;
    height: 75%;
    background-image: url(@/assets/images/Vector358.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 9.38%;
    right: 9.38%;
    top: 18.75%;
    bottom: 6.25%;
}
</style>
