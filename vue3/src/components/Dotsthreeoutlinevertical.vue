<template>
    <div class="component-5578_150093">
        <div id="5578_150093" class="Pixso-symbol-5578_150093">
            <div
                id="5578_150094"
                class="Pixso-symbol-5578_150094"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150095">
                    <div
                        id="5578_150095"
                        class="Pixso-vector-5578_150095"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150100"
                class="Pixso-symbol-5578_150100"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150101">
                    <div
                        id="5578_150101"
                        class="Pixso-vector-5578_150101"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150102"
                class="Pixso-symbol-5578_150102"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150103">
                    <div
                        id="5578_150103"
                        class="Pixso-vector-5578_150103"
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
.Pixso-symbol-5578_150093 {
}
.Pixso-symbol-5578_150094 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150095 {
    width: 25%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector65.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 37.5%;
    right: 37.5%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-symbol-5578_150100 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150101 {
    width: 25%;
    height: 87.5%;
    background-image: url(@/assets/images/Vector63.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 37.5%;
    right: 37.5%;
    top: 6.25%;
    bottom: 6.25%;
}
.Pixso-symbol-5578_150102 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150103 {
    width: 21.88%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector64.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 39.06%;
    right: 39.06%;
    top: 7.81%;
    bottom: 7.81%;
}
</style>
