<template>
    <div class="component-5578_149466">
        <div id="5578_149466" class="Pixso-symbol-5578_149466">
            <div
                id="5578_149467"
                class="Pixso-symbol-5578_149467"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_149468">
                    <div
                        id="5578_149468"
                        class="Pixso-vector-5578_149468"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149473"
                class="Pixso-symbol-5578_149473"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_149474">
                    <div
                        id="5578_149474"
                        class="Pixso-vector-5578_149474"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_149475"
                class="Pixso-symbol-5578_149475"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_149476">
                    <div
                        id="5578_149476"
                        class="Pixso-vector-5578_149476"
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
.Pixso-symbol-5578_149466 {
}
.Pixso-symbol-5578_149467 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149468 {
    width: 74.99%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector35.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.51%;
    right: 12.5%;
    top: 9.38%;
    bottom: 9.38%;
}
.Pixso-symbol-5578_149473 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149474 {
    width: 78.12%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector33.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 10.94%;
    right: 10.94%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_149475 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_149476 {
    width: 74.99%;
    height: 81.24%;
    background-image: url(@/assets/images/Vector34.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.51%;
    top: 9.38%;
    bottom: 9.38%;
}
</style>
