<template>
    <div class="component-6041_60509">
        <div id="6041_60509" class="Pixso-symbol-6041_60509">
            <div
                id="6041_60510"
                class="Pixso-symbol-6041_60510"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_60511">
                    <div id="6041_60511" class="Pixso-vector-6041_60511"></div>
                </slot>
            </div>
            <div
                id="6041_60512"
                class="Pixso-symbol-6041_60512"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_60513">
                    <div id="6041_60513" class="Pixso-vector-6041_60513"></div>
                </slot>
            </div>
            <div
                id="6041_60514"
                class="Pixso-symbol-6041_60514"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_60515">
                    <div id="6041_60515" class="Pixso-vector-6041_60515"></div>
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
.Pixso-symbol-6041_60509 {
}
.Pixso-symbol-6041_60510 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60511 {
    width: 87.5%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector362.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-6041_60512 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60513 {
    width: 90.62%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector360.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-symbol-6041_60514 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60515 {
    width: 87.5%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector361.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 18.75%;
    bottom: 18.75%;
}
</style>
