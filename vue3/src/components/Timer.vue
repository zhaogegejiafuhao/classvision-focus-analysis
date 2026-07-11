<template>
    <div class="component-6041_64814">
        <div id="6041_64814" class="Pixso-symbol-6041_64814">
            <div
                id="6041_64815"
                class="Pixso-symbol-6041_64815"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_64816">
                    <div id="6041_64816" class="Pixso-vector-6041_64816"></div>
                </slot>
            </div>
            <div
                id="6041_64821"
                class="Pixso-symbol-6041_64821"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_64822">
                    <div id="6041_64822" class="Pixso-vector-6041_64822"></div>
                </slot>
            </div>
            <div
                id="6041_64823"
                class="Pixso-symbol-6041_64823"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_64824">
                    <div id="6041_64824" class="Pixso-vector-6041_64824"></div>
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
.Pixso-symbol-6041_64814 {
}
.Pixso-symbol-6041_64815 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_64816 {
    width: 75%;
    height: 87.49%;
    background-image: url(@/assets/images/Vector380.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 3.13%;
    bottom: 9.38%;
}
.Pixso-symbol-6041_64821 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_64822 {
    width: 75%;
    height: 90.63%;
    background-image: url(@/assets/images/Vector378.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 1.56%;
    bottom: 7.81%;
}
.Pixso-symbol-6041_64823 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_64824 {
    width: 75%;
    height: 87.49%;
    background-image: url(@/assets/images/Vector379.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 3.13%;
    bottom: 9.38%;
}
</style>
