<template>
    <div class="component-6041_59176">
        <div id="6041_59176" class="Pixso-symbol-6041_59176">
            <div
                id="6041_59177"
                class="Pixso-symbol-6041_59177"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_59178">
                    <div id="6041_59178" class="Pixso-vector-6041_59178"></div>
                </slot>
            </div>
            <div
                id="6041_59179"
                class="Pixso-symbol-6041_59179"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_59180">
                    <div id="6041_59180" class="Pixso-vector-6041_59180"></div>
                </slot>
            </div>
            <div
                id="6041_59181"
                class="Pixso-symbol-6041_59181"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_59182">
                    <div id="6041_59182" class="Pixso-vector-6041_59182"></div>
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
.Pixso-symbol-6041_59176 {
}
.Pixso-symbol-6041_59177 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59178 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector353.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 15.63%;
    bottom: 6.25%;
}
.Pixso-symbol-6041_59179 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59180 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector351.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 14.06%;
    bottom: 4.69%;
}
.Pixso-symbol-6041_59181 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59182 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector352.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 15.63%;
    bottom: 6.25%;
}
</style>
