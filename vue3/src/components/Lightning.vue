<template>
    <div class="component-5578_150457">
        <div id="5578_150457" class="Pixso-symbol-5578_150457">
            <div
                id="5578_150458"
                class="Pixso-symbol-5578_150458"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150459">
                    <div
                        id="5578_150459"
                        class="Pixso-vector-5578_150459"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150464"
                class="Pixso-symbol-5578_150464"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150465">
                    <div
                        id="5578_150465"
                        class="Pixso-vector-5578_150465"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150466"
                class="Pixso-symbol-5578_150466"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150467">
                    <div
                        id="5578_150467"
                        class="Pixso-vector-5578_150467"
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
.Pixso-symbol-5578_150457 {
}
.Pixso-symbol-5578_150458 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150459 {
    width: 68.76%;
    height: 93.72%;
    background-image: url(@/assets/images/Vector95.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.61%;
    right: 15.63%;
    top: 3.14%;
    bottom: 3.14%;
}
.Pixso-symbol-5578_150464 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150465 {
    width: 71.88%;
    height: 96.9%;
    background-image: url(@/assets/images/Vector93.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 14.06%;
    right: 14.06%;
    top: 1.55%;
    bottom: 1.55%;
}
.Pixso-symbol-5578_150466 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150467 {
    width: 68.74%;
    height: 93.76%;
    background-image: url(@/assets/images/Vector94.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 15.62%;
    right: 15.64%;
    top: 3.11%;
    bottom: 3.13%;
}
</style>
