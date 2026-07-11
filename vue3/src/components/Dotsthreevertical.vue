<template>
    <div class="component-5578_150138">
        <div id="5578_150138" class="Pixso-symbol-5578_150138">
            <div
                id="5578_150139"
                class="Pixso-symbol-5578_150139"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150140">
                    <div
                        id="5578_150140"
                        class="Pixso-vector-5578_150140"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150145"
                class="Pixso-symbol-5578_150145"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150146">
                    <div
                        id="5578_150146"
                        class="Pixso-vector-5578_150146"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150147"
                class="Pixso-symbol-5578_150147"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150148">
                    <div
                        id="5578_150148"
                        class="Pixso-vector-5578_150148"
                    ></div>
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
.Pixso-symbol-5578_150138 {
}
.Pixso-symbol-5578_150139 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150140 {
    width: 9.38%;
    height: 62.5%;
    background-image: url(@/assets/images/Vector71.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 45.31%;
    right: 45.31%;
    top: 18.75%;
    bottom: 18.75%;
}
.Pixso-symbol-5578_150145 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150146 {
    width: 12.5%;
    height: 65.62%;
    background-image: url(@/assets/images/Vector69.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 43.75%;
    right: 43.75%;
    top: 17.19%;
    bottom: 17.19%;
}
.Pixso-symbol-5578_150147 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150148 {
    width: 37.5%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector70.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 31.25%;
    right: 31.25%;
    top: 6.25%;
    bottom: 6.25%;
}
</style>
