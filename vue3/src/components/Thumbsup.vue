<template>
    <div class="component-6041_59183">
        <div id="6041_59183" class="Pixso-symbol-6041_59183">
            <div
                id="6041_59184"
                class="Pixso-symbol-6041_59184"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_6041_59185">
                    <div id="6041_59185" class="Pixso-vector-6041_59185"></div>
                </slot>
            </div>
            <div
                id="6041_59186"
                class="Pixso-symbol-6041_59186"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_6041_59187">
                    <div id="6041_59187" class="Pixso-vector-6041_59187"></div>
                </slot>
            </div>
            <div
                id="6041_59188"
                class="Pixso-symbol-6041_59188"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_6041_59189">
                    <div id="6041_59189" class="Pixso-vector-6041_59189"></div>
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
.Pixso-symbol-6041_59183 {
}
.Pixso-symbol-6041_59184 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59185 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector356.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 15.63%;
}
.Pixso-symbol-6041_59186 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59187 {
    width: 90.62%;
    height: 81.25%;
    background-image: url(@/assets/images/Vector354.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.69%;
    right: 4.69%;
    top: 4.69%;
    bottom: 14.06%;
}
.Pixso-symbol-6041_59188 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-6041_59189 {
    width: 87.5%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector355.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.25%;
    top: 6.25%;
    bottom: 15.63%;
}
</style>
