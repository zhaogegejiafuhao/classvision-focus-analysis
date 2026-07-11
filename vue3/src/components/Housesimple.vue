<template>
    <div class="component-6041_60586">
        <div id="6041_60586" class="Pixso-symbol-6041_60586">
            <div
                id="6041_60587"
                class="Pixso-symbol-6041_60587"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_60588">
                    <div id="6041_60588" class="Pixso-vector-6041_60588"></div>
                </slot>
            </div>
            <div
                id="6041_60589"
                class="Pixso-symbol-6041_60589"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_60590">
                    <div id="6041_60590" class="Pixso-vector-6041_60590"></div>
                </slot>
            </div>
            <div
                id="6041_60591"
                class="Pixso-symbol-6041_60591"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_60592">
                    <div id="6041_60592" class="Pixso-vector-6041_60592"></div>
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
.Pixso-symbol-6041_60586 {
}
.Pixso-symbol-6041_60587 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60588 {
    width: 75%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector341.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 9.37%;
    bottom: 12.5%;
}
.Pixso-symbol-6041_60589 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60590 {
    width: 78.12%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector339.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 10.94%;
}
.Pixso-symbol-6041_60591 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_60592 {
    width: 75%;
    height: 78.13%;
    background-image: url(@/assets/images/Vector340.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 9.37%;
    bottom: 12.5%;
}
</style>
