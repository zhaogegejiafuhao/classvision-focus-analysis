<template>
    <div class="component-5579_152486">
        <div id="5579_152486" class="Pixso-symbol-5579_152486">
            <div
                id="5579_152487"
                class="Pixso-symbol-5579_152487"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5579_152488">
                    <div
                        id="5579_152488"
                        class="Pixso-vector-5579_152488"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152493"
                class="Pixso-symbol-5579_152493"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5579_152494">
                    <div
                        id="5579_152494"
                        class="Pixso-vector-5579_152494"
                    ></div>
                </slot>
            </div>
            <div
                id="5579_152495"
                class="Pixso-symbol-5579_152495"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5579_152496">
                    <div
                        id="5579_152496"
                        class="Pixso-vector-5579_152496"
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
.Pixso-symbol-5579_152486 {
}
.Pixso-symbol-5579_152487 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152488 {
    width: 98.28%;
    height: 62.55%;
    background-image: url(@/assets/images/Vector56.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.85%;
    right: 0.87%;
    top: 18.74%;
    bottom: 18.71%;
}
.Pixso-symbol-5579_152493 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152494 {
    width: 99.21%;
    height: 64.1%;
    background-image: url(@/assets/images/Vector54.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.39%;
    right: 0.4%;
    top: 17.17%;
    bottom: 18.73%;
}
.Pixso-symbol-5579_152495 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5579_152496 {
    width: 98.27%;
    height: 62.51%;
    background-image: url(@/assets/images/Vector55.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 0.87%;
    right: 0.86%;
    top: 18.74%;
    bottom: 18.75%;
}
</style>
