<template>
    <div class="component-5578_150490">
        <div id="5578_150490" class="Pixso-symbol-5578_150490">
            <div
                id="5578_150491"
                class="Pixso-symbol-5578_150491"
                v-if="Format === 'Outline' && Weight === 'Regular'"
            >
                <slot name="slot_5578_150492">
                    <div
                        id="5578_150492"
                        class="Pixso-vector-5578_150492"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150497"
                class="Pixso-symbol-5578_150497"
                v-if="Format === 'Outline' && Weight === 'Bold'"
            >
                <slot name="slot_5578_150498">
                    <div
                        id="5578_150498"
                        class="Pixso-vector-5578_150498"
                    ></div>
                </slot>
            </div>
            <div
                id="5578_150499"
                class="Pixso-symbol-5578_150499"
                v-if="Format === 'Outline' && Weight === 'Fill'"
            >
                <slot name="slot_5578_150500">
                    <div
                        id="5578_150500"
                        class="Pixso-vector-5578_150500"
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
.Pixso-symbol-5578_150490 {
}
.Pixso-symbol-5578_150491 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150492 {
    width: 87.51%;
    height: 75.01%;
    background-image: url(@/assets/images/Vector101.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 6.25%;
    right: 6.24%;
    top: 12.49%;
    bottom: 12.5%;
}
.Pixso-symbol-5578_150497 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150498 {
    width: 90.64%;
    height: 78.12%;
    background-image: url(@/assets/images/Vector99.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 4.67%;
    right: 4.69%;
    top: 10.94%;
    bottom: 10.94%;
}
.Pixso-symbol-5578_150499 {
    width: 24px;
    height: 24px;
    position: relative;
    background-color: transparent;
}
.Pixso-vector-5578_150500 {
    width: 75%;
    height: 75%;
    background-image: url(@/assets/images/Vector100.svg);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    position: absolute;
    left: 12.5%;
    right: 12.5%;
    top: 12.5%;
    bottom: 12.5%;
}
</style>
