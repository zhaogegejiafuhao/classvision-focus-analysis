<template>
    <div class="component-5578_150325">
        <div id="5578_150325" class="Pixso-symbol-5578_150325">
            <div
                id="5578_150326"
                class="Pixso-symbol-5578_150326"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150327">
                    <div
                        id="5578_150327"
                        class="Pixso-vector-5578_150327"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150332"
                class="Pixso-symbol-5578_150332"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150333">
                    <div
                        id="5578_150333"
                        class="Pixso-vector-5578_150333"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150334"
                class="Pixso-symbol-5578_150334"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150335">
                    <div
                        id="5578_150335"
                        class="Pixso-vector-5578_150335"
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
.Pixso-symbol-5578_150325 {
}
.Pixso-symbol-5578_150326 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150327 {
    width: 87.51%;
    height: 81.26%;
    background-image: url(@/assets/images/Vector89.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.24%;
    right: 6.25%;
    top: 9.37%;
    bottom: 9.37%;
}
.Pixso-symbol-5578_150332 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150333 {
    width: 90.61%;
    height: 84.38%;
    background-image: url(@/assets/images/Vector87.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.7%;
    right: 4.69%;
    top: 7.81%;
    bottom: 7.81%;
}
.Pixso-symbol-5578_150334 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150335 {
    width: 87.51%;
    height: 81.27%;
    background-image: url(@/assets/images/Vector88.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.24%;
    right: 6.25%;
    top: 9.37%;
    bottom: 9.36%;
}
</style>
